from parse_rest.user import User
import settings_local
from business.ShoppingCart import ShoppingCart
from parse_rest.connection import *
from business.ShoppingCart import *
register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)


def signup(username, password):
    try:
        u = User.signup(username, password)
        sc = ShoppingCart(cartItems=[])
        sc.save()
        u.shoppingCart = sc
        u.save()
    except:
        return "User Already Exists"
    return u


def login(username, password):
    try:
        u = User.login(username, password)
    except:
        return "Error: User login failed"
    return u

def logout():
    try:
        User.logout_user()
    except:
        return "Error"
