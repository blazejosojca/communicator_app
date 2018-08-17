import mysql.connector
from mysql.connector import errorcode
from database.db_data import DATABASE
from database.db_production import close_connection

users_table = """
    CREATE TABLE users (
    id int AUTO_INCREMENT,
    username varchar(64),
    email varchar(64) UNIQUE,
    hashed_password varchar(256),
    PRIMARY KEY(id)
    )
    """

messages_table = """
    CREATE TABLE messages (
    message_id int AUTO_INCREMENT,
    from_id int NOT NULL,
    to_id int NOT NULL,
    text varchar(256),
    creation_date datetime NOT NULL,
    PRIMARY KEY(message_id),
    FOREIGN KEY(from_id) REFERENCES users(id),
    FOREIGN KEY(to_id) REFERENCES users(id)
    )"""


def create_db():
    init_cnx = mysql.connector.connect(
        user=DATABASE['USER'],
        password=DATABASE['PASSWORD']
    )
    init_cursor = init_cnx.cursor()
    init_sql = f"CREATE DATABASE IF EXISTS {DATABASE['NAME']} DEFAULT CHARACTER SET 'utf8'"
    try:
        init_cursor.execute(init_sql)
        print("DB created")
    except mysql.connector.Error:
        print(f"DB Error. Failed to create databse: {DATABASE['NAME']} ")
    finally:
        close_connection(init_cursor, init_cnx)


def create_table(sql_table):
    cnx = mysql.connector.connect(
        user=DATABASE['USER'],
        database=DATABASE['NAME'],
        password=DATABASE['PASSWORD']
    )
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
