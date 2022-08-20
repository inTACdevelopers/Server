from server import serve
from database.users import User
import asyncio


async def test():
    user = User()
    await user.get_user()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())

    # serve()
