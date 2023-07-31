from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp, willhaben
from modules.announce import Announce
# from modules.willhaben import Willhaben
from modules.bazos import generate_bazos_search_link, parse_search_site


@dp.callback_query_handler(lambda callback_query: True)
async def callback_query_handler(call: CallbackQuery, state: FSMContext):
    await call.answer("Working...")
    category = call.data.split(":")[-1]
    request = ""

    async with state.proxy() as data:
        request = data["search_request"]
        data["search_request"] = ""

    await state.finish()

    willhaben_link = willhaben.generate_link_by_category(category, request)
    bazos_link = generate_bazos_search_link(category, request)

    try:
        announces: list[Announce] = []

        await dp.bot.send_message(call.message.chat.id, f"The process of parsing has been started. Please, wait.")

        bazos_announces = parse_search_site(bazos_link)
        willhaben_announces = willhaben.parse_link(willhaben_link)

        announces: list[Announce] = bazos_announces + willhaben_announces 
        if len(announces) == 0:
            await dp.bot.send_message(call.message.chat.id, "No results :(")
            return
        for i in announces:
            await i.send_announce_to_chat(dp.bot, call.message.chat.id)
        return 
    except Exception as err:
        return await dp.bot.send_message(call.message.chat.id, f"Something went wrong. {err}")