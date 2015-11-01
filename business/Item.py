__author__ = 'Herb'
from parse_rest.datatypes import Object

class Item(Object):
    pass

def getItem(itemName):
    return Item.Query.all().filter(Name=itemName)