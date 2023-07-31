# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def add_announce_category():
    button1 = InlineKeyboardButton("Phones", callback_data="willhaben_add:phones")
    button2 = InlineKeyboardButton("Laptops", callback_data="willhaben_add:laptops")
    button3 = InlineKeyboardButton("GPUs", callback_data="willhaben_add:gpus")

    search_choose_category = InlineKeyboardMarkup()
    search_choose_category.add(button1)
    search_choose_category.add(button2)
    search_choose_category.add(button3)
    
    return search_choose_category

def add_announce_laptops():
    buttons = []
    buttons.append(InlineKeyboardButton("Acer", callback_data="willhaben_laptop:acer"))
    buttons.append(InlineKeyboardButton("Apple", callback_data="willhaben_laptop:apple"))
    buttons.append(InlineKeyboardButton("ASUS", callback_data="willhaben_laptop:asus"))
    buttons.append(InlineKeyboardButton("Dell", callback_data="willhaben_laptop:dell"))
    buttons.append(InlineKeyboardButton("Fujitsu", callback_data="willhaben_laptop:fujitsu"))
    buttons.append(InlineKeyboardButton("HP", callback_data="willhaben_laptop:hp"))
    buttons.append(InlineKeyboardButton("Huawei", callback_data="willhaben_laptop:huawei"))
    buttons.append(InlineKeyboardButton("Lenovo", callback_data="willhaben_laptop:lenovo"))
    buttons.append(InlineKeyboardButton("Microsoft", callback_data="willhaben_laptop:microsoft"))
    buttons.append(InlineKeyboardButton("Samsung", callback_data="willhaben_laptop:samsung"))
    buttons.append(InlineKeyboardButton("Sony", callback_data="willhaben_laptop:sony"))

    keyboard = InlineKeyboardMarkup()
    for i in buttons:
        keyboard.add(i)
    
    return keyboard

def add_announce_inches():
    buttons = []
    buttons.append(InlineKeyboardButton('< 11"', callback_data="willhaben_laptop_inch:less11inches"))
    buttons.append(InlineKeyboardButton('12-12,9"', callback_data="willhaben_laptop_inch:12inches"))
    buttons.append(InlineKeyboardButton('13-13,9"', callback_data="willhaben_laptop_inch:13inches"))
    buttons.append(InlineKeyboardButton('14-14,9"', callback_data="willhaben_laptop_inch:14inches"))
    buttons.append(InlineKeyboardButton('15-15,9"', callback_data="willhaben_laptop_inch:15inches"))
    buttons.append(InlineKeyboardButton('16-16,9"', callback_data="willhaben_laptop_inch:16inches"))
    buttons.append(InlineKeyboardButton('17-17,9"', callback_data="willhaben_laptop_inch:17inches"))
    buttons.append(InlineKeyboardButton('> 18"', callback_data="willhaben_laptop_inch:more18inches"))

    keyboard = InlineKeyboardMarkup()
    for i in buttons:
        keyboard.add(i)
    
    return keyboard


def add_announce_phone_brand():
    buttons = []
    buttons.append(InlineKeyboardButton('Alcatel', callback_data="willhaben_phone:alcatel"))
    buttons.append(InlineKeyboardButton('Apple', callback_data="willhaben_phone:apple"))
    buttons.append(InlineKeyboardButton('Huawei', callback_data="willhaben_phone:huawei"))
    buttons.append(InlineKeyboardButton('Motorola', callback_data="willhaben_phone:motorola"))
    buttons.append(InlineKeyboardButton('Nokia', callback_data="willhaben_phone:nokia"))
    buttons.append(InlineKeyboardButton('OnePlus', callback_data="willhaben_phone:oneplus"))
    buttons.append(InlineKeyboardButton('Samsung', callback_data="willhaben_phone:samsung"))
    buttons.append(InlineKeyboardButton('Sony', callback_data="willhaben_phone:sony"))
    buttons.append(InlineKeyboardButton('Xiaomi', callback_data="willhaben_phone:xiaomi"))
    buttons.append(InlineKeyboardButton('Other', callback_data="willhaben_phone:other"))

    keyboard = InlineKeyboardMarkup()
    for i in buttons:
        keyboard.add(i)
    
    return keyboard

def add_announce_phone_gbs():
    buttons = []
    buttons.append(InlineKeyboardButton('> 512 GB', callback_data="willhaben_phone_gbs:more512gb"))
    buttons.append(InlineKeyboardButton('256 GB', callback_data="willhaben_phone_gbs:256gb"))
    buttons.append(InlineKeyboardButton('128 GB', callback_data="willhaben_phone_gbs:128gb"))
    buttons.append(InlineKeyboardButton('64 GB', callback_data="willhaben_phone_gbs:64gb"))
    buttons.append(InlineKeyboardButton('32 GB', callback_data="willhaben_phone_gbs:32gb"))
    buttons.append(InlineKeyboardButton('16 GB', callback_data="willhaben_phone_gbs:16gb"))
    buttons.append(InlineKeyboardButton('< 8 GB', callback_data="willhaben_phone_gbs:less8gb"))

    keyboard = InlineKeyboardMarkup()
    for i in buttons:
        keyboard.add(i)
    
    return keyboard

def add_announce_phone_unblocked():
    buttons = []
    buttons.append(InlineKeyboardButton('Blocked', callback_data="willhaben_phone_unblocked:no"))
    buttons.append(InlineKeyboardButton('Unblocked', callback_data="willhaben_phone_unblocked:yes"))

    keyboard = InlineKeyboardMarkup()
    for i in buttons:
        keyboard.add(i)
    
    return keyboard