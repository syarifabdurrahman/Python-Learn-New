import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from twilio.rest import Client

SYMBOL = 'META'

load_dotenv(r'Depth_python\DAY36_Stock_notifier\.env')
stock_api = os.getenv('STOCK_API_KEY')
news_api = os.getenv('NEWS_API_KEY')
twilio_token = os.getenv('twillio_auth_token')
account_sid = 'AC7191331c0433a787ebcb14c5671c32d2'

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': SYMBOL,
    'apikey': stock_api,
}

today = datetime.today().date()
yesterday = today - timedelta(days=1)
two_days_from_today = yesterday - timedelta(days=1)
days = [yesterday.strftime(r'%Y-%m-%d'),
        two_days_from_today.strftime(r'%Y-%m-%d')]

response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()

stock_data_raw = response.json()
stock_data = stock_data_raw['Time Series (Daily)']
two_last_day_stocks = []

for x, y in sorted(stock_data.items(), reverse=True)[:2]:
    # print(y['5. adjusted close'])
    two_last_day_stocks.append(float(y['5. adjusted close']))

pecentage = round((two_last_day_stocks[0] - two_last_day_stocks[1])/100, 3)


parameters = {
    'q': 'facebook',
    'from': '2022-11-18',
    'sortBy': 'popularity',
    'apiKey': news_api
}

response = requests.get('https://newsapi.org/v2/everything', params=parameters)
response.raise_for_status()

news_data = response.json()
headline = news_data['articles'][0]['title']
brief = news_data['articles'][0]['content']


def send_message(icon):
    global headline, brief, pecentage, account_sid, twilio_token

    client = Client(account_sid, twilio_token)
    message = client.messages \
        .create(
            body=f"{SYMBOL}{icon}{pecentage}%\nHeadline: {headline}\nBrief: {brief}",
            from_='+18583302206',
            to='+6281240251829'
        )
    print(message.status)


if two_last_day_stocks[0] > two_last_day_stocks[1]:
    _icon = '🔼'
    send_message(_icon)
else:
    _icon = '🔽'
    send_message(_icon)
