from PIL import Image
from loader import dp, logger
from aiogram import types
from aiogram.dispatcher import FSMContext
from typing import List
import os

# # state=AddAnnounceForm.photos
# @dp.message_handler(is_media_group=True, content_types=types.ContentTypes.PHOTO)
# async def process_photos(message: types.Message, album: List[types.Message], state: FSMContext):
#     photo_ids = []
#     for i in album:
#         if not i.photo:
#             continue
#         photo_ids.append(i.photo[-1].file_id)
#     if not os.path.exists(f"./pictures/{message.from_user.id}"):
#         os.mkdir(f"./pictures/{message.from_user.id}")
#     for i in photo_ids:
#         file = await dp.bot.get_file(i)
#         file_path = file.file_path  
#         src = "./pictures/" + str(message.from_user.id) + "/" + str(i) + ".png" 
#         download_file = await dp.bot.download_file(file_path, src) 
#     await message.answer("The file is saved!!")

# # @dp.message_handler(content_types=["photo"])
# # async def process_photo(message: types.Message, state: FSMContext):
# #     message.photo