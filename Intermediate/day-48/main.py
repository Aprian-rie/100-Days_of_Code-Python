from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:\Development\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.amazon.com/PlayStation4-Console-1TB-Warfare-PlayStation-4/dp/B0BSVRC9K1/ref=sr_1_2?crid=37V2B5VSBRDGF&keywords=ps4&qid=1695144737&sprefix=PS4%2Caps%2C401&sr=8-2")
# price = driver.find_element(By.CLASS_NAME, 'a-offscreen')
price = driver.find_element(By.CSS_SELECTOR, 'span.a-size-medium')
price2 = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]')
price3 = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
price4 = driver.find_element(By.ID, 'corePrice_desktop')
title = driver.find_element(By.ID, 'productTitle')

print(price2.text)
print(title.text)
print(price3.text)
print(price4.text)
# print(price.text)

# close will close a particular tab
# driver.close()

# quit will close the entire browser/ program
driver.quit()

