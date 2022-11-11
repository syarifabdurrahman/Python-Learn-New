import smtplib
from data import *
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open(r'Depth_python\DAY32_Email_Automation\quotes.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='bamnbang.id@gmail.com',
            msg=f'Subject:Motivation\n\n{quote}'
        )
