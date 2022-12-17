from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# get_number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# get_number.click()  # this is how abut clicking

search_bar = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
