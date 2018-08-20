import time
from .user import User

class Message(object):
    def __init__(self, from_id, to_id, text):
        self.__id = -1
        self.from_user_id = from_id
        self.to_user_id = to_id
        self.text = text
        self.creation_date = ''

        @property
        def message_id(self):
            return self.__id


        def create_message(self, cursor):
            sql = """INSERT INTO message(from_user_id, to_user_id, text, creation_date)
                    VALUES (%s, %s, %s, %s, '%s')
                  """
            send_time = time.strftime('%Y-%m-%d %H:%M:%S')
            values = (self.from_user_id, self.to_user_id, self.text, send_time)
            cursor.execute(sql, values)
            return True


        @staticmethod
        def load_message_by_from_user_id(cursor, user_id):
            sql = f'SELECT * FROM messages WHERE from_user_id = {user_id}'
            cursor.execute(sql)
            data = cursor.fetchone()

            if data is not None:
                loaded_message = Message()
                loaded_message.__id = data[0]
                loaded_message.from_user_id = data[1]
                loaded_message.to_user_id = data[2]
                loaded_message.text = data[3]
                return loaded_message
            return None


        def load_all_messages(self):
            pass

        def save_message_to_db(self):
            pass