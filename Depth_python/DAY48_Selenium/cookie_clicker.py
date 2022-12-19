from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import random


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(
    service=chrome_driver_path, options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')


def countdown(t, cookie_btn):

    while t:
        current_cookie = get_cookie()

        for i in range(1, 50):
            cookie_btn.click()

        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        random_buy(current_cookie)


def get_cookie():
    global driver

    cokie_amount = driver.find_element(By.XPATH, '//*[@id="money"]')
    print(f'Cookie Amount: {cokie_amount.text}')

    return cokie_amount.text


def random_buy(cokie_amount):
    global driver

    store_element = driver.find_elements(
        By.CSS_SELECTOR, '#rightPanel #store div')
    store_price = driver.find_elements(By.CSS_SELECTOR, '#store div b')
    store_list_price = []
    for a in store_price[:-1]:
        store_list_price.append(a.text.split(' - ')[1].replace(",", ""))

    # bug here
    store_list = []
    for i in store_element[:1]:
        store_list.append(i.text)

    random_index = random.randrange(0, 8)
    get_store_price = store_list_price[random_index]
    print(random_index)

    # for i in store_element:
    #     print(f'{i.text} \n')

    if int(cokie_amount) >= int(get_store_price):
        store_element[random_index].click()
    else:
        print('not enought cookie')

    print(f'price list len: {len(store_list_price)}')
    print(f'store len: {len(store_list)}')
    print(f'store_list: {store_list}')


def start_clicking():
    global driver

    cookie_btn = driver.find_element(By.XPATH, '//*[@id="cookie"]')

    countdown(300, cookie_btn)


start_clicking()
