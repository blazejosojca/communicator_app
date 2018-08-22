import argparse

from database.db_production import connect_to_db, close_connection
from models.user import User


def manage_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store",
                        dest="username", help="User login")
    parser.add_argument("-p", "--password", action="store",
                        dest="password", help="User password")
    parser.add_argument("-e", "--email", action="store",
                        dest="email", help="User mail")
    parser.add_argument("-n", "--new-password", action="store",
                        dest="new_password", help="New user password")
    parser.add_argument("-l", "--list", action="store_true",
                        dest="list", help="Get users list")
    parser.add_argument("-d", "--delete", action="store",
                        dest="delete", help="Delete user")
    parser.add_argument("-m", "--modify", action="store",
                        dest="modify", help="Modify user")

    parse_options = parser.parse_args()
    return parse_options


def manage_users(parse_options):
    cnx, cursor = connect_to_db()

    # for save_to_db()
    if(all([parse_options.username, parse_options.email, parse_options.password])
            and not any([parse_options.delete, parse_options.list, parse_options.new_password, parse_options.edit])):
        new_user = User()
        new_user.username = parse_options.username
        new_user.email = parse_options.email
        new_user.set_password(parse_options.password)
        new_user.save_to_db(cursor)
        print(f"New user was added to db."
              f"Name:{parse_options}")

    # for load_all_user()
    if(parse_options.list
            and not any([parse_options.delete, parse_options.list,    parse_options.new_password, parse_options.edit])):
        users = User.load_all_users(cursor)
        for user in users:
            print(user)

    # for delete_user()
    if(all([parse_options.delete, parse_options.username, parse_options.password]) and
            not any([parse_options.list, parse_options.new_password, parse_options.modify])):
        deleted_user = User()
        if deleted_user.verify_user(cursor, parse_options.username, parse_options.password):
            pass

    # for load_user_by_id()
    # for update_password()

    close_connection(cnx, cursor)
    # modify user


if __name__ == '__main__':
    manage_users(manage_options())
