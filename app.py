from flask import Flask, session
app = Flask(__name__)

import settings_local
from parse_rest.connection import SessionToken, register
from parse_rest.user import User
import process_user


register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)


@app.route('/')
def hello():
    return "Hello World"


### USER ROUTES ###

@app.route('/register')
def uregister():
    username = "demo5"
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






if __name__ == '__main__':
    app.secret_key = 'A0Z=-(0a-/dfhg$%##@ew4rfwc[}{}>#@$>:SKF$%!'
    app.run();
