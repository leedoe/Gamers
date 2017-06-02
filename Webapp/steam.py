# -*- coding: utf-8 -*-
import urllib.request
import requests
import codecs
import re
import os
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"reviewer.settings")

import django
django.setup()
from Gamers.models import Game, Developer, Genre, Publisher, Platform, Screenshot


# stroe.steampowered 페이지에 있는 게임 목록을 가져옴
def get_appid_steam(page_number):
    appid = []
    for i in range(1, page_number):
        req = urllib.request.Request(
            'http://store.steampowered.com/search/?page=' + str(i),
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
            }
        )

        f = urllib.request.urlopen(req).read().decode('utf-8')

        bs = BeautifulSoup(f, 'lxml')
        appid_row = bs.find_all('a', class_='search_result_row ds_collapse_flag')
    
        for item in appid_row:
            appid.append(item['data-ds-appid'])
    
    return appid


# 영어로 된 달을 숫자로 바꿈
def convert_release_date(release_date_raw):
    mdy = release_date_raw.split()
    
    day = mdy[0]
    month = mdy[1]
    year = mdy[2]

    for month_name, value in {'Jan,': '01', 'Feb,':'02', 'Mar,':'03', 'Apr,':'04', 'May,':'05', 'Jun,':'06', 'Jul,':'07', 'Aug,':'08', 'Sep,':'09', 'Oct,':'10', 'Nov,':'11', 'Dec,':'12'}.items():
        if month == month_name:
            month = value
            break

    release_date = year + '-' + month + '-' + day

    return release_date


# 스팀에서 게임 데이터를 가져옴(title, release_date, homepage, genre, developer, publisher, screenshot)
def get_game_data(appid):
    content_list = []
    num = 1
    for item in appid:
        url = 'http://store.steampowered.com/app/' + str(item)
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                'cookie': 'browserid=1344725717332693116; sessionid=adcfbe925844f84782bd1577; strResponsiveViewPrefs=touch; birthtime=678985201; lastagecheckage=9-July-1991; recentapps=%7B%22271590%22%3A1487220706%7D; timezoneOffset=32400,0; _ga=GA1.2.657082707.1487220674; mature_content=1'
            }
        )

        f = urllib.request.urlopen(req).read().decode('utf-8')
        bs = BeautifulSoup(f, 'lxml')

        title = bs.find('div', class_='apphub_AppName').text
        if Game.objects.filter(title=title).exists():
            print(str(num) + '/' + str(len(appid)))
            num = num + 1
            continue

        release_date = convert_release_date(bs.find('span', class_='date').text)
        homepage_raw = bs.find('a', class_='linkbar', attrs={'rel':'noreferrer'})
        if homepage_raw is not None:
            homepage = homepage_raw['href']
        else:
            homepage = ''

        platforms = []
        if bs.find('span', class_='platform_img win'):
            platforms.append('Windows')
        if bs.find('span', class_='platform_img mac'):
            platforms.append('Mac')
        if bs.find('span', class_='platform_img linux'):
            platforms.append('Linux')

        content_div = bs.find_all('div', class_='page_content')
        for page in content_div:
            if page['class'][0] == 'page_content':
                genres_raw = page.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/genre/[.]*')})
                developers_raw = page.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/search/\?developer[.]*')})
                publishers_raw = page.find_all('a', attrs={"href": re.compile('http://store.steampowered.com/search/\?publisher[.]*')})
                break

        genres = []
        developers = []
        publishers = []
        
        for g in genres_raw:
            genres.append(g.text.strip())

        for d in developers_raw:
            developers.append(d.text.strip())
        
        for p in publishers_raw:
            publishers.append(p.text.strip())

        screenshot = bs.find('a', class_='highlight_screenshot_link')['href'][43:].replace('1920x1080', '600x338')
        

        content = {}
        content['title'] = title
        content['release_date'] = release_date
        content['homepage'] = homepage
        content['platforms'] = platforms.replace(',', ' ')
        content['genres'] = genres.replace(',', ' ')
        content['developers'] = developers.replace(',', ' ')
        content['publishers'] = publishers.replace(',', ' ')
        content['screenshot'] = screenshot

        content_list.append(content)

        print(str(num) + '/' + str(len(appid)))
        num = num + 1
    return content_list


# Game모델 저장(genre, developer, publisher 관계연결), Screenshot모델 저장
def save_object(content):
    for item in content:
        obj, created = Game.objects.update_or_create(
            title = item['title'],
            release_date = item['release_date'],
            homepage = item['homepage'],
        )

        if created == False:
            print('exist already')
            continue

        
        obj.save()

        for platform in item['platforms']:
            temp, created = Platform.objects.get_or_create(name=platform)
            obj.platforms.add(temp)

        for genre in item['genres']:
            temp, created = Genre.objects.get_or_create(name=genre)
            obj.genres.add(temp)

        for developer in item['developers']:
            temp, created = Developer.objects.get_or_create(name=developer)
            obj.developers.add(temp)

        for publisher in item['publishers']:
            temp, created = Publisher.objects.get_or_create(name=publisher)
            obj.publishers.add(temp)

        screenshot = Screenshot.objects.get_or_create(screenshot_url=item['screenshot'], game=obj)

        print('Save object!')

        

        

    


game_list = get_game_data(get_appid_steam(10))
save_object(game_list)