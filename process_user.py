from parse_rest.user import User
import settings_local

from parse_rest.connection import SessionToken, register
register(settings_local.APPLICATION_ID, settings_local.REST_API_KEY)


def signup(username, password):
    try:
        u = User.signup(username, password)
    except:
        return "User Already Exists"
    return u.sessionToken.token


def login(username, password):
    try:
        u = User.login(username, password)
    except:
        return "Error: User login failed"
    return u.sessionToken.token

def logout():
    try:
        User.logout_user()
    except:
        return "Error"
