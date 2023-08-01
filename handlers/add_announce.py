from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.add_announce_category import add_announce_category, add_announce_inches, add_announce_laptops, add_announce_phone_brand, add_announce_phone_gbs, add_announce_phone_unblocked
from keyboards.inline.add_announce_country import add_announce_country

from loader import dp, willhaben, logger
from modules.add_announce import AddAnnounce
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from typing import List
import os

class AddAnnounceForm(StatesGroup):
    title = State()
    description = State()
    price = State()
    category = State()
    country = State()
    post_index = State()
    photos = State()



@dp.message_handler(commands=['add_announce'])
async def add_announce_command(message: types.Message, state: FSMContext):
    # add_announce = AddAnnounce("oneplus 8", "", "1000", "fdsafads", "dsfafasd", "Oneplus бери не хочу")
    # willhaben.add_announce(add_announce)
    await AddAnnounceForm.title.set()
    await dp.bot.send_message(message.chat.id, "Enter the title of the announce:")


@dp.message_handler(state='*', commands='cancel_announce')
@dp.message_handler(Text(equals='cancel_announce', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=AddAnnounceForm.title)
async def process_title(message: types.Message, state: FSMContext):
    """
    Process title
    """
    async with state.proxy() as data:
        data['title'] = message.text

    await AddAnnounceForm.next()
    await message.reply("Enter the description:")

@dp.message_handler(state=AddAnnounceForm.description)
async def process_description(message: types.Message, state: FSMContext):
    """
    Process description
    """
    async with state.proxy() as data:
        data['description'] = message.text

    await AddAnnounceForm.next()
    await message.reply("Enter the price in eur(digits only):")

@dp.message_handler(lambda message: not message.text.isdigit(), state=AddAnnounceForm.price)
async def process_error_price(message: types.Message, state: FSMContext):
    """
    Process error price
    """

    return await message.reply("Enter the price in eur(digits only):")

@dp.message_handler(lambda message: message.text.isdigit(), state=AddAnnounceForm.price)
async def process_price(message: types.Message, state: FSMContext):
    """
    Process price
    """
    await AddAnnounceForm.next()
    await state.update_data(price=int(message.text))

    return await message.reply("Choose a category of the announce:", reply_markup=add_announce_category())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_add"), state=AddAnnounceForm.category)
async def callback_category_query_handler(call: CallbackQuery, state: FSMContext):
    """
    Process a category
    """
    category = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['category'] = category
    
    if category == "phones":
        return await call.message.reply("Choose a phone brand:", reply_markup=add_announce_phone_brand())
    if category == "laptops":
        return await call.message.reply("Choose a laptop brand:", reply_markup=add_announce_laptops())

    await AddAnnounceForm.next()
    await call.message.reply("Choose a country where you send the announce from:", reply_markup=add_announce_country())
#phone
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_phone_unblocked"), state=AddAnnounceForm.category)
async def callback_phone_unblocked_query_handler(call: CallbackQuery, state: FSMContext):
    phone_unblocked = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['phone_unblocked'] = phone_unblocked

    await AddAnnounceForm.next()
    await call.message.reply("Choose a country where you send the announce from:", reply_markup=add_announce_country())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_phone_gbs"), state=AddAnnounceForm.category)
async def callback_phone_gbs_query_handler(call: CallbackQuery, state: FSMContext):
    phone_gbs = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['phone_gbs'] = phone_gbs

    await call.message.reply("Is phone unblocked?", reply_markup=add_announce_phone_unblocked())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_phone"), state=AddAnnounceForm.category)
async def callback_phone_brand_query_handler(call: CallbackQuery, state: FSMContext):
    phone_brand = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['phone_brand'] = phone_brand

    await call.message.reply("Choose phone GBs amount:", reply_markup=add_announce_phone_gbs())

#phone^^^

#laptop
@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_laptop_inch"), state=AddAnnounceForm.category)
async def callback_laptop_inches_query_handler(call: CallbackQuery, state: FSMContext):
    laptop_inches = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['laptop_inches'] = laptop_inches

    await AddAnnounceForm.next()
    await call.message.reply("Choose a country where you send the announce from:", reply_markup=add_announce_country())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_laptop"), state=AddAnnounceForm.category)
async def callback_laptop_brand_query_handler(call: CallbackQuery, state: FSMContext):
    laptop_brand = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['laptop_brand'] = laptop_brand

    return await call.message.reply("Choose laptop inches:", reply_markup=add_announce_inches())
#laptop^^^
    

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("willhaben_add_country"), state=AddAnnounceForm.country)
async def callback_query_handler(call: CallbackQuery, state: FSMContext):
    country = call.data.split(":")[-1]
    async with state.proxy() as data:
        data['country'] = country
    await AddAnnounceForm.next()
    await call.message.reply("Write a post index(digits only):")

