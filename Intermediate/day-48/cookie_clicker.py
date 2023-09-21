from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.set_window_size(1920,1032)
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cc_btn cc_btn_accept_all']"))).click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='langSelectButton title' and @id='langSelect-EN']"))).click()

# language_selector = driver.find_element(By.ID, 'langSelect-EN')
# language_selector = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
# language_selector.click()

cookie_count = driver.find_element(By.ID, 'cookies')
cookies_per_second = driver.find_element(By.ID, 'cookiesPerSecond')
cookie_button = driver.find_element(By.ID, 'bigCookie')

print(cookies_per_second.text)

# product_0_button = driver.find_element(By.ID, 'product0')
# product_price_0 = driver.find_element(By.ID, 'productPrice0')

# if cookie_count >= product_price_0:
#     product_price_0.click()
# print(cookies_per_second.text)
# print(product_price_0)

cookie_button.click()



