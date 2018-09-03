import argparse
from models.user import User
from models.message import Message
from database.db_production import close_connection, connect_to_db


parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('-u', '--username', action='store', dest='username', help='User name')
parent_parser.add_argument('-p', '--password', action='store', dest='password', help='User password')

main_parser = argparse.ArgumentParser()

subparsers = main_parser.add_subparsers(dest='command', help='Main commands')

create_user = subparsers.add_parser('create_user', help='Create user',
                                    parents=[parent_parser])
create_user.add_argument('-e', '--email', action='store', dest='email', help='User mail')

create_message = subparsers.add_parser('create_message', help='Create message',
                                       parents=[parent_parser])
create_message.add_argument('-to', '--to_user', action='store', dest='to_user', help="Id of recipient")
create_message.add_argument('-from', '--from_user', action='store', dest='from_user', help="Id of sende")
create_message.add_argument('-t', '--text', action='store', dest='text', help='Enter the text')

view_user = subparsers.add_parser("view_user", help='View selected user')
view_user.add_argument('-id', '--user_id', action='store', dest='id', help='Id of selected user')

view_message = subparsers.add_parser("view_message", help='View selected message', parents=[parent_parser])
view_message.add_argument('-id', '--message_id', action='store', dest='id', help='Id of selected message')

modify_password = subparsers.add_parser("modify_password", help="Modify user password",
                                        parents=[parent_parser])
modify_password.add_argument('-np' '--new_password', action='store', dest='new_password', help="New user password")

remove_user = subparsers.add_parser("remove_user", help="Remove selected users",
                                    parents=[parent_parser])

list_users = subparsers.add_parser("list_users", help="List of all users")

list_messages_for_user = subparsers.add_parser("list_messages_from_user", help="List messages for user",
                                               parents=[parent_parser])
list_messages_for_user.add_argument('-id', '--user_id', action='store', dest='id', help='Id of selected user')

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

if args.command == 'view_user':
    user = User.load_by_user_id(cursor, args.id)
    print(user)

if args.command == 'modify_password':
    user = User()
    if user.verify_user(cursor, args.username, args.password):
        user.set_password(args.new_password)
        user.update_password(cursor)
        print(f'Password was updated!')
    else:
        print('Password wasn\'t changed. Check credentials.')

if args.command == 'remove_user':
    user_to_remove = User()
    if user_to_remove.verify_user(cursor, args.username, args.password):
        user_to_remove.remove_user(cursor)
        print(f'{user_to_remove} was removed')
    else:
        print('It\'s impossible to remove this user. Please check your credentials')

if args.command == 'list_users':
    users = User.load_all_users(cursor)
    for user in users:
        print(user)

if args.command == 'create_message':
    user = User()
    if user.verify_user(cursor, args.username, args.password):
        new_message = Message()
        new_message.from_user_id = args.from_user
        new_message.to_user_id = args.to_user
        new_message.text = args.text
        Message.set_creation_date()
        new_message.save_message_to_db(cursor)
        print(f'message for user{args.to_user} was created')
    else:
        print('Your credentials don\'t work. Please check them.')

if args.command == 'view_message':
    user = User()
    if user.verify_user(cursor, args.username, args.password):
        Message().load_message_by_id(cursor, args.id)
    else:
        print('Your credentials don\'t work. Please check them.')

if args.command == 'list_messages_from_user':
    user = User()
    if user.verify_user(cursor, args.username, args.password):
        Message.load_all_messages_from_user(cursor, args.id)
    else:
        print('Your credentials don\'t work. Please check them.')

close_connection(cursor, cnx)
