from flask import Flask, session
app = Flask(__name__)

import settings_local
from parse_rest.connection import *
import process_user


register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)

currentUser = None


@app.route('/')
def hello():
    return "Hello World"


### USER ROUTES ###

@app.route('/register')
def uregister():
    username = "demo5"
    password = "abcd123"
    u = process_user.signup(username, password)
    if u != 'User Already Exists':
        session['token'] = u.session_header()['X-Parse-Session-Token']
        return u.username
    return "Can not register user"


@app.route('/login')
def ulogin():
    username = 'demo5'
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
    if 'token' in session and session['token'] is not None:
        register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY, session_token=session['token'])
        try:
            currentUser = process_user.User.current_user()
            
        except Exception as exp:
            return exp.message

        return "User Logged in"

    else:
        return "Not logged in"






if __name__ == '__main__':
    app.secret_key = 'A0Z=-(0a-/dfhg$%##@ew4rfwc[}{}>#@$>:SKF$%!'
    app.run();
