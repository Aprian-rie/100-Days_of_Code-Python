from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")

# print(event_dates)

# for date in event_dates:
#     print(date.text)

length = len(event_dates)
# print(type(length))

index_event_dictionary = {}

for i in range(length):
    event_dictionary = {}

    event_dictionary['time'] = f"2023-{event_dates[i].text}"
    # if event_titles[i].text == "More":
    #     pass
    # else:
    event_dictionary['name'] = f"{event_titles[i + 1].text}"
    index_event_dictionary[i] = event_dictionary

print(index_event_dictionary)

