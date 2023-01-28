from create_bot import bot
from datetime import datetime as dt
import asyncio
import config
import datetime
import random
from request import rate, weather

async def get_time():
    time_h = int(dt.today().strftime('%H'))
    time_m = int(dt.today().strftime('%M'))
    hours = 24-time_h+5
    mins = int(60-time_m)
    if time_m not in [0, 00]:
        res = f'{hours-1},{mins}'
    else:
        res = hours
        
    return ((res.split(',')[0]), (res.split(',')[1]))


async def task_timer(hours, minuts):
    t = (hours*60*60)+(minuts*60)
    print(f'Таймер сработает через {t} секунд')
    print('Если ты это читаешь, то асинхронность работает')
    await asyncio.sleep(t)
    for admin in config.admin_ID:
        await bot.send_message(admin, str(datetime.datetime.today()))
        await bot.send_sticker(admin, random.choice(stickers))
        await bot.send_message(admin, await rate.get_rate())
        await bot.send_message(admin, await weather.get_weather())


