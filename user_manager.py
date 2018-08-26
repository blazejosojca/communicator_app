import argparse
from models.user import User
from database.db_production import close_connection, connect_to_db


def arg_options():
    parser = argparse.ArgumentParser(description="communication_app", add_help=True)
    parser.add_argument("-username", action="store",
                        dest="username", help="User login")
    parser.add_argument("-password", action="store",
                        dest="password", help="User password")
    parser.add_argument("-email", action="store",
                        dest="email", help="User mail")
    parser.add_argument("-new-password", action="store",
                        dest="new_password", help="New user password")
    parser.add_argument("-list", action="store_true",
                        dest="list", help="Get users list")
    parser.add_argument("-remove", action="store",
                        dest="remove", help="Remove user")
    parser.add_argument("-modify", action="store",
                        dest="modify", help="Modify user")
    parser.add_argument("-user-id", action="store", type=int,
                        dest="user_id", help="User id")
    parser.add_argument("-v", "--view_user", action="store_true",
                        dest="view", help="View user by id")

    parse_options = parser.parse_args()
    return parse_options

# TODO - fix this