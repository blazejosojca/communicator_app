from passlib.hash import argon2
from database.db_production import connect_to_db, close_connection

#TODO finish tests
class User:
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
            values = (self.username, self.email, self.hashed_password)
            print(values)
            cursor.execute(sql, values)
            return True
        return False


    def verify_user(self, cursor, username, password_try):
        sql = "SELECT * FROM users WHERE username=%s LIMIT 1"
        value = (username, )
        cursor.execute(sql, value)
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
        sql = 'SELECT * FROM users WHERE id= %s'
        value = (user_id,)
        cursor.execute(sql, value)
        data = cursor.fetchone()

        if data is not None:
            loaded_user = User()
            loaded_user.__id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.__hashed_password = data[3]
            return loaded_user
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

    def delete_user(self, cursor):
        sql = "DELETE FROM users WHERE id=%s"
        value = (self.__id,)
        cursor.execute(sql, value)
        # self.__id = -1
        return True

    def __repr__(self):
        return f'{self.user_id} {self.username} - {self.email}'

    def __str__(self):
        return  'User: {}, id: {}, email:{}'.\
            format(self.username, self.__id, self.email)


cnx, cursor = connect_to_db()

# new_user3 = User()
# # #new_user.username = 'grazyna'
# # # # new_user.email = "grazyna@mail.com"
# # # # new_user.set_password('haslo')
# # # # new_user.save_to_db(cursor)
# # new_user3.username = 'buu'
# # new_user3.email = "buuu@mail.com"
# # new_user3.set_password('buuu')
# # new_user3.save_to_db(cursor)
# # close_connection(cursor, cnx)
# # user_to_delete = User.load_by_user_id(cursor, 12)
# # print(user_to_delete)
# # user_to_delete.delete_user(cursor)
# all = User.load_all_users(cursor)
# print(all)
# # all = User.load_all_users(cursor)
# # print(all)
# # new_user3.delete_user(cursor, 2)
# close_connection(cursor, cnx)
