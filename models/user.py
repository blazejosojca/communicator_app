from passlib.hash import argon2


class User(object):
    def __init__(self):
        self.__id = -1
        self.username = ''
        self.email = ''
        self.__hashed_password = ''

    @property
    def user_id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password):
        self.__hashed_password = argon2.hash(password)

    def save_to_db(self, cursor):
        if self.__id == -1:

            sql = """INSERT INTO users(username, email, hashed_password) 
                VALUES (%s, %s, %s)"""
            values = (self.email, self.username, self.hashed_password)
            cursor.execute(sql, values)
            print(f"User {self.username} was added to DB")
            return True
        return False


    def verify_user(self, cursor, username, password_try):
        sql = f"SELECT * FROM users WHERE username={username} LIMIT 1"
        cursor.execute(sql)
        data = cursor.fetchone()
        if data is not None:
            self.__id = data[0]
            self.email = data[2]
            self.__hashed_password = data[3]
        if argon2.verify(password_try,self.__hashed_password):
            return True
        return False

    def update_password(self, cursor):
        sql = 'UPDATE users SET hashed_password=%s WHERE id=%s'
        values = (self.hashed_password, self.__id)
        cursor.execute(sql, values)
        return True


    @staticmethod
    def load_by_user_id(cursor, user_id):
        sql = f'SELECT * FROM users WHERE id={user_id}'
        cursor.execute(sql)
        data = cursor.fetchone()

        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        data = cursor.fetchall()

        all_users = list()
        for user in data:
            loaded_user = User()
            loaded_user.__id = user[0]
            loaded_user.username = user[1]
            loaded_user.email = user[2]
            loaded_user.__hashed_password = user[3]
            all_users.append(loaded_user)
        return all_users

    def delete(self, cursor):
        sql = "DELETE FROM users WHERE id=%s"
        cursor.execute(sql, self.__id)
        self.__id = -1
        return True

    def __repr__(self):
        pass

    def __str__(self):
        return  'User: {}, id: {}, email:{}'.format(self.username, self.__id, self.email)