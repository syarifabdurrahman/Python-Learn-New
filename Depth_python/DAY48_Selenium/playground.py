from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get('https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-14%E2%80%91core/dp/B09JQL8KP9/ref=sr_1_2?crid=2Q6ZZF2X3QP9W&keywords=macbook+pro&qid=1671013397&sprefix=macbook%2Caps%2C745&sr=8-2')

price = driver.find_element(
    By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]')
print(price.text)

driver.quit()
