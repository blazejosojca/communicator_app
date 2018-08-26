from mysql import connector
from mysql.connector import errorcode as db_errorcode
from manager_module.database.db_data import DATABASE


def connect_to_db():
    try:
        cnx = connector.connect(
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            database=DATABASE['NAME'],
         )
        cursor = cnx.cursor()
        return cnx, cursor
    except connector.Error as db_error:
        if db_error.errno == db_errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied, please check your credentials.")
        elif db_error.errno == db_errorcode.ER_BAD_DB_ERROR:
            print("DB dosen't exist.")
        else:
            print(db_error.msg)


def close_connection(cursor, cnx):
    cnx.commit()
    cursor.close()
    cnx.close()
