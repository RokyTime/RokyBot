from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
b1 = KeyboardButton('Инфа')
b2 = KeyboardButton('Анекдот')

kb_mane = ReplyKeyboardMarkup(resize_keyboard=True)

kb_mane.add(b1).add(b2)