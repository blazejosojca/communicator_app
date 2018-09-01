import argparse
from models.user import User
from models.message import Message
from database.db_production import close_connection, connect_to_db


def view():
    print("view")


def modify():
    print("modify")


def remove():
    print("remove")


def list():
    print("list_all_users")


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('-u', '-username', action='store', dest='username', help='User name')
parent_parser.add_argument('-p', '-password', action='store', dest='password', help='User password')

main_parser = argparse.ArgumentParser()

subparsers = main_parser.add_subparsers(dest='command', help='Main commands')
create_user = subparsers.add_parser('create_user', help='Create user', parents=[parent_parser])
create_user.add_argument('-e', '--email', action='store', dest='email', help='User mail')

view_user = subparsers.add_parser("view_user", help='View selected user')
view_user.add_argument('-id', '--user_id', action='store', dest='id', help='Id of selected user')

modify_user = subparsers.add_parser("modify_user", help="Modify user", parents=[parent_parser])
modify_user.add_argument('-np' '--new_password', action='store', help="New user password")

remove_user = subparsers.add_parser("remove_user", help="Remove selected users", parents=[parent_parser])

list__users = subparsers.add_parser("list_users", help="List of all users")

args = main_parser.parse_args()
print(args)

cnx, cursor = connect_to_db()

if args.command == 'create_user':
    new_user = User()
    new_user.username = args.username
    new_user.email = args.email
    new_user.set_password(args.password)
    new_user.save_to_db(cursor)
    print("New user was aded to db - name: {new_user.usermail}")


if args.command == 'view':
    view()

if args.command == 'modify':
    modify()

if args.command == 'remove':
    remove()

if args.command == 'list_users':
    users = User.load_all_users(cursor)
    for user in users:
        print(user)

