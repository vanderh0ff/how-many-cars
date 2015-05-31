import requests
import urllib.parse
import lxml.html
se = requests.session()
url = "http://carfolio.com/search/results/?"
cartext = input('what car?')
car = urllib.parse.urlencode({'terms':cartext})
se.get(url)
data = se.get(url+car+"&offset=0&num=20&makematch=e&modelmatch=e")
doc = lxml.html.fromstring(data.content)
cars = doc.xpath('//*[@id="content"]/div[2]/ol/li/dl/dt/a')
data = se.get("http://carfolio.com"+cars[len(cars)-1].attrib['href'])
doc = lxml.html.fromstring(data.content)
length = doc.xpath('//*[@id="content"]/div[3]/table/tbody[2]/tr[6]/td[1]/strong')
length = length[0]
mapsurl = "http://maps.googleapis.com/maps/api/directions/json?"
origin = input("start point ")
destination = input("end point ")
data = se.get(mapsurl+urllib.parse.urlencode({
    'origin':origin,
    'destination':destination
    }))
meters = data.json()['routes'][0]['legs'][0]['distance']['value']
cartimes = meters / (int(length.text_content())/1000)
print ('a ', cartext, ' can fit on a route from ', origin, ' to ', destination,\
    ' ', cartimes, ' times.' )
