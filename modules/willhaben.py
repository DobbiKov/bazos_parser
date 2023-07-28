import time
from bs4 import BeautifulSoup
import requests
from lxml import etree

from modules.announce import Announce

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

phone_url = "/iad/kaufen-und-verkaufen/d/"



class Willhaben:
    def __init__(self, browser):
        self.browser = browser
        self.browser.maximize_window()

    def parse_link(self, link) -> list[Announce]:
        links = self.parse_hrefs_from_link(link)
        announces = [self.parse_phone_link(i) for i in links]
        return announces

    def parse_phone_link(self, phone_link: str) -> Announce:
        html = requests.get(phone_link, headers=HEADERS).text

        soup = BeautifulSoup(html, "html.parser")
        dom = etree.HTML(str(soup))

        laptop_name = dom.xpath('//*[@id="skip-to-content"]/article/section[3]/div/div[1]/div/div[1]/div[1]/h1')[0].text
        laptop_price = ""

        price_dom = dom.xpath('//*[@id="skip-to-content"]/article/section[3]/div/div[3]/div/div/div[1]/div/span[1]')
        price_dom_2 = dom.xpath('//*[@id="skip-to-content"]/article/section[3]/div/div[3]/div/div/div[1]/div/div[1]/span[1]')

        if len(price_dom) > 0:
            laptop_price = price_dom[0].text
        elif len(price_dom_2) > 0:
            laptop_price = price_dom_2[0].text

        laptop_link = phone_link
        laptop_location = self.parse_locations(soup)
        laptop_image_link = dom.xpath('//*[@id="skip-to-content"]/article/section[3]/div/div[2]/div/div/div[1]/div[1]/div[1]/button/img')[0].attrib.get('src')
        
        announce = Announce(laptop_name, laptop_link, laptop_price, laptop_location, laptop_image_link)

        return announce

    def parse_locations(self, soup) -> str:
        loc_div = soup.find_all("div", {'data-testid': 'top-contact-box-address-box'})
        loc_spans = loc_div[0].find_all("span")
        laptop_location = ""
        for loc_span in loc_spans:
            laptop_location += loc_span.getText()
        return laptop_location

    def parse_hrefs_from_link(self, link: str) -> str:
        driver = self.browser
        driver.get(link)

        time.sleep(5)

        button = driver.find_element(by="xpath", value='//*[@id="didomi-notice-agree-button"]')
        button.click()

        time.sleep(3)

        for i in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)

        hrefs = driver.find_elements(by="tag name", value='a')

        urls = []
        for item in hrefs:
            href = item.get_attribute('href')
            if href == None:
                continue
            if phone_url not in href:
                continue
            urls.append(href)
        
        driver.close()
        return urls[3::]
    
    def generate_link_by_category(self, category, request):
        request = request.replace(" ", "%20")
        if category == "phones":
            return "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/smartphones-handys-2722?sfId=610a8d40-20b9-416d-bdc8-d7387616eb8a&isNavigation=true&keyword=" + request
        if category == "laptops":
            return "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/computer-tablets-5828?sfId=19c08a04-cdde-4ac3-9907-606598efba8c&isNavigation=true&keyword=" + request
        if category == "gpus":
            return "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/pc-komponenten/grafikkarten-5882?sfId=ac3d5d75-760b-4728-a86e-52f83435e00a&rows=30&isNavigation=true&keyword=" + request
        return Exception("You used the wrong category")