from variables import search_link
from modules.parse_search_site import parse_search_site
import telebot
from telebot import types
from variables import TOKEN
from modules.announce import Announce

bot = telebot.TeleBot(TOKEN)

# def main():
#     announces = parse_search_site(search_link)

@bot.message_handler()
def message_handler(message):
    if message.text.startswith("https://"):
        try:
            link = message.text
            announces: list[Announce] = parse_search_site(link)
            for i in announces:
                bot.send_photo(message.chat.id, i.image_link, f"Title: {i.name}\n\
Price: {i.price}\n\
Located in: {i.location}\n\n\
More info here: {i.link}")
        except:
            bot.send_message(message.chat.id, "Something went wrong.")

@bot.message_handler(commands=['laptops_1'])
def laptops_1_command(message):
    try:
        announces: list[Announce] = parse_search_site(search_link)
        for i in announces:
            bot.send_photo(message.chat.id, i.image_link, f"Title: {i.name}\n\
Price: {i.price}\n\
Located in: {i.location}\n\n\
More info here: {i.link}")
    except:
        bot.send_message(message.chat.id, "Something went wrong.")
        
@bot.message_handler(commands=['find_by_link'])
def find_by_link_command(message):
    try:
        link = message.text.split("/find_by_link ")[-1]
        announces: list[Announce] = parse_search_site(link)
        for i in announces:
            bot.send_photo(message.chat.id, i.image_link, f"Title: {i.name}\n\
Price: {i.price}\n\
Located in: {i.location}\n\n\
More info here: {i.link}")
    except:
        bot.send_message(message.chat.id, "Something went wrong.")

bot.polling()
# if __name__ == "__main__":
#     main()