Day 32, learning about email SMTP and the date time module

How to send an email using python
```python
import smtplib

#Use your own emails and passwords
my_email = "youremail@gmail.com"
sent_email = "torecepient@gmail.com"
password = "randompassword"
custom_letter ="Some words"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=sent_email,
            msg=f"Subject:Happy Birthday\n\n{custom_letter}"
        )
```
#### Things to Note When Sending an email 
- Make sure that you have the correct smtp address for the email provider
  - Gmail: smtp.gmail.com
  - Hotmail: smtp.live.com
  - Outlook: outlook.office365.com
  - Yahoo: smtp.mail.yahoo.com
- If you use another email provider just Google for the email provider

#### Specific steps for Gmail addresses
- Make sure you've enabled less secure apps if sending from Gmail account.
- Try to go through the Gmail Captcha while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
- Add a port number by changing your code to this:
``smtplib.SMTP("smtp.gmail.com, port=587)``
### The End

By Aprian