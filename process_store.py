__author__ = 'Herb'
from business.Store import Store
from parse_rest.datatypes import GeoPoint



def saveStore(Name, LocationLat, LocationLon, Description, Type):


    store = Store(Name=Name, Description=Description, Location = GeoPoint(latitude=LocationLat, longitude=LocationLon))
    store.save()



    return store