Day 47, building an Amazon Price Tracker Project, it alerts us using an email telling us when the price of an item drops to a certain value
### Steps of The Amazon Tracker Project
1. Found a product that I wanted to track, in my case was the PS4 Modern warfare edition 
https://www.amazon.com/PlayStation4-Console-1TB-Warfare-PlayStation-4/dp/B0BSVRC9K1/ref=sr_1_2?crid
2. The process of scraping Amazon was kinda complex, it required to add some specific headers otherwise it wouldn't work
-  At minimum the required headers were ``"User-Agent`` and ``"Accept-Language``
- Inorder to access these headers visit http://myhttpheader.com


```python
import requests
# How to pass headers with the requests library
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
              "Safari/537.36")
accept_lang = "en-GB,en-TZ;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6"
URL = ("https://www.amazon.com/PlayStation4-Console-1TB-Warfare-PlayStation-4/dp/B0BSVRC9K1/ref=sr_1_2?crid"
       "=37V2B5VSBRDGF&keywords=ps4&qid=1695144737&sprefix=PS4%2Caps%2C401&sr=8-2")
response = requests.get(URL, headers={"User-agent": f"{user_agent}", "Accept-Language": f"{accept_lang}"})
amazon_product_webpage = response.text
```
3. After obtaining my required webpage I consoled to the output to make sure it's the one i'm looking for
-``print(amazon_product_webpage)``
4. It's time for scraping where I used beautiful soup to obtain my required data which are the price plus the name of the required item
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(amazon_product_webpage, "lxml")

price_element = soup.find(name="span", class_="a-offscreen")
name_element = soup.find(name="span", class_="a-size-large product-title-word-break")

# Slice method was used to get rid of the $ sign in the price 
price_string = price_element.getText()[1:]
price_float = float(price_string)
# price_float = 200

name_of_product = name_element.getText().strip()
# Strip was used to get rid of the extra whitespace
# print(name_of_product)
```
5. We want to get an email when the price of our product is below a certain value in our case for our PS4 if it is less than $290
so when the price is below 290 we use smtp module to send an emailincluding the title, current price and the link to buy the product.
```python
if price_float < 290.00:
    message = f"{name_of_product} is now ${price_float}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
```
The ``.encode("utf-8)`` is very important to encode non-ASCII characters as if you don't you might encounter an error

``The error you're encountering, UnicodeEncodeError,
occurs when you try to send an email with non-ASCII characters in the subject or body of the email.
Using the smtplib library. In your code, you have a character '\u2013' (an en dash)
in the name_of_product, which might be causing this issue.``

### The End

By Aprian
