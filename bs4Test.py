# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:40:15 2017

@author: moon
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read())

a = bsObj.h1

print(bsObj.h1)