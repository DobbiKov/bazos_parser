class AddAnnounce:
    def __init__(self, user_id, title: str, link: str, price: str, location: str, description: str, category: str, post_index: str):
        self.title = title
        self.link = link
        self.price = price
        self.location = location
        self.description = description
        self.category = category
        self.post_index = post_index

        self.user_id = user_id

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
    