
__author__ = 'Herb'

from business.Item import Item
from parse_rest.datatypes import GeoPoint
from business.Store import Store
import settings_local
import requests
import json
import math
import httplib,urllib
def saveItem(name, description, price, store, quantity, unitPrice):

    item = Item(Name=name, Description=description, Price=price, Store = store, Quantity=quantity, UnitPrice= unitPrice)
    item.save()
    return item

def getItemById(id):
    item = Item.Query.get(objectId=id)
    return item
def getItemByName(itemName):
    return Item.Query.all().filter(Name=itemName)

def updateItem(id, name, description, price, store, quantity, unitPrice):

    if (id is not None):
        item = Item.Query.get(objectId = id)
        if (name is not None):
            item.Name = name
        if (description is not None):
            item.Description = description
        if (price is not None):
            item.Price = price
        if (store is not None):
            item.Store = store
        if (quantity is not None):
            item.Quantity = quantity
        if (unitPrice is not None):
            item.UnitPrice = unitPrice
        item.save()
        return item
    else:
        return None


def deleteItem(id):
    try:
        item = getItemById(id)
        item.delete()
    except:
        print "Something Went Wrong"
        return False
    return True
def findItemNearestTo(Zipcode, Radius):
    LocationLatAndLong = getLongitudeAndLatitudeFromZipCode(Zipcode)
    latDegree = (float(Radius) / 177.77)
    y1 = LocationLatAndLong[0] + latDegree
    y2 = LocationLatAndLong[0] - latDegree
    longitude1= LocationLatAndLong[1] + 177.77 * math.cos(y1)
    longitude2= LocationLatAndLong[1] + 177.77 * math.cos(y2)
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"where":json.dumps({
       "location": {
         "$nearSphere": {
           "__type": "GeoPoint",
           "latitude": 12.0,
           "longitude": -33.0
         },
         "$maxDistanceInMiles": 100.0
       }
     })})
    connection.connect()
    connection.request('GET', '/1/classes/Store?%s' % params, '', {
       "X-Parse-Application-Id": settings_local.APPLICATION_ID,
       "X-Parse-REST-API-Key": settings_local.REST_API_KEY
     })
    result = json.loads(connection.getresponse().read())



    return (y1, longitude1, y2, longitude2)

def getLongitudeAndLatitudeFromZipCode(Zipcode):
    response = requests.request("GET", "http://dev.virtualearth.net/REST/v1/Locations/US/-/"+Zipcode+"/-/-?o=json&key=" + settings_local.BING_API_KEY)
    longitude = None
    latitude = None
    if (response.status_code is 200):
            json_response = json.loads(response.text)
            longitude = json_response['resourceSets'][0]['resources'][0]['point']['coordinates'][0]
            latitude  =  json_response['resourceSets'][0]['resources'][0]['point']['coordinates'][1]
    return (longitude, latitude)