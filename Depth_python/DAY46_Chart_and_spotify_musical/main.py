from bs4 import BeautifulSoup
from spotifyAPI import creating_playlist
import requests
import lxml
import datetime
import re


def validate(date_text):
    try:
        date = datetime.datetime.strptime(date_text, r'%Y-%m-%d').date()
        return date
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def scraping_data(urldate, parser='lxml'):
    response = requests.get(
        f"https://www.billboard.com/charts/hot-100/{urldate}")
    song_list_webpage = response.text

    soup = BeautifulSoup(song_list_webpage, parser)

    class_parent_name = 'chart-results-list'
    class_childname = 'o-chart-results-list-row-container'
    music_title = soup.select(
        f'.{class_parent_name} .{class_childname} li h3', {'class': 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only" id="title-of-a-story'})
    # print(music_title)
    list_of_music_title = [re.sub(r'\s+', '', title_text.get_text())
                           for title_text in music_title]

    print(list_of_music_title)
    return list_of_music_title


def getting_data():
    user_input = input(
        'Which year do you want to travel to? Enter a date in YYYY-MM-DD format: ')

    date_time = validate(user_input)
    song_names = scraping_data(urldate=date_time)
    # print(date_time)
    # scraping_data(urldate=date_time)
    creating_playlist(date=date_time, song_names_list=song_names)


getting_data()
