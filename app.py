from flask import Flask, session
app = Flask(__name__)

import settings_local
from parse_rest.connection import *
from parse_rest.user import User
from parse_rest.datatypes import GeoPoint
import process_user
import process_store
import process_item
from process_store import Store



register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)


@app.route('/')
def hello():
    return "Hello World"


### USER ROUTES ###

@app.route('/register')
def uregister():
    username = "demo7"
    password = "abcd123"
    u = process_user.signup(username, password)
    session['token'] = u.session_header()['X-Parse-Session-Token']

    return u.username


@app.route('/login')
def ulogin():
    username = 'demo'
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

    #Is user logged in?
    if session['token']:
        return "User Logged in"
    else:
        return "Not logged in"


@app.route('/store')
def addStore():

    savedStore = process_store.saveStore(Name="Trader Joe's", Description="Basic hoe's shop at these Joes", LocationLat=12, LocationLon= -34, Type="")

    return savedStore.objectId
@app.route('/item')
def addItem():
    homeStore = Store.Query.get(Name= "Trader Joe's")
    id = process_item.saveItem(Name="Tequila", Description="How bad bitches drown their sorrows", Store=homeStore, Price = 10)
    return id



if __name__ == '__main__':
    app.secret_key = 'A0Z=-(0a-/dfhg$%##@ew4rfwc[}{}>#@$>:SKF$%!'
    app.run();
