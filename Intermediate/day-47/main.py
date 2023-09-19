import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

my_email = "aprianbwire@gmail.com"
password = "aqgfvwixiqgszabj"

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
              "Safari/537.36")
accept_lang = "en-GB,en-TZ;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6"
URL = ("https://www.amazon.com/PlayStation4-Console-1TB-Warfare-PlayStation-4/dp/B0BSVRC9K1/ref=sr_1_2?crid"
       "=37V2B5VSBRDGF&keywords=ps4&qid=1695144737&sprefix=PS4%2Caps%2C401&sr=8-2")
response = requests.get(URL, headers={"User-agent": f"{user_agent}", "Accept-Language": f"{accept_lang}"})
amazon_product_webpage = response.text
# print(amazon_product)

soup = BeautifulSoup(amazon_product_webpage, "lxml")

price_element = soup.find(name="span", class_="a-offscreen")
name_element = soup.find(name="span", class_="a-size-large product-title-word-break")
price_string = price_element.getText()[1:]
# price_float = float(price_string)
price_float = 200

name_of_product = name_element.getText().strip()
# print(name_of_product)

# print(price_float)
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

    #-- Alternative by Chat Gpt --##
    # subject = "Amazon Price Alert!"
    # body = f"{name_of_product} is now ${price_float}\n{URL}"
    #
    # msg = MIMEMultipart()
    # msg["From"] = my_email
    # msg["To"] = my_email
    # msg["Subject"] = subject
    #
    # msg.attach(MIMEText(body, "plain"))
    #
    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs=my_email,
    #         msg=msg.as_string()
    #     )
