import datetime

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
        self.about = ''


def get_user_id(user_id: int) -> User:
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE id={user_id} LIMIT 1--")

            user_data = cursor.fetchone()
            if user_data is not None:
                user = User(user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
                user.id = user_data[0]
                user.about = user_data[9]
                return user
            else:
                return None
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return None
    finally:
        conn.close()


def get_user(login) -> User:
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
                           f"AS SELECT * FROM posts ORDER BY weight DESC LIMIT 500 --")
            cursor.execute(f"ALTER TABLE post_session_{session_name} ADD COLUMN position serial --")
        conn.autocommit = False
        return 0
    except Exception as ex:
        print("There was some errors while working with database")

        drop_user_post_session(session_name)
        create_user_post_session(session_name)

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


def get_count_of_user_posts(sha256_user_id):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        count = -1
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM user_posts_{sha256_user_id}--")
            count = int(cursor.fetchone()[0])

        conn.autocommit = False
        return count
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return -1  # Error with database
    finally:
        conn.close()


def create_users_posts_table(sha256_user_id):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"CREATE TABLE user_posts_{sha256_user_id} AS (SELECT * FROM posts) with no data--")

            cursor.execute(f"CREATE SEQUENCE id_seq_user_posts_{sha256_user_id} "
                           f"AS BIGINT "
                           f"INCREMENT 1 "
                           f"MINVALUE 1 "
                           f"START  1 "
                           f"OWNED BY user_posts_{sha256_user_id}.id --")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("There was some errors while working with database")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_photo(user_id: int, photo_bytes) -> int:
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        path = server_file_title = str(hash(str(datetime.datetime.today()))) + ".JPEG"
        dir = PROFILE_PHOTO_DIR
        if DEBAG:
            dir = DEBAG_PROFILE_PHOTO_DIR
        if not os.path.exists(dir + server_file_title):
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE users SET profile_photo={path} WHERE id={user_id}--")

            with open(dir + server_file_title, "wb") as file:
                file.write(photo_bytes)
            conn.autocommit = False
            return 0
        else:
            return 1


    except Exception as ex:
        print("DataBase Error in update_user_photo")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_about(user_id: int, about: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET about={about} WHERE id={user_id}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("DataBase Error in update_user_about")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_name(user_id: int, name: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET name={name} WHERE id={user_id}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("DataBase Error in update_user_about")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_login(user_id: int, login: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET login={login} WHERE id={user_id}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("DataBase Error in update_user_about")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_password(user_id: int, password: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET password={password} WHERE id={user_id}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("DataBase Error in update_user_about")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def update_user_sur_name(user_id: int, surname: str):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE users SET surname={surname} WHERE id={user_id}--")

        conn.autocommit = False
        return 0
    except Exception as ex:
        print("DataBase Error in update_user_about")
        print(ex)
        return 1  # Error with database
    finally:
        conn.close()


def get_user_photo(user_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT profile_photo FROM users WHERE id={user_id}--")
            path = cursor.fetchone()
            if path is not None:
                with open(path, "rb") as file:
                    return file.read()

        return 0
    except Exception as ex:
        print("DataBase Error in get_user_photo")
        print(ex)
        return 1  # Error with database
    finally:
        conn.autocommit = False
        conn.close()
