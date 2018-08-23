import argparse
from .user import *
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


def args_manager(parse_options):


if __name__ == '__main__':


