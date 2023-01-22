import datetime
import hashlib
import os.path
import time

from config import *

import psycopg2
import psycopg2.errors as exceptions
from exeptions import *


class Post():
    def __init__(self, id, title, descr, contact, user, time, bytes):
        self.id = id
        self.title = title
        self.descr = descr
        self.seller_contact = contact
        self.from_user = user
        self.file_path = ""
        self.creation_date = time
        self.photo_bytes = bytes
        self.likes = 0
        self.weight = 0
        self.like = 0

    def weight_function(self):
        self.weight = self.likes


def make_post(title: str, desrc: str, contact: str, user: int, photo_bytes):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        server_file_title = str(hash("file_name" + str(datetime.datetime.today()))) + ".JPEG"

        conn.autocommit = True

        dir = PHOTO_DIR
        if DEBAG:
            dir = DEBAG_PHOTO_DIR

        if not os.path.exists(dir + server_file_title):

            with open(dir + server_file_title, "wb") as file:
                file.write(photo_bytes)

            server_file_title = dir + server_file_title

            _hash = hashlib.sha256()
            _hash.update(user.to_bytes(8, 'big'))
            sha256 = _hash.hexdigest()

            with conn.cursor() as cursor:
                # Запрос на вставку поста
                cursor.execute(
                    "INSERT INTO posts (title,description,seller_contact,from_user,file_path,creation_time) VALUES("
                    f"'{title}','{desrc}','{contact}',{user},'{server_file_title}','{str(datetime.datetime.today())}')--")

                # Запрос на обновление последовательности постов юзера
                cursor.execute(f"SELECT nextval('id_seq_user_posts_{sha256}');--")
                post_id = cursor.fetchone()

                # Запрос на вставку поста в табличку с постами пользователя

                cursor.execute(
                    f"INSERT INTO user_posts_{sha256} (id,title,description,seller_contact,from_user,file_path,"
                    f"creation_time) VALUES("
                    f"{post_id[0]},'{title}','{desrc}','{contact}',{user},'{server_file_title}','{str(datetime.datetime.today())}')--")

                # Запрос на получение id последнего созданого поста
                cursor.execute(f"SELECT currval('posts_id_seq');--")
                last_created_post_id = int(cursor.fetchone()[0])
                print(last_created_post_id)

                # билдим хэш из последнего id-шника
                _hash = hashlib.sha256()
                _hash.update(last_created_post_id.to_bytes(8, 'big'))
                post_hash_id = _hash.hexdigest()

                # Запрос на создание таблицы с лайками для данного поста
                cursor.execute(f'CREATE TABLE post_likes_{post_hash_id} ('
                               f'user_id BIGINT PRIMARY KEY'
                               f');--')
                conn.autocommit = False
                return 0
        else:
            return 1

    except Exception as ex:

        print(ex)
        return 2
    finally:
        conn.close()


def get_post(post_id):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM posts WHERE id={post_id}--")
            post_data = cursor.fetchone()
            path = post_data[5]

            if path is not None:
                with open(path, "rb") as file:
                    return Post(id=post_id, title=post_data[1], descr=post_data[2], contact=post_data[3],
                                user=post_data[4], bytes=file.read(), time=post_data[6])

    except Exception as ex:
        print(ex)
        return None

    finally:
        conn.close()


