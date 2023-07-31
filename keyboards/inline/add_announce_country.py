# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def add_announce_country():
    button1 = InlineKeyboardButton("Ukraine", callback_data="willhaben_add_country:ukraine")
    button2 = InlineKeyboardButton("Czech", callback_data="willhaben_add_country:czech")
    button3 = InlineKeyboardButton("Poland", callback_data="willhaben_add_country:poland")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    
    return keyboard