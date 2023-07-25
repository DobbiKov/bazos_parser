class Announce:
    def __init__(self, name: str, link: str, price: str, location: str, image_link: str):
        self.name = name
        self.link = link
        self.price = price
        self.location = location
        self.image_link = image_link

    def print(self):
        print(self.name)
        print(self.link)
        print(self.price)
        print(self.location)
        print(self.image_link)