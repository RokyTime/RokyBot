from aiogram.utils import executor

from create_bot import dp, bot

from handlers import users_requests
from users_database.db_requests import db_connect


async def on_startup(_):
    print('Bot online.')
    await db_connect()
   

users_requests.register_Roky_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)