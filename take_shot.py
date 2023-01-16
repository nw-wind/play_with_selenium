#!/usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

opts = Options()
opts.add_argument("--headless")
print("Запускаю Хром в безголовлом режиме.")
driver = webdriver.Chrome(options=opts)
driver.set_window_size(1024, 1024)
print("Запустил в размере 1Kx1K.")
url = "https://ya.ru"
delay = 3 # seconds
print(f"Даю запрос {url} и жду {delay} секунд.")
driver.get(url)
print("Запрос улетел.")
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'text')))
    print(f"Страница {url} загружена.")
except TimeoutException:
    print(f"Не удалось загрузить {url} за {delay} секунд.")
driver.find_element(By.NAME, 'text').send_keys('жопа стряслась')
driver.save_screenshot("screenshot0.png")
print("Заскриншотил 0.")
submit = driver.find_element(By.XPATH, '/html/body/main/div[2]/form/div[2]/button')
print("Написал и нашёл, куда жать.")
submit.click()
print("Жмакнул.")
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'text')))
    print(f"Кликнул успешно.")
except TimeoutException:
    print(f"Не накликал за {delay} секунд.")
driver.save_screenshot("screenshot1.png")
print("Заскриншотил 1.")
res = driver.find_elements(By.XPATH, '//*[@id="search-result"]/li[*]/div/div[2]/div/a')
for r in res:
    e = r.get_attribute("href")
    print(f"Ссылка: {e}")
driver.quit()
print("Кончил.")
