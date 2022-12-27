from bs4 import BeautifulSoup
import requests
import lxml
import json


HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7,tr;q=0.6"
}

address_list = []
link_list = []
price_list = []


def scraping():
    # for n in range(1, 21):
    link = f'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B"pagination"%3A%7B"currentPage"%3A2%7D%2C"mapBounds"%3A%7B"west"%3A-123.103495015625%2C"east"%3A-121.763162984375%2C"south"%3A37.20431802773444%2C"north"%3A38.341889054014594%7D%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%7D%2C"isListVisible"%3Atrue%7D'
    # if i != 1:
    #     link = f'https://www.zillow.com/homes/for_rent/{i}_p/?searchQueryState=%7B"pagination"%3A%7B"currentPage"%3A2%7D%2C"mapBounds"%3A%7B"west"%3A-123.103495015625%2C"east"%3A-121.763162984375%2C"south"%3A37.20431802773444%2C"north"%3A38.341889054014594%7D%2C"isMapVisible"%3Afalse%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%7D%2C"isListVisible"%3Atrue%7D'

    response = requests.get(url=link, headers=HEADER)
    response.raise_for_status()
    data_webpage = response.text

    soup = BeautifulSoup(data_webpage, 'lxml')

    # Address
    price_parent = soup.find_all(
        'div', class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX')

    for price_text in price_parent:
        print(price_text.find('span').get_text())


scraping()
