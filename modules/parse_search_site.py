import bs4, requests
from .announce import Announce

def parse_search_site(link: str) -> list:
    html = requests.get(link).text

    soup = bs4.BeautifulSoup(html, "html.parser")

    divs_laptops = soup.find_all("div", {'class': 'inzeraty'})

    announces = []
    for div_laptop in divs_laptops:
        laptop_name = div_laptop.find("div", {'class': 'inzeratynadpis'}).find("h2", {'class', 'nadpis'}).find("a").getText()
        laptop_price = div_laptop.find("div", {'class': 'inzeratycena'}).find("b").getText()
        laptop_link = "https://pc.bazos.cz" + div_laptop.find("div", {'class': 'inzeratynadpis'}).find("h2", {'class', 'nadpis'}).find("a")['href']
        laptop_location = div_laptop.find("div", {'class': 'inzeratylok'}).getText()
        laptop_image_link = div_laptop.find("img", {'class': 'obrazek'})['src']
        
        announce = Announce(laptop_name, laptop_link, laptop_price, laptop_location, laptop_image_link)
        announces.append(announce)
    return announces