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


def make_post(title:str, desrc:str, contact:str, user:int, photo_bytes):
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


            hash = hashlib.sha256()
            hash.update(user.to_bytes(8,'big'))
            sha256 = hash.hexdigest()


            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO posts (title,description,seller_contact,from_user,file_path,creation_time) VALUES("
                    f"'{title}','{desrc}','{contact}',{user},'{server_file_title}','{str(datetime.datetime.today())}')--")

                cursor.execute(
                    f"INSERT INTO user_posts_{sha256} (title,description,seller_contact,from_user,file_path,creation_time) VALUES("
                    f"'{title}','{desrc}','{contact}',{user},'{server_file_title}','{str(datetime.datetime.today())}')--")

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


def get_posts_paginated(last_weight, limit, session_name):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        out_posts = []

        with conn.cursor() as cursor:

            cursor.execute(
                f"SELECT * FROM post_session_{session_name} WHERE weight < {last_weight} ORDER BY weight DESC LIMIT {limit}--")
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
        return 1
    except Exception as ex:
        print(ex)
        return 2

    finally:
        conn.close()


def get_users_posts_paginated(last_id,limin,sha_256_id):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        out_posts = []

        with conn.cursor() as cursor:

            cursor.execute(
                f"SELECT * FROM user_posts_{sha_256_id} WHERE id > {last_id} ORDER BY weight DESC LIMIT {limit}--")
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
        conn.clos


# TODO
#  Сделай таблицу с лайками в нее после успешного лайка должен добавляться VALUES(like_id,user_id,post_id,seller_id)
#  Потом делай выборку, это будет надо для уведомлений о лайках и просмотра списка лайков
def likePost(post_id: int):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(f"UPDATE posts SET likes=likes + 1 WHERE id={post_id}--")

            conn.autocommit = False
            return 0

    except Exception as ex:
        print(f"{ex} in likePost")
        return 1
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
