from variables import search_link
from modules.parse_search_site import parse_search_site
import telebot
from telebot import types
from variables import TOKEN
from modules.announce import Announce

from modules.au_parse_seach_site import Willhaben

bot = telebot.TeleBot(TOKEN)

# def main():
#     announces = parse_search_site(search_link)

@bot.message_handler()
def message_handler(message):
    if message.text.startswith("https://"):
        try:
            willhaben = Willhaben()
            link = message.text
            announces: list[Announce] = []

            if "bazos" in message.text:
                bot.send_message(message.chat.id, f"The process of parsing has been started. Please, wait.")
                announces = parse_search_site(link)
            elif "willhaben" in message.text:
                bot.send_message(message.chat.id, f"The process of parsing has been started. Please, wait.")
                announces = willhaben.parse_link(link)

            for i in announces:
                bot.send_photo(message.chat.id, i.image_link, f"Title: {i.name}\n\
Price: {i.price}\n\
Located in: {i.location}\n\n\
More info here: {i.link}")
        except Exception as err:
            bot.send_message(message.chat.id, f"Something went wrong. {err}")

@bot.message_handler(commands=['laptops_1'])
def laptops_1_command(message):
    try:
        announces: list[Announce] = parse_search_site(search_link)
        for i in announces:
            bot.send_photo(message.chat.id, i.image_link, f"Title: {i.name}\n\
Price: {i.price}\n\
Located in: {i.location}\n\n\
More info here: {i.link}")
    except Exception as err:
        bot.send_message(message.chat.id, f"Something went wrong. {err}")
        

bot.polling()
# if __name__ == "__main__":
#     main()