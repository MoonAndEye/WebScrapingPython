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
#這個是最基本的網頁 有 h1 h2 body 等

#target = "http://www.pythonscraping.com/pages/warandpeace.html"
#這個是練其他 tag 像是 <span class="green"></span>

target = "http://www.pythonscraping.com/pages/page3.html"


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
#print (bsObj)

a = []
b = []
c = []

for child in bsObj.find("table", {"id": "giftList"}).children:
    #這 child 只有子代,所以只有物品的名稱
    a.append(child)
    print(child)



for descendant in bsObj.find("table", {"id": "giftList"}).descendants:
    #這 descendant 是子孫,除了物品,img 標籤 span 標籤 都會有
    b.append(descendant)
    print(descendant)
    
    
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    # 平輩
    c.append(sibling)
    print(sibling)