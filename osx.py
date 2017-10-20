#!python2
import urllib
import os
import ctypes
import imghdr
from datetime import datetime
from bs4 import BeautifulSoup
import requests

url = 'http://fuckinghomepage.com/rss'
sourceCode = requests.get(url)
plainText = sourceCode.text
soup = BeautifulSoup(plainText, 'lxml')

data = soup.item.description.text
href = data.split('PICTURE OF THE DAY:')[1].split('href=')[1].split('target=')[0]
href = href.replace('\"', ' ').strip()

today = datetime.now()
files = os.listdir(os.getcwd())

dateString = str(today.day)+'-'+str(today.month)+'-'+str(today.year)
prev = str(today.day-1)+'-'+str(today.month)+'-'+str(today.year)

if not os.path.exists(dateString):
    urllib.urlretrieve(href, dateString)
    from appscript import app, mactypes
    app('Finder').desktop_picture.set(mactypes.File(dateString))
    print "Wallpaper set successfully"
