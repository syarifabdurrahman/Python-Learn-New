import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

MY_LAT = -6.981010
MY_LON = 108.492889

# loaad an key from .env
load_dotenv(r'Depth_python\DAY35_OpenWeather_and_Send_SMS\.env')
API_KEY = os.getenv('OVM_API_KEY')
account_sid = os.getenv('twillio_account_sid')
auth_token = os.getenv('twillio_auth_token')

parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY,
}

response = requests.get(
    'https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_in_hour_list = weather_data['hourly']

for data in weather_in_hour_list[0:12]:
    current_id = data['weather'][0]['id']

    if current_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It\'s going to rain today. Remember to bring an ☂️",
            from_='+18583302206',
            to='+6281240251829'
        )
    print(message.status)
