from aiogram import executor

from loader import dp, logger
import handlers
from middlewares.album_middleware import AlbumMiddleware
# from utils.notify_admins import on_startup_notify
# from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # await set_default_commands(dispatcher)

    # await on_startup_notify(dispatcher)
    logger.info("The bot has been started!")


if __name__ == '__main__':
    dp.middleware.setup(AlbumMiddleware())
    executor.start_polling(dp, on_startup=on_startup)

