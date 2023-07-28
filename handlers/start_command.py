from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    await dp.bot.send_message(message.chat.id, "Hello! It's bot that helps to get data from willhaben.at and bazos.cz. If you wanne try it out write him: @dobbikov")