import mysql.connector
from mysql.connector import connect, errorcode

# password and user cleared
DATABASE = {
    'NAME': 'communicator_app',
    'PASSWORD': 'debil1984',
    'USER': 'root'
}

users_table = """
    CREATE TABLE users (
    id int AUTO_INCREMENT,
    username varchar(64),
    email varchar (64) UNIQUE,
    PRIMARY KEY(id)
    )
    """

messages_table = """
    CREATE TABLE messages (
    message_id int AUTO_INCREMENT,
    text varchar(256),
    creation_date datetime NOT NULL,
    PRIMARY KEY(message_id)
    )"""

uses_messages_table = """
    CREATE TABLE messages_users (
    id int AUTO_INCREMENT,
    from_id int NOT NULL,
    to_id int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(from_id) REFERENCES users(id),
    FOREIGN KEY(to_id) REFERENCES users(id)
    )"""


def connect_to_db():
    cnx = connect(
        user=DATABASE['NAME'],
        password=DATABASE['PASSWORD'],
        database=DATABASE['USER'],
    )
    cursor = cnx.cursor()
    return cnx, cursor


def close_connection(cursor, cnx):
    cnx.commit()
    cursor.close()
    cnx.close()


def create_db():
    init_cnx = mysql.connector.connect(user=DATABASE['USER'], password=DATABASE['PASSWORD'])
    init_cursor = init_cnx.cursor()
    init_sql = f"CREATE DATABASE {DATABASE['NAME']} DEFAULT CHARACTER SET 'utf8'"
    try:
        init_cursor.execute(init_sql)
        print("DB created")
    except mysql.connector.Error:
        print(f"DB Error. Failed to create databse : {DATABASE['NAME']} ")
    finally:
        close_connection(init_cursor, init_cnx)


def create_table(sql_table):
    cnx = mysql.connector.connect(user=DATABASE['USER'], database = DATABASE['NAME'], password=DATABASE['PASSWORD'])
    cursor = cnx.cursor()
    try:
        cursor.execute(sql_table)
        print(f"Creating table {sql_table}")
    except mysql.connector.Error as err_db:
        if err_db == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table already exist")
        else:
            print(err_db.msg)
    finally:
        close_connection(cursor, cnx)


create_table(users_table)
create_table(messages_table)
create_table(uses_messages_table)
