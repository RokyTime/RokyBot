from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import bot

from date_time import alarm
import asyncio


import config
import datetime
import random
from keyboards import kb_mane
from request import weather, rate, anekdot

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
    await bot.send_message(message.from_user.id, '🤨', reply_markup=kb_mane)
    await message.delete()
    t = await alarm.get_time()
    await alarm.task_timer(hours=int(t[0]), minuts=int(t[1]))

async def get_info(message : types.Message):
    global stickers
    if message.from_user.id in config.admin_ID:
        await bot.send_message(message.from_user.id, str(datetime.datetime.today()))
        await bot.send_sticker(message.from_user.id, random.choice(stickers))
        await bot.send_message(message.from_user.id, await rate.get_rate())
        await bot.send_message(message.from_user.id, await weather.get_weather(), reply_markup=kb_mane)
        await message.delete()
    else:
        await bot.send_message(message.from_user.id, 'Я тебя не знаю.')
        await message.delete()


async def anek_handler(message : types.Message):
    if message.from_user.id in config.admin_ID:
        await bot.send_message(message.from_user.id, await anekdot.get_anekdot(), reply_markup=kb_mane)
        await message.delete()

def register_Roky_handler(dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_info, lambda message : 'Инф' in message.text)
    dp.register_message_handler(anek_handler, lambda message : 'Анек' in message.text)
    