from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"

@app.route('/login')
def mei():
    return "Hello Inna"

@app.route('/kristel')
def mek():
    return "Hello Kristel"


if __name__ == '__main__':
    app.run();
