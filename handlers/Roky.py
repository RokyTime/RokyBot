from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import bot
import requests

import datetime
import random
from keyboards import kb_mane

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

async def start_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Салам', reply_markup=kb_mane)


async def get_info(message : types.Message):
    global stickers
    if message.text != 'Инфа':
        return
    await bot.send_message(message.from_user.id, str(datetime.datetime.today()))
    await bot.send_sticker(chat_id=message.from_user.id, sticker=random.choice(stickers))
    city_id = 486071
    appid = "ae8f8b7ed81c5375a2d7ef07a966169a"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        await bot.send_message(message.from_user.id, f'🌧️Погода:{data["weather"][0]["description"]},\n\
        🌡️Температура:{data["main"]["temp"]},\n\
        🌡️Минимальная температура:{data["main"]["temp_min"]},\n\
        🌡️Максимальная температура:{data["main"]["temp_max"]}')
    except Exception as e:
        bot.send_message(message.from_user.id , f'Exception (weather):{e}')


    





def register_Roky_handler(dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_info)
    