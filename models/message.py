from time import strftime


# TODO finish all methods
class Message:
    def __init__(self):
        self.__id = -1
        self.from_user_id = ""
        self.to_user_id = ""
        self.text = ""
        self.creation_date = ""

    @property
    def message_id(self):
        return self.__id

    @classmethod
    def set_creation_date(cls):
        return strftime('%Y-%m-%d')

    def save_message_to_db(self, cursor):
        if self.__id == -1:
            sql = """INSERT INTO messages(from_user_id, to_user_id, text, creation_date)
                        VALUES (%s, %s, %s, %s)"""
            values = (self.from_user_id, self.to_user_id, self.text, Message.set_creation_date())
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
            loaded_message.creation_date = data[4]
            print(loaded_message)
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

    # this method load message for user by from_user_id
    @staticmethod
    def load_all_messages_for_user(cursor, user_id):
        sql = 'SELECT * FROM messages WHERE from_user_id = %s'
        value = (user_id,)
        cursor.execute(sql, value)
        data = cursor.fetchone()

        if data is not None:
            loaded_mssg = Message()
            loaded_mssg.__id = data[0]
            loaded_mssg.from_user_id = data[1]
            loaded_mssg.to_user_id = data[2]
            loaded_mssg.text = data[3]
            loaded_mssg.creation_date = data[4]
            return loaded_mssg.__str__()
        return None

    def __str__(self):
        return f'from {self.from_user_id} to {self.to_user_id}: {self.text} / sent: {self.creation_date}'


