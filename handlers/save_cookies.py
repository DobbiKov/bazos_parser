from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, willhaben

@dp.message_handler(commands=['save_cookies'])
async def save_cookies_command(message: types.Message, state: FSMContext):
    willhaben.browser_save_cookies()
    await dp.bot.send_message(message.chat.id, "The cookies have been saved!")