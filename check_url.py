import urllib2
from bs4 import BeautifulSoup

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_245044.html'
htm = urllib2.urlopen(url).read()
soup = BeautifulSoup(htm)
spans = soup.find_all('span')
sum =0
for i in spans:
    sum = sum + int(i.string)
print 'sum = ', sum
    # print i.get('class', None), 'bla\\'
#
# pairs = soup.get_text()
# a= list()
# a = pairs.split()
# for str in a:
#     print  re.findall('\d', str)