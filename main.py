from database.posts import get_posts_paginated, test
from server import serve
from parser import *

from services.YmlParser.parser import *

if __name__ == "__main__":

    #print(get_posts_paginated(2,5))
    serve()
