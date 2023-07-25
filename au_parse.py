import time
from bs4 import BeautifulSoup
import requests
from lxml import etree
from selenium import webdriver

from modules.announce import Announce

link_to_parse = "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/oneplus-2739?sfId=cac891b1-e34c-4301-8faf-7c03049a1c49&isNavigation=true&page=1"

temp_phone_link = "https://www.willhaben.at/iad/kaufen-und-verkaufen/d/oneplus-nord-5g-128gb-grau-display-wie-neu-696681245/"
phone_url = "/iad/kaufen-und-verkaufen/d/"

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
def main():
    print("The program has started")
    # links = parse_hrefs_from_link(link_to_parse)
    # for i in links:
    #     parse_phone_link(i).print()
    #     print("++++++++")

    parse_phone_link(temp_phone_link).print()
    # webpage = requests.get(temp_phone_link, headers=HEADERS).text
    # with open('index.html', 'w') as f:
    #     f.write(webpage)

    # soup = bs4.BeautifulSoup(webpage.content, "html.parser")
    # dom = etree.HTML(str(soup))

    # html = driver.page_source
    # soup = BeautifulSoup(html, "html.parser")

def parse_phone_link(phone_link: str) -> Announce:
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
    
    loc_div = soup.find_all("div", {'data-testid': 'top-contact-box-address-box'})
    loc_spans = loc_div[0].find_all("span")
    laptop_location = ""
    for loc_span in loc_spans:
        laptop_location += loc_span.getText()

    laptop_image_link = dom.xpath('//*[@id="skip-to-content"]/article/section[3]/div/div[2]/div/div/div[1]/div[1]/div[1]/button/img')[0].attrib.get('src')
    
    announce = Announce(laptop_name, laptop_link, laptop_price, laptop_location, laptop_image_link)

    return announce

def parse_hrefs_from_link(link: str) -> str:
    driver = webdriver.Firefox()
    driver.maximize_window()
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
    
    return urls

if __name__ == "__main__":
    main()