@dp.message_handler(lambda message: not message.text.isdigit() or len(message.text) != 5, state=AddAnnounceForm.post_index)
async def process_name(message: types.Message, state: FSMContext):

    return await message.reply("Write a post index(digits only):")

@dp.message_handler(lambda message: message.text.isdigit(), state=AddAnnounceForm.post_index)
async def process_post_index(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['post_index'] = message.text
        await AddAnnounceForm.next()
    await message.answer("Send me announce photos:")

@dp.message_handler(is_media_group=True, content_types=types.ContentTypes.PHOTO, state=AddAnnounceForm.photos)
async def process_photos(message: types.Message, album: List[types.Message], state: FSMContext):
    photo_ids = []
    for i in album:
        if not i.photo:
            continue
        photo_ids.append(i.photo[-1].file_id)
    photos_paths = await save_photos(message.from_user.id, photo_ids)
    async with state.proxy() as data:
        announce = AddAnnounce(message.from_user.id, data['title'], "", data['price'], data['country'], photos_paths, data['description'], data['category'], data['post_index'])
        if data['category'] == "laptops":
            announce.laptop_brand = data['laptop_brand']
            announce.laptop_inches = data['laptop_inches']

        if data['category'] == "phones":
            announce.phone_brand = data['phone_brand']
            announce.phone_gbs = data['phone_gbs']
            announce.phone_unblocked = data['phone_unblocked']

        announce.print()
        willhaben.add_announce(announce)
        await message.reply("Congrats! You've added an announce!")
    await state.finish()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=AddAnnounceForm.photos)
async def process_photo(message: types.Message, state: FSMContext):
    photo_ids = []
    photo_ids.append(message.photo[-1].file_id)
    photos_paths = await save_photos(message.from_user.id, photo_ids)
    async with state.proxy() as data:
        announce = AddAnnounce(message.from_user.id, data['title'], "", data['price'], data['country'], photos_paths, data['description'], data['category'], data['post_index'])
        if data['category'] == "laptops":
            announce.laptop_brand = data['laptop_brand']
            announce.laptop_inches = data['laptop_inches']

        if data['category'] == "phones":
            announce.phone_brand = data['phone_brand']
            announce.phone_gbs = data['phone_gbs']
            announce.phone_unblocked = data['phone_unblocked']

        # announce.print()
        announce_link = willhaben.add_announce(announce)
        await message.reply(f"Congrats! You've added an announce!\n\
Here is your link: {announce_link}")
    await state.finish()

async def save_photos(user_id, photo_ids: list) -> list[str]:
    photo_paths = []
    if not os.path.exists(f"./pictures/{user_id}"):
        os.mkdir(f"./pictures/{user_id}")
    for i in photo_ids:
        file = await dp.bot.get_file(i)
        file_path = file.file_path  
        src = "./pictures/" + str(user_id) + "/" + str(i) + ".png" 
        download_file = await dp.bot.download_file(file_path, src) 
        photo_paths.append(src)
    return photo_paths

