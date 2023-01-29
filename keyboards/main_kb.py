from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
b1 = KeyboardButton('Инфа')
b2 = KeyboardButton('Анекдот')

kb_mane = ReplyKeyboardMarkup(resize_keyboard=True)

kb_mane.row(b1, b2)