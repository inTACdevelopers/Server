from server import serve
from database.users import *
import asyncio

if __name__ == "__main__":
    #print(get_user_by_login_password("89020930883", "pass").user_type)
    serve()

# Перенеси файлы .proto в андройд студию, перекомпиль проект и потом проверяй
