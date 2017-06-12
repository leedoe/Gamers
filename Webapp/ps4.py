import urllib.request
import requests
import codecs
import re
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"reviewer.settings")

import django
django.setup()
from Gamers.models import Game, Developer, Genre, Publisher, Platform, Screenshot


# stroe.steampowered 페이지에 있는 게임 목록을 가져옴
def get_appid_ps4(pages):
    page_number = pages
    appid = []

    driver = webdriver.Chrome()
    driver.get('http://www.playstation.co.kr/game/ps4')

    for i in range(2, page_number+2):
        html = driver.page_source

        bs = BeautifulSoup(html, 'lxml')
        games = bs.find_all('div', class_='game_disc')
        for item in games:
            appid.append(item.find('a')['href'])

        driver.execute_script('goPage('+str(i)+');')
        #time.sleep(1)

    return appid


def get_detail(appid):
    contents = []
    driver = webdriver.Chrome()
    for item in appid:
        driver.get('http://www.playstation.co.kr' + item)
        detail = driver.page_source

        bs = BeautifulSoup(detail, 'lxml')
        title = bs.find('h3', class_='title').text.replace(',', ' ')
        ul = bs.find('ul', class_='floatL spec_txt').find_all('li')
        developer = ul[0].text.split(' : ')[1].replace(',', ' ')
        publisher = ul[1].text.split(' : ')[1].replace(',', ' ')
        genre = ul[2].text.split(' : ')[1].replace(',', ' ')
        release_date = ul[3].text.split(' : ')[1][:10]

        content = {
            'title': title,
            'developer': developer,
            'publisher': publisher,
            'genre': genre,
            'release_date': release_date
        }

        contents.append(content)

    return contents
        

    """
    game = bs.find('div',class_='game_disc')
    driver.get('http://www.playstation.co.kr' + game.find('a')['href'])

    detail = driver.page_source

    bss = BeautifulSoup(detail, 'lxml')
    print(bss.find('div', class_='spec'))
    """
    """
    driver.execute_script('goPage('+str(i)+');')
    i = i + 1
    time.sleep(2)

    html = driver.page_source

    bs = BeautifulSoup(html, 'lxml')
    games = bs.find_all('div', class_='game_disc')
    for item in games:
        print(item.find('h5').text)

        print(item.find('p').text)
    """

def save_data(content):
    for item in content:
        title = item['title']
        developer = item['developer']
        publisher = item['publisher']
        genre = item['genre']
        release_date = item['release_date']
        platform = Platform.objects.get(name='PS4')

        obj, created = Game.objects.update_or_create(
            title = title,
            release_date = release_date,
        )

        if created == False:
            print('exist already')
            continue
        else:
            obj.save()

        temp, created = Developer.objects.get_or_create(name=developer)
        obj.developers.add(temp)

        temp, created = Publisher.objects.get_or_create(name=publisher)
        obj.publishers.add(temp)

        temp, created = Genre.objects.get_or_create(name=genre)
        obj.genres.add(temp)

        obj.platforms.add(platform)

        print('Save object!!')


    


content = get_detail(get_appid_ps4(5))
save_data(content)
#print(get_appid_ps4(2))