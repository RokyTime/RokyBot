from create_bot import bot
from datetime import datetime as dt
import asyncio
import config
import datetime
import random
from request import rate, weather

stickers=['CAACAgIAAxkBAAEHeadj1CqOXs2Wf7Y_yJJELsZRNt9j9AACiRYAAsfqwEqfTbQfquYe0i0E',
    'CAACAgIAAxkBAAEHealj1CsQUMUxXkZBV0kHLn8Yq-Ds0gACjA0AAqKEiUhTpgS0QAL2iy0E',
    'CAACAgEAAxkBAAEHeatj1CsxA5Q8PMAmalJq93DoH8zuMQACUwEAAml6MQW6hVyZUojP4y0E',
    'CAACAgIAAxkBAAEHea1j1CtJH8Tq0okgJBdEHUHYyPWyzwACrxYAAuWS2Uoi_Y50nFSDpi0E',
    'CAACAgIAAxkBAAEHea9j1CtfoQulVkFafUH-xUJBk5whUAAChhIAAhVbcUnkPBotqKzxly0E',
    'CAACAgIAAxkBAAEHebFj1Ct0dp_U2mP4QYpeeLqJ5-IaYAACtBUAAvyiSUjmLfpo7N1fMi0E',
    'CAACAgUAAxkBAAEHebNj1Ct-7ugO6Vaiw93_TDaW7DhwVwACnAADFbnXJOT0gQHNedUKLQQ',
    'CAACAgIAAxkBAAEHebVj1CuJY_rh9rQ_DXX9G4vKV4TK_QAClyEAArLcQEr6mbBz1F797C0E',
    'CAACAgIAAxkBAAEHebdj1CuYbzSNQ7c6-giKZ4hE4FwxzwACAhsAAqOLGEtxqbC_159d5S0E',
    'CAACAgIAAxkBAAEHebxj1Cu_PzNc_QV7u_V7AAHYlPAHTggAAskVAAKT2TBLYOx2aJt_ZIYtBA',
    'CAACAgIAAxkBAAEHecBj1CvQXz4Yom-XAAEaQp04mtAo5_EAAg0GAALSWogBef8AAdOuIoKJLQQ',
    'CAACAgIAAxkBAAEHecJj1CvlfmcnupqSKK7JRPNu0AiY2QACIQAD_2gqO1SDz_zBchjwLQQ',
    'CAACAgIAAxkBAAEHecRj1Cvu--f4qRTVd195UiocsUb9mgACuiwAAuCjggcMXhhpMbDivi0E'
]

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
    return await task_timer(hours, minuts)

