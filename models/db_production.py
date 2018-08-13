import mysql.connector
from mysql.connector import connect

# password and user cleared
DATABASE = {
    'NAME': 'communicator_app',
    'PASSWORD': '##########',
    'USER': "#####"
}

TABLES = {}

TABLES['users'] = (
    """
    CREATE TABLE users (
    user_id int AUTO_INCREMENT,
    username varchar(64),
    email varchar (64) UNIQUE,
    PRIMARY KEY(user_id)
    )
    """)

TABLES['messages'] = (
    """
    CREATE TABLE messages (
    message_id int AUTO_INCREMENT,
    text varchar(256),
    creation_date datetime NOT NULL,
    PRIMARY KEY(message_id)
    )
    """)

TABLES['messages_users'] = (
    """
    CREATE TABLE messages_users (
    id int AUTO_INCREMENT,
    from_id int NOT NULL,
    to_id int NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(from_id) REFERENCES users(user_id),
    FOREIGN KEY(to_id) REFERENCES users(user_id)
    )
    """)


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
        init_cnx.close()


if __name__ == '__main__':
    create_db()
