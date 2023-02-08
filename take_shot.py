#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.add_argument("--headless")
print("Запускаю Хром в безголовлом режиме.")
driver = webdriver.Chrome(options=opts)
driver.set_window_size(1024, 1024)
print("Запустил в размере 1Kx1K.")
url = "https://google.ru"
delay = 3 # seconds
print(f"Даю запрос {url} и жду {delay} секунд.")
driver.get(url)
print("Запрос улетел.")
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'q')))
    print(f"Страница {url} загружена.")
except TimeoutException:
    print(f"Не удалось загрузить {url} за {delay} секунд.")
driver.find_element(By.NAME, 'q').send_keys('жопа стряслась')
driver.save_screenshot("screenshot0.png")
print("Заскриншотил 0.")
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
print("Жмакнул ентер.")
#submit = driver.find_element(By.NAME, 'btnK')
#print("Написал и нашёл, куда жать.")
#submit.click()
#print("Жмакнул.")
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'q')))
    print(f"Кликнул успешно.")
except TimeoutException:
    print(f"Не накликал за {delay} секунд.")
driver.save_screenshot("screenshot1.png")
print("Заскриншотил 1.")
res = driver.find_elements(By.XPATH, '//*[@id="rso"]/div[3]/div/script[*]/text()')
for r in res:
    #e = r.get_attribute("href")
    print(f"Ссылка: {res}")
driver.quit()
print("Кончил.")
