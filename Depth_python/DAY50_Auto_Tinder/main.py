from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, InvalidSelectorException
from dotenv import load_dotenv
import random
import os
import time


load_dotenv(r'Depth_python\DAY50_Auto_Tinder\.env')
FB_USERNAME = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(
    service=chrome_driver_path, options=chrome_options)
driver.get('https://tinder.com/')

main_page = driver.current_window_handle


def login():

    # Allow Cookies
    cookies = driver.find_element(
        By.XPATH, "//*[@id='q888578821']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
    cookies.click()

    login_btn = driver.find_element(
        By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    login_btn.click()

    time.sleep(2)

    facebook_btn = driver.find_element(
        By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
    facebook_btn.click()

    time.sleep(3)

    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle

    driver.switch_to.window(login_page)
    # print(driver.title)  # chec if its facebook

    # Login Facebook
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    password = driver.find_element(By.XPATH, '//*[@id="pass"]')

    email.send_keys(FB_USERNAME)
    password.send_keys(FB_PASSWORD)
    password.send_keys(Keys.ENTER)

    driver.switch_to.window(main_page)
    print(driver.title)

    time.sleep(5)

    try:
        check_components()
    except NoSuchElementException:
        time.sleep(10)
        check_components()

    time.sleep(5)
    start_working()


def check_components():
    # Allow Location
    location_btn = driver.find_element(
        By.XPATH, "//*[@id='q-839802255']/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
    location_btn.click()

    time.sleep(5)

    # Allow Notification
    notification_btn = driver.find_element(
        By.XPATH, "//*[@id='q-839802255']/main/div/div/div/div[3]/button[2]/div[2]/div[2]")
    notification_btn.click()

    time.sleep(5)

    try:
        # Decline dark mode
        dark_close_btn = driver.find_element(
            By.XPATH, "/html/body/div[2]/main/div/div[2]/button")
        dark_close_btn.click()
    except:
        time.sleep(10)
        dark_close_btn = driver.find_element(
            By.XPATH, "//*[@id='q-839802255']/main/div/div[2]/button")
        dark_close_btn.click()


def start_working():

    for i in range(100):
        print("Working Now!")
        try:
            time.sleep(3)
            action = driver.find_element(
                By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
            action.click()
        except NoSuchElementException:
            try:
                time.sleep(4)
                action = driver.find_element(
                    By.XPATH, '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
                action.click()
                continue
            except ElementClickInterceptedException:
                print("exceptions.ElementClickInterceptedException")
                time.sleep(5)
                match_pop = driver.find_element(
                    By.XPATH, "//*[@id='q-71405977']/main/div/div[1]/div/div[4]/button")
                match_pop.click()

    # driver.quit()


if __name__ == '__main__':
    login()
