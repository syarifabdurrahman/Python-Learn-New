import smtplib
import datetime as dt
from dummy_data import *
import random
import pandas


letter_templates_path = [letter_1, letter_2, letter_3]
file = pandas.read_csv(r'Depth_python\C_Birthday_wisher\birthdays.csv')

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day


def randomizing_letter(curr_email, curr_name):
    global letter_templates_path

    random_letter = random.choice(letter_templates_path)
    print(random_letter)
    with open(random_letter, mode='r') as letter:
        content = letter.read()
        the_message = content.replace('[NAME]', f'{curr_name}')
        send_email(to_address=curr_email,
                   message=f'Subject:Happy birthday\n\n{the_message}')

        # with open(f"Depth_python\C_Birthday_wisher\output_to_send\sendletter_to_{name}.txt", mode='r') as letter_ready:
        #     new_content = letter_ready.read()
        #     send_email(to_address=curr_email,
        #                message=f'Subject:Happy birthday\n\n{new_content}')


def send_email(to_address, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_address,
            msg=message
        )


def birthday_wisher():
    for index, row in file.iterrows():
        if current_month == row['month'] and current_day == row['day']:
            randomizing_letter(curr_email=row['email'], curr_name=row['name'])


birthday_wisher()
