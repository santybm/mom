__author__ = 'Herb'
from parse_rest.datatypes import Object

class ShoppingCart(Object):
    pass

def createCart(firstItem):
    return ShoppingCart(cartItems=[firstItem.objectId])

def addItemtoCart(cart, Item):
    c = ShoppingCart.Query.get(objectId=cart.objectId)
    lis = c.cartItems
    lis.append(Item.objectId)
    c.cartItems = lis
    c.save()
    return c

def removeItemFromCart(cart, Item):
    c = ShoppingCart.Query.get(objectId=cart.objectId)
    for item in c.cartItems:
        if item == Item.objectId:
            c.cartItems.remove(item)

    c.save()
    return "successful"

