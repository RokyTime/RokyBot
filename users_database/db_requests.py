import sqlite3 as sq

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
