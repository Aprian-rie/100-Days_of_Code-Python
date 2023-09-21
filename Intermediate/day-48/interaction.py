from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("window-size=2400x2400")

driver = webdriver.Chrome( options=options)
driver.set_window_size(1920,1032)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

no_of_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

# no_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

# no_of_articles.click()
# Clicking a link
content_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# content_portals.click()

search = driver.find_element(By.NAME, "search")

# search = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)




