from database.posts import remove_all, get_first_post
from database.users import create_user_post_session, drop_user_post_session, create_users_posts_table
from server import serve
# from parser import *
import hashlib
from services.YmlParser.parser import *

if __name__ == "__main__":
    serve()
