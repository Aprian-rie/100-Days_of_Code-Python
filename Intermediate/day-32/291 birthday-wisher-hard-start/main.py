##################### Hard Starting Project ######################
import csv
import datetime as dt
import random
import smtplib
my_email = "aprianbwire@gmail.com"
password = "aqgfvwixiqgszabj"

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
birthday_dict = {}
with open("birthdays.csv") as birthday_file:
    reader = csv.reader(birthday_file)
    next(reader)

    for row in reader:
        month = row[3]
        day = row[4]
        birthday_dict[(month, day)] = row
# specific_date = ('8', '26')
# name = birthday_dict[specific_date][0]
# print(name)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
today_day = str(dt.datetime.now().day)
today_month = str(dt.datetime.now().month)
my_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
if (today_month, today_day) in birthday_dict:
    name = birthday_dict[(today_month, today_day)][0]
    sent_email = birthday_dict[(today_month, today_day)][1]
    print(sent_email)
    letter_choice = random.choice(my_letters)
    with open(f"letter_templates/{letter_choice}", "r") as my_letter:
        letter = my_letter.read()
        custom_letter = letter.replace("[NAME]", name)
        print(custom_letter)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=sent_email,
            msg=f"Subject:Happy Birthday\n\n{custom_letter}"
        )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
