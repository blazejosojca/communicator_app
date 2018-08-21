import time
from models.user import User
from database.db_production import connect_to_db, close_connection


# TODO finish all methods
class Message:
    def __init__(self):
        self.__id = -1
        self.from_user_id = ""
        self.to_user_id = ""
        self.text = ""
        self.creation_date = time.strftime('%Y-%m-%d')

    @property
    def message_id(self):
        return self.__id

    def save_message_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO messages(from_user_id, to_user_id, text, creation_date)
                        VALUES (%s, %s, %s, %s)"""
            values = (self.from_user_id, self.to_user_id, self.text, self.creation_date)
            cursor.execute(sql, values)
            return True
        return False

    @staticmethod
    def load_message_by_id(cursor, message_id):
        sql = f'SELECT * FROM messages WHERE id=%s'
        value = (message_id,)
        cursor.execute(sql, value)
        data = cursor.fetchone()

        if data is not None:
            loaded_message = Message()
            loaded_message.__id = data[0]
            loaded_message.from_user_id = data[1]
            loaded_message.to_user_id = data[2]
            loaded_message.text = data[3]
            return loaded_message
        return None

    @staticmethod
    def load_all_messages(cursor):
        sql = "SELECT * FROM messages"
        cursor.execute(sql)
        data = cursor.fetchall()

        all_mssgs = list()
        for message in data:
            loaded_message = Message()
            loaded_message.__id = message[0]
            loaded_message.from_user_id = message[1]
            loaded_message.to_user_id = message[2]
            loaded_message.text = message[3]
            loaded_message.creation_date = message[4]
            all_mssgs.append(loaded_message.__str__())
        return all_mssgs

    def load_all_messages_for_user(self, cursor):
        pass

    def __str__(self):
        return f'from {self.from_user_id} to {self.to_user_id}: {self.text} '
