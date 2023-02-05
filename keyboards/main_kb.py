from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
b1 = KeyboardButton('Инфа')
b2 = KeyboardButton('Анекдот')
b3 = KeyboardButton('Добавить расписание')
b4 = KeyboardButton('Расписание')

kb_mane = ReplyKeyboardMarkup(resize_keyboard=True)

kb_mane.row(b1, b2).row(b3, b4)