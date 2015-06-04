"""
Made by Matthew Vander Hoff, @vanderh0ff
"""

import requests
import urllib.parse
import lxml.html

def init():
    se = requests.session()
    se.get("http://carfolio.com/search/results/?")
    return se

def get_car_name():
    cartext = input('what car?')
    car = urllib.parse.urlencode({'terms':cartext})
    return [cartext,car]

def query_car_length(se, car):
    data = se.get("http://carfolio.com/search/results/?"+car+"&offset=0&num=20&makematch=e&modelmatch=e")
    doc = lxml.html.fromstring(data.content)
    cars = doc.xpath('//*[@id="content"]/div[2]/ol/li/dl/dt/a')
    data = se.get("http://carfolio.com"+cars[len(cars)-1].attrib['href'])
    doc = lxml.html.fromstring(data.content)
    length = doc.xpath('//*[@id="content"]/div[3]/table/tbody[2]/tr[6]/td[1]/strong')
    return length[0].text_content()

def get_route_points():
    origin = input("start point ")
    destination = input("end point ")
    return {
    'origin':origin,
    'destination':destination
    }

def query_route_length(routepoints):
    mapsurl = "http://maps.googleapis.com/maps/api/directions/json?"
    data = requests.get(mapsurl+urllib.parse.urlencode(routepoints))
    meters = data.json()['routes'][0]['legs'][0]['distance']['value']
    return meters

def calculate_cars_on_route(routelength, carlength):
    return routelength / (int(carlength)/1000)


def main():
    se = init()
    carinfo = get_car_name()
    carlength = query_car_length(se, carinfo[1])
    routepoints = get_route_points()
    routelength = query_route_length(routepoints)
    cartimes = calculate_cars_on_route(routelength, carlength)
    print ('a ', carinfo[0], ' can fit on a route from ', routepoints['origin'], ' to ', routepoints['destination'],\
        ' ', cartimes, ' times.' )
if __name__ == "__main__":
    main()
