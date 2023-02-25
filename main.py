from database.posts import remove_all, get_first_post, calculate_weight, get_posts_paginated, is_user_liked_post, \
    remove_all_post_likes_tables
from database.users import create_user_post_session, drop_user_post_session, create_users_posts_table
from server import serve
# from parser import *
import hashlib
from services.YmlParser.parser import *

if __name__ == "__main__":
    #remove_all_post_likes_tables()
    serve()
