import urllib2
import xml.etree.ElementTree as ET
#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_42.xml'

sum = 0
while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    # url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('count')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location






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


