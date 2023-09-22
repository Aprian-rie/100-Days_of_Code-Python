import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920,1032)
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc_btn cc_btn_accept_all']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='langSelectButton title' and @id='langSelect-EN']"))).click()

driver.refresh()

cookie_count = driver.find_element(By.ID, 'cookies').text.split()
cookie_button = driver.find_element(By.ID, 'bigCookie')
timeout = time.time() + 60*2
timeout_start = time.time()

product_price0 = driver.find_element(By.ID, 'productPrice0')
product0 = driver.find_element(By.ID, 'product0')
# print(product_price0.text)
# print(product0.text)
# print(cookie_count)

def check_upgrades():
    if int(cookie_count[0]) > int(product_price0.text):
        product0.click()








# while time.time() < timeout_start + timeout:
#     cookie_button.click()
#
while True:
    cookie_button.click()
    time.sleep(5)
    check_upgrades()
    if time.time() > timeout:
        break


# print(cookies_per_second.text)
# print(cookie_count.text)

# product_0_button = driver.find_element(By.ID, 'product0')
# product_price_0 = driver.find_element(By.ID, 'productPrice0')

# if cookie_count >= product_price_0:
#     product_price_0.click()
# print(cookies_per_second.text)
# print(product_price_0)





