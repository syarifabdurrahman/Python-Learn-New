from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service(
    "E:\Python_Learn\Tools\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get('https://www.python.org/')

upcoming_events_webpage = driver.find_elements(
    By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

upcoming_events_list = [link.find_element(
    By.CSS_SELECTOR, 'a').text for link in upcoming_events_webpage]

upcoming_events_links = [link.find_element(
    By.CSS_SELECTOR, 'a').get_attribute('href') for link in upcoming_events_webpage]

upcoming_events_date = [link.find_element(
    By.CSS_SELECTOR, 'time').text for link in upcoming_events_webpage]


python_events = {}
for i in range(len(upcoming_events_list)):
    python_events[i] = {
        'date': upcoming_events_date[i],
        'name': upcoming_events_list[i],
        'link': upcoming_events_links[i],
    }

print(python_events)
