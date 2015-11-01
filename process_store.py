__author__ = 'Herb'
from business.Store import Store
from parse_rest.datatypes import GeoPoint



def saveStore(Name, LocationLat, LocationLon, Description, Type):


    store = Store(Name=Name, Description=Description, Location = GeoPoint(latitude=LocationLat, longitude=LocationLon, Type=Type))
    store.save()
    return store

def getStoreByName(storeName):
    store = Store.Query.all().filter(Name=storeName)
    return store
def getStoreById(id):
    store = Store.Query.get(objectId=id)
    return store
def updateStore(id, name, description, LocationLat, LocationLon, Type):

    if (id is not None):
        store = getStoreById(id)
        if (name is not None):
            store.Name = name
        if (description is not None):
            store.Description = description
        if (LocationLat is not None and LocationLon is not None):
            store.Location = GeoPoint(latitude=LocationLat, longitude= LocationLon)
        if (Type is not None):
            store.Type = Type

        store.save()
        return store
    else:
        return None

def deleteStore(id):
    try:
        store = getStoreById(id)
        store.delete()
    except:
        print "Something Went Wrong"
        return False
    return True