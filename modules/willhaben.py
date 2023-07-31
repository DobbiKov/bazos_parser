import time
from bs4 import BeautifulSoup
import requests
from lxml import etree
from selenium.webdriver import Firefox
import pickle

from modules.announce import Announce
from modules.add_announce import AddAnnounce

from loader import logger

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

phone_url = "/iad/kaufen-und-verkaufen/d/"



class Willhaben:
    def __init__(self, browser):
        self.browser: Firefox = browser
        self.browser.maximize_window()
        self.is_cookies_loaded = False

        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            self.browser.get("https://willhaben.at")
            for cookie in cookies:
                self.browser.add_cookie(cookie)
            self.browser.get("https://willhaben.at")
            logger.info("The cookies have been loaded to the browser!")
            self.is_cookies_loaded = True
        except Exception as er:
            logger.error(f"Couldn't load cookies. {er}")
        
        self.accept_cookies()

    def login(self):
        pass

    def add_announce(self, announce: AddAnnounce):
        self.browser.get("https://willhaben.at/iad/anzeigenaufgabe/marktplatz?adTypeId=67&productId=67")

        # price
        price_input = self.browser.find_element(by="id", value="price")
        price_input.clear()
        price_input.send_keys(announce.price)

        # title
        title_input = self.browser.find_element("xpath", '//*[@id="heading"]')
        title_input.clear()
        title_input.send_keys(announce.title)

        # category
        category_button = self.browser.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[4]/div/div/div/div/div/button')
        category_button.click()

        if announce.category == "gpus":
            pcs_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[6]')
            pcs_button.click()

            pc_components_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[7]')
            pc_components_button.click()

            gpus_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[4]')
            gpus_button.click()

        if announce.category == "laptops":
            pcs_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[6]')
            pcs_button.click()

            computers_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[2]')
            computers_button.click()

            laptops_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[4]')
            laptops_button.click()

            brands = {
                'acer': 1,
                'apple': 2,
                'asus': 3,
                'dell': 4,
                'fujitsu': 5,
                'hp': 6,
                'huawei': 7,
                'lenovo': 8,
                'microsoft': 10,
                'samsung': 11,
                'sony': 12,
            }

            laptop_brand_button = self.browser.find_element('xpath', f'/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[4]/div[2]/div/div/div/div/div/div[{brands[announce.laptop_brand]}]/div')
            laptop_brand_button.click()
            
            inches = {
                'less11inches': 1,
                '12inches': 2,
                '13inches': 3,
                '14inches': 4,
                '15inches': 5,
                '16inches': 6,
                '17inches': 7,
                'more18inches': 8,
            }
            # 
            laptop_inches_button = self.browser.find_element('xpath', f'/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[4]/div[3]/div/div/div/div/div[{inches[announce.laptop_inches]}]/div')
            laptop_inches_button.click()

        if announce.category == "phones":
            phones_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[13]')
            phones_button.click()

            smartphones_button = self.browser.find_element('xpath', '/html/body/div[5]/div/div/div[3]/div[2]/button[2]')
            smartphones_button.click()

            phone_brands = {
                'alcatel': 1,
                'apple': 2,
                'huawei': 5,
                'motorola': 8,
                'nokia': 9,
                'oneplus': 10,
                'samsung': 11,
                'sony': 12,
                'xiaomi': 14,
                'other': 15,
            }
            phone_brand_button = self.browser.find_element('xpath', f'/html/body/div[5]/div/div/div[3]/div[2]/button[{phone_brands[announce.phone_brand]}]')
            phone_brand_button.click()

            gbs = {
                'more512gb': 1,
                '256gb': 2,
                '128gb': 3,
                '64gb': 4,
                '32gb': 5,
                '16gb': 6,
                'less8gb': 7,
            }
            phone_gbs = self.browser.find_element('xpath', f'/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[4]/div[2]/div/div/div/div/div[{gbs[announce.phone_gbs]}]/div')
            phone_gbs.click()

            unblocked = {
                'yes': 1,
                'no': 2,
            }
            unblocked_button = self.browser.find_element('xpath', f'/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[4]/div[3]/div/div/div/div/div[{unblocked[announce.phone_unblocked]}]/div')
            unblocked_button.click()
            
        # description
        time.sleep(1)

        description_input = self.browser.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[5]/div/div/div/div[2]/div/div/div[1]')
        # description_input.clear()
        description_input.click()
        description_input.send_keys(announce.description)

        time.sleep(1)

        country_select = self.browser.find_element("xpath", '//*[@id="country"]')
        country_select.click()

        if announce.location == "poland":
            poland_option =  self.browser.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/details/div/div[2]/div[1]/div/div/select/option[3]')
            poland_option.click()
        if announce.location == "czech":
            czech_option =  self.browser.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/details/div/div[2]/div[1]/div/div/select/option[44]')
            czech_option.click()
        if announce.location == "ukraine":
            ukraine_option =  self.browser.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/details/div/div[2]/div[1]/div/div/select/option[46]')
            ukraine_option.click()

        post_index_input = self.browser.find_element(by="xpath", value='//*[@id="postCode"]')
        post_index_input.clear()
        post_index_input.send_keys(announce.post_index)

        # description_input = self.browser.find_element("xpath", '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[4]/div/div/form/fieldset/div/div[1]/div/div[5]/div/div/div/div[2]/div/div/div[1]/p')
        # description_input


    def browser_save_cookies(self):
        cookies = self.browser.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))

    def parse_link(self, link) -> list[Announce]:
        links = self.parse_hrefs_from_link(link)
        announces = [self.parse_phone_link(i) for i in links]
        return announces
    
    def accept_cookies(self) -> bool:
        try:
            button = self.browser.find_element(by="xpath", value='//*[@id="didomi-notice-agree-button"]')
            button.click()
            return True
        except:
            return False
            logger.info("The cookies button wasn't found.")
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

        self.accept_cookies()

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