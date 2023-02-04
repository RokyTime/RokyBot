import sqlite3 as sq

async def db_connect():
    global base, cur
    base = sq.Connection('Users.db')
    cur = base.cursor()
    if base:
        print('База данных подключена.')

async def bd_add(data):
    print(data)
    base.execute("CREATE TABLE IF NOT EXISTS '?'(Понедельник TEXT, Вторник TEXT, \
        Среда TEXT, Четверг TEXT, Пятница TEXT, Суббота TEXT, Воскресенье TEXT)", (str(data['Bot user']), ))
    base.commit()
    cur.execute(f"INSERT INTO {data['Bot user']}({data['day of the week']}) VALUES({data['Todo']})")
    base.commit()
