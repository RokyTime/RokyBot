import sqlite3 as sq
from aiogram import types
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def db_connect():
    global base, cur
    base = sq.Connection('Users.db')
    cur = base.cursor()
    if base:
        print('База данных подключена.')

async def bd_add(data):
    global base, cur
    print(data)
    base.execute('CREATE TABLE IF NOT EXISTS __{}(Понедельник, Вторник, Среда, Четверг, \
        Пятница, Суббота, Воскресенье)'.format(data['Bot user']))
    base.commit()
    #cur.execute("INSERT INTO __{d1}({d2}) VALUES(?)".format(d1=data['Bot user'], \
        #d2=data['day of the week']), data['Todo'])
    cur.execute("INSERT INTO __{}({}) VALUES(?)".format(data['Bot user'], data['day of the week']), (data['Todo'], ))
    base.commit()
    print(await sql_read(data['Bot user']))



async def sql_read(user):
    global base, cur
    print (cur.execute('SELECT * FROM __{}'.format(user)).fetchall())
    pon = ''
    vtor = ''
    sred = ''
    chet = ''
    pt = ''
    sb = ''
    vs = ''
    for i in cur.execute('SELECT * FROM __{}'.format(user)).fetchall():
        if i[0] != None:
            pon += i[0]+"\n"
        if i[1] != None:
            vtor += i[1]+"\n"
        if i[2] != None:
            sred += i[2]+"\n"
        if i[3] != None:
            chet += i[3]+"\n"
        if i[4] != None:
            pt += i[4]+"\n"
        if i[5] != None:
            sb += i[5]+"\n"
        if i[6] != None:
            vs += i[6]+"\n"
    #return (pon, vtor, sred, chet, pt, sb, vs)
    return f'Список на понедельник: {pon}\nСписок на вторник: {vtor}\nСписок на среду: {sred}\nСписок на четверг: {chet}\n\
Список на пятницу: {pt}\nСписок на субботу: {sb}\nСписок на воскресенье: {vs}'


async def sql_read2(callback : types.CallbackQuery, day, day2):
    global cur, base
    for i in cur.execute('SELECT * FROM __{}'.format(callback.from_user.id)).fetchall():
        if i[day-1] != None:
            await bot.send_message(callback.from_user.id, text='ᐁᐁᐁ', reply_markup=InlineKeyboardMarkup()\
                .add(InlineKeyboardButton(text=f"Удалить {i[day-1]}", callback_data=f"delete_ {i[day-1]} {day} {day2}")))



async def sql_delete_f(callback : types.CallbackQuery, req):
    global cur, base
    cur.execute("DELETE FROM __{} WHERE {} = ?".format(callback.from_user.id, req[2]), (req[0], ))
    base.commit()

