import time
from models.user import User
from database.db_production import connect_to_db, close_connection

#TODO finish all methods
class Message:
    def __init__(self, from_user, to_user, text):
        self.from_user = from_user
        self.to_user = to_user
        self.text = text
        self.creation_date = ''

    @property
    def message_id(self):
        return self.__id

    def save_message_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO message(from_user_id, to_user_id, text, creation_date)
                        VALUES (%s, %s, %s, %s, '%s')
                      """
            send_time = time.strftime('%Y-%m-%d %H:%M:%S')
            values = (self.from_user, self.to_user, self.text, send_time)
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
            loaded_message.from_user = data[1]
            loaded_message.to_user = data[2]
            loaded_message.text = data[3]
            return loaded_message
        return None

    @staticmethod
    def load_all_messages(cursor):
        pass

    def load_all_messages_for_user(self, cursor):
        pass
