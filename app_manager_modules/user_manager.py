import argparse
from models.user import User
from models.message import Message
from database.db_production import connect_to_db, close_connection


def arg_options():
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
    parser.add_argument("-r", "--remove", action="store",
                        dest="remove", help="Remove user")
    parser.add_argument("-m", "--modify", action="store",
                        dest="modify", help="Modify user")
    parser.add_argument("-id", "--user-id", action="store", type=int,
                        dest="user_id", help="User id")
    parser.add_argument("-v", "--view_user", action="store_true",
                        dest="view", help="View user by id")

    parse_options = parser.parse_args()
    return parse_options


def arg_manager(parse_options):

    def remove_user_by_name(cursor, parse_options):
        user_to_remove = User()
        if user_to_remove.verify_user(cursor, parse_options.username, parse_options.password):
            user_to_remove.remove_user(cursor)
            print(f'User{parse_options.username} was removed')
        else:
            print(f'User{parse_options.username}, wasn.t removed. '
                  f'Please check credentials ')
    def

        if (all([parse_options.remove, parse_options.username, parse_options.password]) and
                not any([parse_options.list, parse_options.new_password, parse_options.modify,
                         parse_options.view, parse_options.user_id])):
            user_to_remove = User()
            if user_to_remove.verify_user(cursor, parse_options.username, parse_options.password):
                pass



    cnx, cursor = connect_to_db()

    # for save_to_db()

    if(all([parse_options.username, parse_options.email, parse_options.password])
            and not any([parse_options.remove, parse_options.list, parse_options.new_password,
                         parse_options.modify, parse_options.view, parse_options.user_id])):
        new_user = User()
        new_user.username = parse_options.username
        new_user.email = parse_options.email
        new_user.set_password(parse_options.password)
        new_user.save_to_db(cursor)
        print(f"New user was added to db."
              f"Name:{parse_options}")

    # for remove_user()
    if (all([parse_options.username, parse_options.password]) and
            not any([parse_options.list, parse_options.new_password, parse_options.modify,
                     parse_options.view, parse_options.user_id])):
        remove_user_by_name(cursor, parse_options)


    # for load_all_users()
    if(parse_options.list
            and not any([parse_options.remove, parse_options.new_password, parse_options.modify,
                         parse_options.new_password, parse_options.view])):
        users = User.load_all_users(cursor)
        for user in users:
            print(user)

    # for remove user by id


    # for load_user_by_id()
    if (all([parse_options.view, parse_options.user_id]) and
            not any([parse_options.username, parse_options.password, parse_options.new_password, parse_options.modify,
                     parse_options.remove])):
        user_by_id = User.load_by_user_id(cursor, parse_options.user_id)
        print(user_by_id)

    # for update_password()

    if (all([parse_options.username, parse_options.modify, parse_options.new_password, parse_options.password]) and
            not any([parse_options.list, parse_options.view, parse_options.user_id,
                     parse_options.remove, parse_options.email])):
        user = User()
        if user.verify_user(cursor, parse_options.username, parse_options.password):
            user.set_password(parse_options.new_password)
            user.update_password(cursor)
            print(f'Updated password for user:{parse_options.username}')
        else:
            print('Pasword wasn\'t changed.'
                  'Please check credentials.')

    close_connection(cursor, cnx)

if __name__ == '__main__':
    arg_manager(arg_options())

