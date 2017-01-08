# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:40:15 2017

@author: moon
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""
#最簡單的 BeautifulSoup 指令
"""

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return ("HTTP Error")
        
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return ("ATTribute Error")
    return title

#target = "http://www.pythonscraping.com/pages/page1.html"
target = "http://www.pythonscraping.com/pages/warandpeace.html"
"""
html = urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(), "lxml")
"""

#print(bsObj.h1)
#print(bsObj.div)

html = urlopen(target)
bsObj = BeautifulSoup(html, "lxml")


nameList = bsObj.findAll("span", {"class":"green"})

"""
for name in nameList:
    print(name.get_text())
    
"""
print (bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"}))

