import mysql.connector
from mysql.connector import errorcode
from database.db_data import DATABASE
from database.db_production import close_connection, connect_to_db

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
    id int AUTO_INCREMENT,
    from_user_id int NOT NULL,
    to_user_id int NOT NULL,
    text varchar(256),
    creation_date datetime NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(from_user_id) REFERENCES users(id),
    FOREIGN KEY(to_user_id) REFERENCES users(id)
    )"""


def create_db():
    init_cnx = mysql.connector.connect(
        user=DATABASE['USER'],
        password=DATABASE['PASSWORD']
    )
    init_cursor = init_cnx.cursor()
    init_sql = f"CREATE DATABASE {DATABASE['NAME']} DEFAULT CHARACTER SET 'utf8'"
    try:
        init_cursor.execute(init_sql)
        print("DB created")
    except mysql.connector.Error:
        print(f"DB Error. Failed to create databse: {DATABASE['NAME']} ")
    finally:
        close_connection(init_cursor, init_cnx)


def create_table(sql_table):
    cnx, cursor = connect_to_db()
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

# # create_db()
# # create_table(users_table)
# # create_table(messages_table)
