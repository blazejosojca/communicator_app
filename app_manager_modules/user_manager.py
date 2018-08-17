import argparse

from database.db_production import connect_to_db, close_connection
from models.user import User


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store",
                        dest="username", help="User login")
    parser.add_argument("-p", "--password", action="store",
                        dest="password", help="User password")
    parser.add_argument("-n", "--new-password", action="store",
                        dest="new_password", help="New user password")
    parser.add_argument("-l", "--list", action="store_true",
                        dest="list", help="Get users list")
    parser.add_argument("-d", "--delete", action="store",
                        dest="delete", help="Delete user")
    parser.add_argument("-e", "--edit", action="store",
                        dest="edit", help="Edit user")
    options = parser.parse_args()
    return options

def manage_users(options):
    options = set_options()

    def delete_user(cursor, options):
        deleted_user = User()
        if deleted_user.verify_user() is T

