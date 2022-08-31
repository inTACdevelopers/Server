import datetime
import os.path

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


def make_post(title, desrc, contact, user, photo_bytes, file_name):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

        server_file_title = str(hash(file_name + str(datetime.datetime.today()))) + ".JPEG"

        conn.autocommit = True

        dir = PHOTO_DIR
        if DEBAG:
            dir = DEBAG_PHOTO_DIR

        if not os.path.exists(dir + server_file_title):

            with open(dir + server_file_title, "wb") as file:
                file.write(photo_bytes)

            server_file_title = dir + server_file_title

            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO posts (title,description,seller_contact,from_user,file_path,creation_time) VALUES("
                    f"'{title}','{desrc}','{contact}',{user},'{server_file_title}','{str(datetime.datetime.today())}')")

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
            cursor.execute(f"SELECT * FROM posts WHERE id={post_id}")
            post_data = cursor.fetchone()
            path = post_data[5]

            path = path.replace('/home/ivan', os.getcwd())

            if path is not None:
                with open(path, "rb") as file:
                    return Post(id=post_id, title=post_data[1], descr=post_data[2], contact=post_data[3],
                                user=post_data[4], bytes=file.read(), time=post_data[6])

    except Exception as ex:
        print(ex)
        return None

    finally:
        conn.close()


def get_posts_paginated(curr_id, limint):
    try:
        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        out_posts = []

        with conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM posts WHERE id >= {curr_id} LIMIT {limint}")
            posts_data = cursor.fetchall()

            if posts_data == []:
                raise EmptyScrollExeption()

            for item in posts_data:
                path = item[5]

                path = path.replace('/home/ivan', os.getcwd())

                with open(path, "rb") as file:
                    post = Post(id=item[0], title=item[1], descr=item[2], contact=item[3],
                                user=item[4], bytes=file.read(), time=item[6])
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


def get_first_post_id():
    try:

        conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM posts LIMIT 1")
            return int(cursor.fetchone()[0])
    except Exception as ex:
        print(ex)
        return None
    finally:
        conn.close()



