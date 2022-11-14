# response code

# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

import requests
import datetime as dt

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # response.raise_for_status()  # check if not okay raise the error

# # print(response.status_code)  # getting status code
# # print(response.text)  # getting data

# data = response.json()  # same getting data
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# print(f'longitude: {longitude}, latitude: {latitude}')

# API Parameters

MY_LAT = -6.981010
MY_LONG = 108.492889
LOCAL_UTC_OFFSET = 5


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

print(lt_sunrise)
print(lt_sunset)

time_now = dt.datetime.now()
print(time_now.hour)

# formula: Endpoint?param_name=Value& ....
