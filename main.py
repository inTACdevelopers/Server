from database.posts import remove_all
from database.users import create_user_post_session, drop_user_post_session
from server import serve
from parser import *
import hashlib
from services.YmlParser.parser import *

if __name__ == "__main__":
    a = b"1234"
    print(str(hashlib.sha512(a)))
    # remove_all()
    # serve()
