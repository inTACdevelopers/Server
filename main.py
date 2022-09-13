import urllib
from io import BytesIO

from services.YmlParser.parser import *
from server import serve
from database.posts import *

if __name__ == "__main__":
    serve()
