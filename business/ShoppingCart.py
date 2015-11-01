__author__ = 'Herb'
from parse_rest.datatypes import Object

class ShoppingCart(Object):
    pass

def createCart(firstItem):
    return ShoppingCart(cartItems=[firstItem.objectId])

def addItemtoCart(cart, Item):
    c = ShoppingCart.Query.get(objectId=cart.objectId)
    c.cartItems.append(Item.objectId)
    c.save()
    return c


