from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/sensor')
def about():
    return 'Proriro esta bien pendejo men que pendejo men pendejo men que pendejo men pendejo men que pendejo men pendejo men que pendejo men pendejo men que pendejo men pendejo men que pendejo men'
