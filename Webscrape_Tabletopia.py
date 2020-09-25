
# coding: utf-8

import bs4, requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# Loop through all the pages
res_pg1 = requests.get('https://www.boardgamegeek.com/geeklist/201401/tabletopia-official-list-games/page/1?titlesonly=1', headers=headers)
res_pg2 = requests.get('https://www.boardgamegeek.com/geeklist/201401/tabletopia-official-list-games/page/2?titlesonly=1', headers=headers)
res_pg3 = requests.get('https://www.boardgamegeek.com/geeklist/201401/tabletopia-official-list-games/page/3?titlesonly=1', headers=headers)
res_pg4 = requests.get('https://www.boardgamegeek.com/geeklist/201401/tabletopia-official-list-games/page/4?titlesonly=1', headers=headers)

# Parse each of the pages
tt_soup1 = bs4.BeautifulSoup(res_pg1.text, "html.parser")
tt_soup2 = bs4.BeautifulSoup(res_pg2.text, "html.parser")
tt_soup3 = bs4.BeautifulSoup(res_pg3.text, "html.parser")
tt_soup4 = bs4.BeautifulSoup(res_pg4.text, "html.parser")


# Find all the anchor tags and append the href links
links = []
for a in tt_soup1.findAll('a',href=True):
    links.append(a['href'])
    
for a in tt_soup2.findAll('a',href=True):
    links.append(a['href'])
    
for a in tt_soup3.findAll('a',href=True):
    links.append(a['href'])
    
for a in tt_soup4.findAll('a',href=True):
    links.append(a['href'])

# Find all of the boardgame links
games_links = []
for link in links:
    if link.startswith('/boardgame'):
        games_links.append(link)
        print(link)

# Reform the web address
tt_links = []
for link in games_links:
    address = 'https://boardgamegeek.com' + link
    tt_links.append(address)

# Write to text file
with open('C:/Users/Rob/Downloads/board-game-data/parsed_data.txt', 'w') as f:
    for item in tt_links:
        f.write(item + ", ")

# Count the number of items
count = 0
for i in tt_links:
    count += 1
print(count)

