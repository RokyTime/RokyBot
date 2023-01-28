from aiogram.utils import executor

from create_bot import dp, bot

from handlers import Roky



async def on_startup(_):
    print('Bot online.')
   

Roky.register_Roky_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)