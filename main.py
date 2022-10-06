
from database.users import create_user_post_session, drop_user_post_session
from server import serve
from parser import *

from services.YmlParser.parser import *

if __name__ == "__main__":

    serve()
