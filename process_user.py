from parse_rest.user import User

def signup(username, password):
    u = User.signup(username, password)


def login(username, password):
    u = User.login(username, password)