from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def countdown(t):
    global cookie_btn

    while t:
        for i in range(10):
            cookie_btn.click()

        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie_btn = driver.find_element(By.XPATH, '//*[@id="cookie"]')
countdown(300)
