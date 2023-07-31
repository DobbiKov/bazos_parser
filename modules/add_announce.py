class AddAnnounce:
    def __init__(self, title: str, link: str, price: str, location: str, image_links: [str], description: str, category: str, post_index: str):
        self.title = title
        self.link = link
        self.price = price
        self.location = location
        self.image_links = image_links
        self.description = description
        self.category = category
        self.post_index = post_index

        self.laptop_brand = ""
        self.laptop_inches = ""

        self.phone_brand = ""
        self.phone_gbs = ""
        self.phone_unblocked = ""
        # self.set_price(price)

    def print(self):
        print(self.title)
        print(self.link)
        print(self.price)
        print(self.location)
        print(self.image_links)
        print(self.description)
        print(self.category)
        print(self.post_index)
    