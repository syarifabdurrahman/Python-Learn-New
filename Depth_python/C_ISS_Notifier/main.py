import requests
import datetime as dt
import smtplib
import time
from email_password import *
# import math


URL_ISS = 'http://api.open-notify.org/iss-now.json'
MY_LAT = -6.981010
MY_LONG = 108.492889
LOCAL_UTC_OFFSET = 5

response = requests.get(url=URL_ISS)
response.raise_for_status()

data = response.json()

iss_latitude = float(data['iss_position']['longitude'])
iss_longitude = float(data['iss_position']['latitude'])


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# Splitting T and get index 1 and splitting again and get index 0
sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

lt_sunrise = utc_to_local(sunrise)
lt_sunset = utc_to_local(sunset)

time_now = dt.datetime.now()
hour_now = time_now.hour


print(lt_sunrise)
print(lt_sunset)
print(time_now.hour)


def can_see():
    global iss_latitude, iss_longitude, hour_now, lt_sunrise, lt_sunset

    if MY_LAT + 5 >= iss_latitude or MY_LAT - 5 <= iss_latitude and hour_now >= lt_sunset or hour_now < lt_sunrise and MY_LONG + 5 >= iss_longitude or MY_LONG - 5 <= iss_longitude:
        return True
    else:
        return False

# chec if position is within +5 or -5 degrees of iss position
# if the ISS close to my current position and its currently dark


while not response.raise_for_status():
    time.sleep(60)

    print('Adaw')
    if can_see():
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs='bamnbang.id@gmail.com',
                msg='Subject:Look up\n\nLook up the sky ISS is above you this time!!'
            )
