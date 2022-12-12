from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
webpage_list = response.text


def scraping(webpage, parser='lxml'):
    soup = BeautifulSoup(webpage, parser)
    title = soup.find_all(
        'h3', class_='title')
    list_title = [title_text.get_text() for title_text in reversed(title)]

    # Creating text
    with open(r'Depth_python\C_Best_Movie_Scrape\result\result.txt', mode='w', encoding='utf-8') as file:
        for movie in list_title:
            file.write(f'{movie}\n')


scraping(webpage_list)
