"""
Made by Matthew Vanderhoff, @vanderh0ff
"""

import requests
import urllib.parse
import lxml.html

def init():
    se = requests.session()
    se.get("http://carfolio.com/search/results/?")

def get_car_name():
    cartext = input('what car?')
    car = urllib.parse.urlencode({'terms':cartext})
    return [cartext,car]

def query_car_length(carinfo):
    data = se.get("http://carfolio.com/search/results/?"+carinfo[1]+"&offset=0&num=20&makematch=e&modelmatch=e")
    doc = lxml.html.fromstring(data.content)
    cars = doc.xpath('//*[@id="content"]/div[2]/ol/li/dl/dt/a')
    data = se.get("http://carfolio.com"+cars[len(cars)-1].attrib['href'])
    doc = lxml.html.fromstring(data.content)
    length = doc.xpath('//*[@id="content"]/div[3]/table/tbody[2]/tr[6]/td[1]/strong')
    return length[0].textcontent()

def get_route_points():
    origin = input("start point ")
    destination = input("end point ")
    return {
    'origin':origin,
    'destination':destination
    }

def query_route_length(routepoints):
    mapsurl = "http://maps.googleapis.com/maps/api/directions/json?"
    data = se.get(mapsurl+urllib.parse.urlencode(routepoints))
    meters = data.json()['routes'][0]['legs'][0]['distance']['value']
    return meters

def calculate_cars_on_route(routelength, carlength):
    cartimes = routelength / (int(carlength)/1000)


def main():
    init()
    carinfo = get_car_name()
    quert_car_length()
    get_route_points()
    query_route_length()
    calculate_cars_on_route()
    print ('a ', cartext, ' can fit on a route from ', origin, ' to ', destination,\
        ' ', cartimes, ' times.' )
