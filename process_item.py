__author__ = 'Herb'
from business import Item

def saveItem(Name, Description, Store, Price):
    item = Item(Name=Name, Description=Description, Store=Store, Price=Price)
    item.save()
    return item._get_object_id
