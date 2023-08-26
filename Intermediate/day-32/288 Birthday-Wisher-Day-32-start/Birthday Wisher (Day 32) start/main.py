import smtplib
import datetime as dt
import random

my_email = "aprianbwire@gmail.com"
password = "aqgfvwixiqgszabj"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )

































# import smtplib
#
# my_email = "aprianbwire@gmail.com"
# password = "aqgfvwixiqgszabj"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="aprythomas5@gmail.com",
#         msg="Subject:Hello\n\nThe body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=2001, month=4, day=27)
# print(date_of_birth)
