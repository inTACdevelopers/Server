from config import *

import psycopg2
import psycopg2.errors as exeptions


class User:
    def __init__(self, name, password):
        self.id = 0
        self.login = name
        self.password = password

    def get_user(self):
        try:

            conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM users WHERE login='{self.login}'")

                user_data = cursor.fetchone()
                if user_data is not None:
                    return User(user_data[1], user_data[2])
                else:
                    return None
        except Exception as ex:
            print("There was some errors while working with database")
            print(ex)
        finally:
            conn.close()

    def new_user(self):

        try:
            conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

            conn.autocommit = True
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO users (login,password) VALUES('{self.login}','{self.password}')")
                    return "OK"
            except exeptions.UniqueViolation:
                return "User with such login already exists"
            conn.autocommit = False
        except Exception as ex:
            print("There was some errors while working with database")
            print(ex)
        finally:
            conn.close()
