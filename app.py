from flask import Flask, session
app = Flask(__name__)

import settings_local
from parse_rest.connection import *
from parse_rest.datatypes import GeoPoint
import process_user
import process_store
import process_item
from flask import request

from business.Item import *
from business.ShoppingCart import *



register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)

currentUser = None


@app.route('/')
def hello():
    return "Hello World"


### USER ROUTES ###

@app.route('/register')
def uregister():
    username = "demo77"
    password = "abcd123"
    u = process_user.signup(username, password)
    if u != 'User Already Exists':
        session['token'] = u.session_header()['X-Parse-Session-Token']
        return u.username
    return "Can not register user"


@app.route('/login')
def ulogin():
    username = 'demo6'
    password = "abcd123"
    u = process_user.login(username, password)
    session['token'] = u.session_header()['X-Parse-Session-Token']


    return u.objectId

@app.route('/logout')
def ulogout():
    process_user.logout()
    session['token'] = None
    return "Logout Successful"


### GROCERY CART ###

@app.route('/addToCart')
def addCart():
    itemToAdd = getItem("Slim Milk")

    #Is user logged in?
    if 'token' in session and session['token'] is not None:
        register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY, session_token=session['token'])
        try:
            currentUser = process_user.User.current_user()
            #currentUser = process_user.User.Query.get(objectID=currentUser)
        except Exception as exp:
            return exp.message
        cart = currentUser.shoppingCart
        addItemtoCart(cart, itemToAdd)


        return "User Logged in"

    else:
        return "Not logged in"


@app.route('/store')
def addStore():

    savedStore = process_store.saveStore(Name="Nike", Description="Basic hoe's shop at these Joes", LocationLat=12, LocationLon= -34, Type="")

    return savedStore.objectId
@app.route('/item')
def addItem():

    try:
        homeStore = process_store.getStoreByName("Nike").get()
        id = process_item.saveItem(name="Tequila", description="Amarga", price = 10, store=homeStore, quantity = 4, unitPrice= 3.99)
    except Exception as es:
        print es
    return id.objectId

@app.route('/removeitemCart')
def rmCartItem():
    cart = currentUser.shoppingCart
    item = process_item.getItemByName("Slim Milk").get()
    removeItemFromCart(cart, item.get())
    return "done"

@app.route('/searchClosest')
def searchItem():
    zipcode = request.args.get('Zipcode')
    radiusInMi = request.args.get('Radius')
    Location = process_item.findItemNearestTo(Zipcode= zipcode, Radius =radiusInMi)
    #Lat [0] Long [1]
    #zip = str(Location[0]) + ":"+ str(Location[1])
    return str(Location)

if __name__ == '__main__':
    app.secret_key = 'A0Z=-(0a-/dfhg$%##@ew4rfwc[}{}>#@$>:SKF$%!'
    app.run();
