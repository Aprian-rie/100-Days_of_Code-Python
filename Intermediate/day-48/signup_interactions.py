from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
# driver.set_window_size(1920,1032)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email_address = driver.find_element(By.NAME, 'email')

sign_up_button = driver.find_element(By.TAG_NAME, 'button')

first_name.send_keys("Aprian")
last_name.send_keys("Rie")
email_address.send_keys("aprian@gmail.com")

sign_up_button.click()
