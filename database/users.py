from config import *

import psycopg2
import psycopg2.errors as exceptions
from exeptions import *


# its a dataclass... shit
# i need class methods...
class User:
    def __init__(self, login, password, surname, name, company, birth):
        self.id = 0
        self.login = login
        self.password = password
        self.surname = surname
        self.name = name
        self.company = company
        self.user_type = 0
        self.birth_date = birth


def get_user(login):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE login='{login}' LIMIT 1--")

            user_data = cursor.fetchone()
            if user_data is not None:
                user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                user.id = user_data[0]
                return user
            else:
                return None
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
    finally:
        conn.close()


def get_user_by_login_password(login, password):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{password}'--")

            user_data = cursor.fetchone()

            if user_data is not None:
                user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                user.id = user_data[0]
                return user
            else:
                return None
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
    finally:
        conn.close()


def get_user_by_token(token: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE token = '{token}'--")

            user_data = cursor.fetchone()

            if user_data is not None:
                user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                user.id = user_data[0]
                return user
            else:
                return None
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
    finally:
        conn.close()


def check_company_exist(company):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:

            if company == None or company == '':
                return False
            cursor.execute(f"SELECT * FROM users WHERE company='{company}'--")

            return cursor.fetchone() is not None

    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
    finally:
        conn.close()


def new_user(login, password, name, surname, birth, token, company=None):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        try:
            with conn.cursor() as cursor:
                if check_company_exist(company):
                    raise CompanyExistException(company)
                cursor.execute(
                    f"INSERT INTO users (login,password,surname,name,company,birth_date,token) VALUES('{login}','{password}',"
                    f"'{surname}','{name}','{company}','{birth}','{token}')--")
                return 0  # OK
        except exceptions.UniqueViolation:
            return 1  # User already exist
        except CompanyExistException as ex:
            return 2  # Company already exist
        conn.autocommit = False
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return 3  # Error with database
    finally:
        conn.close()


def create_user_post_session(session_name):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"CREATE TABLE post_session_{session_name} "
                           f"AS SELECT * FROM posts ORDER BY weight DESC LIMIT 500--")
        conn.autocommit = False
        return 0
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def drop_user_post_session(session_name):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"DROP TABLE post_session_{session_name}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def create_users_posts_table(sha256_user_id):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"CREATE TABLE user_posts_{sha256_user_id} AS (SELECT * FROM posts) with no data--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()
