from bs4 import BeautifulSoup
import lxml

with open(r'Depth_python\DAY45_BeautifulSoup\website.html', mode='r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(
    contents, 'lxml')

print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.p)
print(soup.ul)

for list in soup.ul:
    print(list.string)

for list in soup.find_all('li'):
    print(list.string)

children = soup.find('ul', {'class': 'list'}).findChildren(
    'li', recursive=False)

for list in children:
    print(list.string)


all_anchor_tags = soup.findAll(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get('href'))


# using like css
company_url = soup.select_one(selector='p a')
print(company_url)

new_list = [text.string for text in soup.ul]
print(new_list)
