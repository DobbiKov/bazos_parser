from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from selenium import webdriver
from loguru import logger

from data import config
from modules.willhaben import Willhaben

logger.add('logging/debug.txt', format="{time} {level} {message}", level="DEBUG", rotation="24 hour", compression="zip")

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920,1080")

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
browser = webdriver.Firefox(options=firefox_options)
willhaben = Willhaben(browser)