def get_posts_paginated(last_id: int, limit: int, session_name: str, user_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        out_posts = []

        with conn.cursor() as cursor:

            cursor.execute(
                f"SELECT * FROM post_session_{session_name} WHERE position > {last_id} LIMIT {limit}--")
            posts_data = cursor.fetchall()

            if posts_data == []:
                raise EmptyScrollExeption()

            for item in posts_data:
                path = item[5]

                if DEBAG:
                    path = path.replace('/home/ivan/database/photos/', DEBAG_PHOTO_DIR)

                with open(path, "rb") as file:
                    post = Post(id=item[0], title=item[1], descr=item[2], contact=item[3],
                                user=item[4], bytes=file.read(), time=item[6])
                    post.like = is_user_liked_post(user_id=user_id, post_id=post.id)
                    post.weight = item[8]
                    out_posts.append(post)
        return out_posts

    except EmptyScrollExeption as ex:
        print(ex)
        return 1
    except Exception as ex:
        print(ex)
        return 2

    finally:
        conn.close()


def get_users_posts_paginated(last_id, limit, token):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        out_posts = []

        with conn.cursor() as cursor:

            cursor.execute(
                f"SELECT * FROM user_posts_{token} WHERE id > {last_id} ORDER BY weight DESC LIMIT {limit}--")
            posts_data = cursor.fetchall()

            if posts_data == []:
                raise EmptyScrollExeption()

            for item in posts_data:
                path = item[5]

                if DEBAG:
                    path = path.replace('/home/ivan/database/photos/', DEBAG_PHOTO_DIR)

                with open(path, "rb") as file:
                    post = Post(id=item[0], title=item[1], descr=item[2], contact=item[3],
                                user=item[4], bytes=file.read(), time=item[6])
                    post.weight = item[8]
                    out_posts.append(post)
        return out_posts

    except EmptyScrollExeption as ex:
        print(ex)
    finally:
        conn.close()


def get_first_post(session_name):
    try:

        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM post_session_{session_name} ORDER BY weight DESC LIMIT 1--")
            data = cursor.fetchone()

            return data
    except Exception as ex:
        print(ex)
        return None
    finally:
        conn.close()


def likePost(post_id: int, user_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE posts SET likes=likes + 1 WHERE id={post_id}--")

            _hash = hashlib.sha256()
            _hash.update(post_id.to_bytes(8, 'big'))
            post_hash_id = _hash.hexdigest()

            cursor.execute(f"INSERT INTO post_likes_{post_hash_id} VALUES({user_id})--")

            conn.autocommit = False
            return 0

    except Exception as ex:
        print(f"{ex} in likePost")
        return 1
    finally:
        conn.close()


def un_likePost(post_id: int, user_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:

            cursor.execute(f"UPDATE posts SET likes=likes - 1 WHERE id={post_id}--")

            _hash = hashlib.sha256()
            _hash.update(post_id.to_bytes(8, 'big'))
            post_hash_id = _hash.hexdigest()

            cursor.execute(f"DELETE FROM post_likes_{post_hash_id} WHERE user_id = {user_id}--")

            conn.autocommit = False
            return 0

    except Exception as ex:
        print(f"{ex} in likePost")
        return 1
    finally:
        conn.close()


def is_user_liked_post(user_id: int, post_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:

            _hash = hashlib.sha256()
            _hash.update(post_id.to_bytes(8, 'big'))
            post_hash_id = _hash.hexdigest()

            cursor.execute(f"SELECT * FROM post_likes_{post_hash_id} WHERE user_id = {user_id}--")
            if cursor.fetchone() == None:
                return 0
            conn.autocommit = False
            return 1

    except Exception as ex:
        print(f"{ex} in is_user_liked_post")
        return 1
    finally:
        conn.close()


def get_weight_params(post_id: int) -> []:
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM posts WHERE id={post_id}--")
            post_data = cursor.fetchone()

            params = [post_data[-2]]
            conn.autocommit = False
            return params

    except Exception as ex:
        print(f"{ex} in get_weight_params")
        return None
    finally:
        conn.close()


def calculate_weight(post_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        params = get_weight_params(post_id)

        count_of_likes = params[0]
        new_weight = count_of_likes

        if params != None and params != []:

            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE posts SET weight={new_weight} WHERE id={post_id}--")

                conn.autocommit = False
                return 0
        else:
            print(f"Error in calculate_weight 'EMPTY LIST'")
            return 1

    except Exception as ex:
        print(f"{ex} in calculate_weight")
        return 2
    finally:
        conn.close()


def remove_all():
    try:

        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM posts WHERE id > 0--")
            cursor.execute("ALTER SEQUENCE posts_id_seq RESTART WITH 1--")
            print(cursor.fetchone())
        conn.autocommit = False
    except Exception as ex:
        print(ex)

    finally:
        conn.close()
