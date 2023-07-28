class Announce:
    def __init__(self, name: str, link: str, price: str, location: str, image_link: str):
        self.name = name
        self.link = link
        self.price = price
        self.location = location
        self.image_link = image_link
        # self.set_price(price)

    def print(self):
        print(self.name)
        print(self.link)
        print(self.price)
        print(self.location)
        print(self.image_link)
    
    def set_price(self, price: str):
        self.price = price
        if "€" in price:
            self.price_int = int(price.replace("€", "").replace(".", "").replace(" ", ""))
        if "Kč" in price:
            self.price_int = int(price.replace("Kč", "").replace(" ", ""))
    
    async def send_announce_to_chat(self, bot, chat_id):
        await bot.send_photo(chat_id, self.image_link, f"Title: {self.name}\n\
Price: {self.price}\n\
Located in: {self.location}\n\n\
More info here: {self.link}")