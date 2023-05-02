# BulkEmail-Sending-APP

#Below is the source code
#Recipients Emails used for testing: soulcleansing96@gmail.com, etoontop@gmail.com, ionyolu2757@gmail.com, okaalive@gmail.com

import smtplib
from email.message import EmailMessage
import ssl

name = input('Enter your name: ')
sender_address = input('Enter sender email address: ')
sender_password = 'skerhljtkfkttxqq'
input_recipients_addresses = input('Enter recipients addressses: ')
recipients_addresses = input_recipients_addresses.split(', ')
subject = input('Enter the subject of the email: ')
body = input('Enter the body of the email: ')

bulk_email = EmailMessage()

bulk_email['Fom'] = sender_address
bulk_email['To'] = ','.join(recipients_addresses)
bulk_email['Subject'] = subject
bulk_email.set_content(body)

bulk = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=bulk) as mybulk:
    mybulk.login(sender_address, sender_password)
    mybulk.sendmail(sender_address, recipients_addresses, bulk_email.as_string())
    print(f"Hello {name.capitalize()}, your mail is sent successfully")
