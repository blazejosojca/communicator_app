import argparse

from database.db_production import connect_to_db, close_connection
from models.message import Message


def manage_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store",
                        dest="username", help="User login")
    parser.add_argument("-p", "--password", action="store",
                        dest="password", help="User password")
    parser.add_argument("-l", "--list", action="store_true",
                        dest="list", help="Get message list")
    parser.add_argument("-s", "--send", action="store",
                        dest="delete", help="Send message")
    parser.add_argument("-t", "--to", action="store",
                        dest="modify", help="Message for")

    parse_options = parser.parse_args()
    return parse_options


def manage_users(parse_options):
    cnx, cursor = connect_to_db()
# TODO write instructions for manager
    close_connection(cursor, cnx)
