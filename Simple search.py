# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:00:07 2020

@author: Anwar
"""


from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

ID_APP = 'AnwarHsu-sdk-PRD-bc8e89b76-29e8dd8c'

Keywords = input('what are you searching for? (ex: white piano)\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

#input(items[0])  -----> gives us the first item in the seacrh menu 

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
 