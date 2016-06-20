# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')
url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.urlopen(url).read()

soup = (html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in soup:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
