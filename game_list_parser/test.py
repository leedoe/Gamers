# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}
req = urllib.request.Request(
	'https://namu.wiki/w/%EC%98%A8%EB%9D%BC%EC%9D%B8%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D',
	data=None,
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
	}
)
# u = urllib.request.urlopen("https://namu.wiki/w/%EC%98%A8%EB%9D%BC%EC%9D%B8%20%EA%B2%8C%EC%9E%84/%EB%AA%A9%EB%A1%9D", header = headers)
f = urllib.request.urlopen(req)
f = f.read()

print(f)
