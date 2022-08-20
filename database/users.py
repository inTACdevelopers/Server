from config import *

import asyncio
import asyncpg


class User:
    def __init__(self):
        self.id = 0
        self.login = ""
        self.password = ""

    async def get_user(self):
        connection = await asyncpg.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME,
                                           ssl=False)

    # await connection.close()
