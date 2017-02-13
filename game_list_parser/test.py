import urllib.request
from bs4 import BeautifulSoup

#online game list
req = urllib.request.Request(
	'https://namu.wiki/w/%EC%98%A8%EB%9D%BC%EC%9D%B8%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D',
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
	}
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('a', class_='wiki-link-internal')

"""
print("########## ONLINE GAME LIST ########")
for item in bs:
	print(item.text)
"""

#mobile game list
req = urllib.request.Request(
	'https://namu.wiki/w/%EB%AA%A8%EB%B0%94%EC%9D%BC%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D',
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
	}
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('ul', class_='wiki-list')

"""
print("########## MOBILE GAME LIST ########")
for item in bs:
	temp = item.find_all('a', class_='wiki-link-internal')
	for item2 in temp:
		print(item2.text)
	
"""


#playstation game list
req = urllib.request.Request(
	'https://namu.wiki/w/%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%85%98/%EA%B2%8C%EC%9E%84%20%EB%AA%A9%EB%A1%9D',
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
	}
)

f = urllib.request.urlopen(req).read().decode('utf-8')

bs = BeautifulSoup(f, 'lxml').find_all('ul', class_='wiki-list')

print("########### PLAYSTATION GAME LIST ########")
for item in bs:
	temp = item.find_all('p')
	for item2 in temp:
		print(item2.text)
