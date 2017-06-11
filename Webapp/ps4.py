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
    driver = webdriver.Chrome()
    for item in appid:
        driver.get('http://www.playstation.co.kr' + item)
        detail = driver.page_source

        bs = BeautifulSoup(detail, 'lxml')
        title = bs.find('h3', class_='title').text
        ul = bs.find('ul', class_='floatL spec_txt').find_all('li')
        developer = ul[0].text.split(' : ')[1]
        publisher = ul[1].text.split(' : ')[1]
        genre = ul[2].text.split(' : ')[1]
        release_date = ul[3].text.split(' : ')[1]

        print(title)
        print(developer)
        print(publisher)
        print(genre)
        print(release_date)

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

get_detail(get_appid_ps4(2))
#print(get_appid_ps4(2))