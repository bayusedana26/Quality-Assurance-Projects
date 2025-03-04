from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_pathh="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

big_cookie = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

lang = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
lang.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, big_cookie))
)

cookie = driver.find_element(By.ID, big_cookie)

while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)

        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break


