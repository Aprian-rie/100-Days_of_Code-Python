import smtplib

my_email = "aprianbwire@gmail.com"
password = "aqgfvwixiqgszabj"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="aprythomas5@gmail.com", msg="Hello Aprian")
connection.close()