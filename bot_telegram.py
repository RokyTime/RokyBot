from aiogram.utils import executor

from create_bot import dp, bot

from handlers import Roky

from date_time import alarm

import asyncio


async def on_startup(_):
    print('Bot online.')
    t = await alarm.get_time()
    await alarm.task_timer(hours=int(t[0]), minuts=int(t[1]))


Roky.register_Roky_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)