from flask import Flask
app = Flask(__name__)

login = False

@app.route('/')
def hello_world():
    return 'Hello, World! 3'

@app.route('/login')
def login():
    login = True
    return 'Logged in'

@app.route('/secret')
def secret():
    if login:
        return 'secret!!'
    return 'Forbidden'
