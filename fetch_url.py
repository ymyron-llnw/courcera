import urllib
from bs4 import BeautifulSoup

linkNum = int(raw_input('Link number:')) -1 #since in soup count starts from 0
repeatNum = int(raw_input('Times to repeat fetch:'))


# starturl = raw_input('URI to fetch:')
starturl = 'http://python-data.dr-chuck.net/known_by_Tehzeeba.html'
i = 1
while i <= repeatNum :
    htm = urllib.urlopen(starturl)
    soup = BeautifulSoup(htm)
    starturl = soup('a')[linkNum]['href']
    print 'Fetching:', starturl
    name = soup('a')[linkNum].string
    i = i+1

print name