from aiogram import types
from aiogram.dispatcher import Dispatcher
from create_bot import bot

from date_time import alarm
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import config
import datetime
import random
from keyboards import kb_mane
from request import api_parse, parse
from aiogram.dispatcher.filters import Text
from users_database.db_requests import bd_add, sql_read, sql_read2, sql_delete_f

async def set_timer():
    t = await alarm.get_time()
    await alarm.task_timer(hours=int(t[0]), minuts=int(t[1]))


async def get_message(message):
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
    if message.from_user.id in config.admin_ID:
        await message.delete()
        await bot.send_message(message.from_user.id, str(datetime.datetime.today()))
        await bot.send_sticker(message.from_user.id, random.choice(stickers))
        await bot.send_message(message.from_user.id, await parse.get_rate())
        await bot.send_message(message.from_user.id, await api_parse.get_weather(), reply_markup=kb_mane)
        
    else:
        await message.delete()
        await bot.send_message(message.from_user.id, '?? ???????? ???? ????????.')
        






async def start_command(message : types.Message):
    await bot.send_message(message.from_user.id, '????', reply_markup=kb_mane)
    await message.delete()
    await set_timer()

async def get_info(message : types.Message):
    await get_message(message)
    await set_timer()
    


async def anek_handler(message : types.Message):
    if message.from_user.id in config.admin_ID:
        await message.delete()
        await bot.send_message(message.from_user.id, await parse.get_anekdot(), reply_markup=kb_mane)
        await set_timer()


async def db_handler(message : types.Message):
    if message.from_user.id not in config.admin_ID:
        return
    await bot.send_message(message.from_user.id, '?????????????? ???????? ????????????????????, ?????????????????? ???????????? ??????????????????????',\
         reply_markup=InlineKeyboardMarkup()\
            .add(InlineKeyboardButton(text='??????????????????????', callback_data='data_ ??????????????????????'))\
            .add(InlineKeyboardButton(text='??????????????', callback_data='data_ ??????????????'))\
                .add(InlineKeyboardButton(text='??????????', callback_data='data_ ??????????'))\
                .add(InlineKeyboardButton(text='??????????????', callback_data='data_ ??????????????'))\
                    .add(InlineKeyboardButton(text='??????????????', callback_data='data_ ??????????????'))\
                    .add(InlineKeyboardButton(text='??????????????', callback_data='data_ ??????????????'))\
                        .add(InlineKeyboardButton(text='??????????????????????', callback_data='data_ ??????????????????????')))



async def db_callback(callback : types.CallbackQuery):
    await bot.send_message(callback.from_user.id, f'???????????????????? ???? {callback.data.replace("data_ ", "")}\
        \n???????????? ?????????? ?????????? ?????? ?????????? ???? ?????? ???????????????????????? ?????? ????????????????.',\
         reply_markup=InlineKeyboardMarkup()\
            .add(InlineKeyboardButton(text='???????????????? ??????????.', callback_data=f'data__ 1 {callback.data.replace("data_ ", "")}')))
    ind = 0
    if callback.data.replace("data_ ", "") == '??????????????????????':
        ind = 1
    if callback.data.replace("data_ ", "") == '??????????????':
        ind = 2
    if callback.data.replace("data_ ", "") == '??????????':
        ind = 3
    if callback.data.replace("data_ ", "") == '??????????????':
        ind = 4
    if callback.data.replace("data_ ", "") == '??????????????':
        ind = 5
    if callback.data.replace("data_ ", "") == '??????????????':
        ind = 6
    if callback.data.replace("data_ ", "") == '??????????????????????':
        ind = 7
    await sql_read2(callback, ind, callback.data.replace("data_ ", ""))


async def get_todo(message : types.Message):
    bot.send_message(message.from_user.id, 'dsdsdsd')

class FSMUser(StatesGroup):
    todo = State()



async def toFSM(callback : types.CallbackQuery):
    global toFSMdata
    print(callback.data.replace('data__ ', ''))
    toFSMdata ={
    'Bot user' : callback.from_user.id, 
    'day of the week' : callback.data.replace('data__ ', '').split(' ')[1],
    'Number' : callback.data.replace('data__ ', '').split(' ')[0]
    }
    await FSMUser.todo.set()
    await callback.answer(text='?????????? ????????????')
    

async def todo_handler(message : types.Message, state : FSMContext):
    toFSMdata['Todo'] = message.text
    await bd_add(toFSMdata)
    await state.finish()


async def sql_callback_handler(callback : types.CallbackQuery):
    req = callback.data.replace("delete_ ", "").split(" ")
    print(req)
    await sql_delete_f(callback, req)
    await callback.answer('??????????????.', show_alert=True)

async def ras(message : types.Message):
    text = await sql_read(str(message.from_user.id))
    await bot.send_message(chat_id=message.from_user.id, text=text)


def register_Roky_handler(dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(get_info, lambda message : '????????' in message.text)
    dp.register_message_handler(anek_handler, lambda message : '??????????????' in message.text)
    dp.register_message_handler(db_handler, lambda message : '????????????????????' in message.text)
    dp.register_callback_query_handler(db_callback, Text(startswith='data_ '))

    dp.register_callback_query_handler(sql_callback_handler, Text(startswith='delete_ '))
    
    dp.register_message_handler(ras, lambda message : '????????????????????' in message.text)

    dp.register_callback_query_handler(toFSM, Text(startswith='data__ '), state=None)
    dp.register_message_handler(todo_handler, state=FSMUser.todo)
    