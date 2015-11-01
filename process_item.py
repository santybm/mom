__author__ = 'Herb'
from business.Item import Item

def saveItem(name, description, price, store, quantity, unitPrice):

    item = Item(Name=name, Description=description, Price=price, Store = store, Quantity=quantity, UnitPrice= unitPrice)
    item.save()
    return item

def getItemById(id):
    item = Item.Query.get(objectId=id)
    return item

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
