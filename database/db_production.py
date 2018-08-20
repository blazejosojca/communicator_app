from mysql.connector import connect
from database.db_data import DATABASE


def connect_to_db():
    cnx = connect(
        user=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        database=DATABASE['NAME'],
    )
    cursor = cnx.cursor()
    return cnx, cursor


def close_connection(cursor, cnx):
    cnx.commit()
    cursor.close()
    cnx.close()
