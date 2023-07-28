# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def search_choose_category():
    button1 = InlineKeyboardButton("Phones", callback_data="willhaben:phones")
    button2 = InlineKeyboardButton("Laptops", callback_data="willhaben:laptops")
    button3 = InlineKeyboardButton("GPUs", callback_data="willhaben:gpus")

    search_choose_category = InlineKeyboardMarkup()
    search_choose_category.add(button1)
    search_choose_category.add(button2)
    search_choose_category.add(button3)
    
    return search_choose_category