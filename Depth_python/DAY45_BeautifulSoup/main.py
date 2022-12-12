from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://news.ycombinator.com/news')
response.raise_for_status()
yc_web_page = response.text


def scraping(webpage, parser='lxml'):
    soup = BeautifulSoup(webpage, parser)

    # Get Title
    title = soup.find_all('span', class_='titleline')
    upvotes = soup.find_all('span', class_='score')

    article_title = [title_text.find('a').getText() for title_text in title]
    article_links = [title_text.find('a').get('href') for title_text in title]
    article_upvotes = [int(upvote_text.getText().split(" ")[0])
                       for upvote_text in upvotes]

    print(article_upvotes)
    largest_number = min(article_upvotes)
    print(largest_number)

    largest_index = article_upvotes.index(largest_number)
    print(article_title[largest_index + 1])
    print(article_links[largest_index + 1])
    print(f"{article_upvotes[largest_index]} \n")

# print('Result : \n')
# for i in range(30):
#     if (largest_number):
#         print(article_title[i - 1])
#         print(article_links[i - 1])
#         print(f"{article_upvotes[i - 1]} \n")

# upvote = soup.find_all('span', class_='score')

# for i in range(30):
#     print(f"{title[i].find('a').getText()}")
#     print(f"{title[i].find('a').get('href')}")
#     print(f"{upvote[i].getText()} \n")

# Get upvote
# for list_upvote_points in upvote:
#     print(f"{list_upvote_points.getText()}")


scraping(yc_web_page)
