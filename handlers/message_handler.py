from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.search_choose_category import search_choose_category

from loader import dp, browser
from modules.announce import Announce
from modules.willhaben import Willhaben
from modules.bazos import parse_search_site

@dp.message_handler(state="*")
async def message_handler(message: types.Message, state: FSMContext):
    if message.text.startswith("https://"):
        try:
            willhaben = Willhaben(browser)
            link = message.text
            announces: list[Announce] = []

            if "bazos" in message.text:
                await dp.bot.send_message(message.chat.id, f"The process of parsing has been started. Please, wait.")
                announces = parse_search_site(link)
            elif "willhaben" in message.text:
                await dp.bot.send_message(message.chat.id, f"The process of parsing has been started. Please, wait.")
                announces = willhaben.parse_link(link)

            if len(announces) == 0:
                await dp.bot.send_message(call.message.chat.id, "No results :(")
                return
            for i in announces:
                await i.send_announce_to_chat(dp.bot, message.chat.id)
            return 
        except Exception as err:
            return await dp.bot.send_message(message.chat.id, f"Something went wrong. {err}")
    
    text = message.text
    async with state.proxy() as data:
        data["search_request"] = text
    await dp.bot.send_message(message.chat.id, "Please, choose a category that concerns your request:", reply_markup=search_choose_category())