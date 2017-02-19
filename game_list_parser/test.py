# -*- coding: utf-8 -*-
import urllib.request
import codecs
import re
import os
from bs4 import BeautifulSoup

file = codecs.open("GameList.txt", 'a', 'utf-8')

# online game list
"""
req = urllib.request.Request(
    'https://namu.wiki/w/%EC%98%A8%EB%9D%BC%EC%9D%B8%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('a', class_='wiki-link-internal')

print("########## ONLINE GAME LIST ########")
for item in bs:
    print(item.text)
"""

# mobile game list
"""
req = urllib.request.Request(
    'https://namu.wiki/w/%EB%AA%A8%EB%B0%94%EC%9D%BC%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('ul', class_='wiki-list')

print("########## MOBILE GAME LIST ########")
for item in bs:
    temp = item.find_all('a', class_='wiki-link-internal')
    for item2 in temp:
        print(item2.text)
"""


# playstation game list
"""
req = urllib.request.Request(
    'https://namu.wiki/w/%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%85%98%204/%EA%B2%8C%EC%9E%84%20%EB%AA%A9%EB%A1%9D',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('ul', class_='wiki-list')

gameListArray = []
print("########### PLAYSTATION GAME LIST ########")
for item in bs:
    temp = item.find_all('p')
    for item2 in temp:
        gameName = item2.text.replace(" ☆", "")
        gameName = gameName.replace(" ★", "")
        if gameName[-1] == ' ':
            gameName = gameName[0: -1]
        gameListArray.append(gameName)

print(gameListArray)
for item in gameListArray:
    file.write(item + '\n')
"""

"""
# test
req = urllib.request.Request(
    'https://namu.wiki/edit/%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%85%98%204/%EA%B2%8C%EC%9E%84%20%EB%AA%A9%EB%A1%9D?section=2',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
)

f = urllib.request.urlopen(req).read().decode('utf-8')
bs = BeautifulSoup(f, 'lxml').find('textarea', {"id": "textInput"})

# print(f)
print(bs.text)
"""

"""
req = urllib.request.Request(
    'http://api.steampowered.com/ISteamApps/GetAppList/v0002/',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('apps')

data = json.loads(str(f))
count = 0
for item in data['applist']['apps']:
    count = count+1
    file.write(item['name'] + '\n')
"""

# game list in steam
req = None

for i in range(1, 5):
    print(i)
    req = urllib.request.Request(
        'http://store.steampowered.com/search/?page=' + str(i),
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
        }
    )
    # proxy_host = '154.16.126.94'
    # req.set_proxy(proxy_host, 'http')

    f = urllib.request.urlopen(req).read().decode('utf-8')

    bs = BeautifulSoup(f, 'lxml').find('div', class_='leftcol large')
    bs = bs.find('div', {"id": 'search_result_container'})
    bs = bs.find_all('div')[1]
    bs = bs.find_all('a', class_='search_result_row ds_collapse_flag')

    for item in bs:
        title = item.find('span', class_='title').text

        platform = {'Win': False, 'Mac': False, 'Linux': False}

        if item.find('span', class_='platform_img win'):
            platform['Win'] = True
        if item.find('span', class_='platform_img mac'):
            platform['Mac'] = True
        if item.find('span', class_='platform_img linux'):
            platform['Linux'] = True

        # file.write(title.text + '\n')
        print(title, end="-----")
        print(str(platform['Win']) + str(platform['Mac']) + str(platform['Linux']), end='-----')
        print(item['data-ds-appid'])

        req2 = urllib.request.Request(
            'http://store.steampowered.com/app/' + str(item['data-ds-appid']),
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                'cookie': 'browserid=1344725717332693116; sessionid=adcfbe925844f84782bd1577; strResponsiveViewPrefs=touch; birthtime=678985201; lastagecheckage=9-July-1991; recentapps=%7B%22271590%22%3A1487220706%7D; timezoneOffset=32400,0; _ga=GA1.2.657082707.1487220674; mature_content=1'
            }
        )
        # req2.set_proxy(proxy_host, 'http')

        f = urllib.request.urlopen(req2).read().decode('utf-8')
        bs = BeautifulSoup(f, 'lxml')

        # get game information
        gameInfoBlock = bs.find_all('div', class_='details_block')

        if len(gameInfoBlock) == 5:
            WebsiteBlock = gameInfoBlock[4]
            gameInfoBlock = gameInfoBlock[3]
        else:
            WebsiteBlock = gameInfoBlock[1]
            gameInfoBlock = gameInfoBlock[0]

        genre = gameInfoBlock.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/genre/[.]*')})
        developer = gameInfoBlock.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/search/\?developer[.]*')})
        publisher = gameInfoBlock.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/search/\?publisher[.]*')})

        website = WebsiteBlock.find('a')['href']

        print('GENRE: ', end='')
        for genreName in genre:
            print(genreName.text, end=", ")
        print()

        print('DEVELOPER: ', end='')
        for developerName in developer:
            print(developerName.text, end=', ')
        print()

        print('PUBLISHER: ', end='')  
        for publisherName in publisher:
            print(publisherName.text, end=', ')
        print()

        print(website)
        # get screenshot
        gameScreenshot = bs.find('a', class_='highlight_screenshot_link')
        filename = re.sub('[\W]', '', title)
        urllib.request.urlretrieve(gameScreenshot['href'][43:], os.path.join('D:\\git\\Gamers\\game_list_parser\\pictures', filename + '.jpg'))

