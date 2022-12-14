from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import lxml
import smtplib
import os


URL = 'https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/dp/B09JQL8KP9/ref=sr_1_2?crid=2Q6ZZF2X3QP9W&keywords=macbook+pro&qid=1671013397&sprefix=macbook%2Caps%2C745&sr=8-2'
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,id;q=0.7,tr;q=0.6"
}

load_dotenv(r'Depth_python\DAY47_Scrape_Product\.env')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


def alerting_email(title_product, product_price):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='bamnbang.id@gmail.com',
            msg=f'Subject:AMAZON ALERT!!\n\n{title_product}\nNow {product_price}'.encode(
                'utf-8')
        )


def scrape_product():
    response = requests.get(url=URL, headers=HEADER)
    data_webpage = response.text

    soup = BeautifulSoup(data_webpage, 'lxml')
    text_product_title = soup.find('span', {'id': 'productTitle'})
    text_price = soup.find('span', class_='a-offscreen')

    title_product = text_product_title.get_text().lstrip()
    product_price = text_price.get_text()

    print(title_product)
    print(product_price)

    alerting_email(title_product=title_product, product_price=product_price)


scrape_product()
