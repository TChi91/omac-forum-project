from flask import Flask

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def home():
    return 'Hi there'


@app.route('/sayHello/<username>')
def sayhello(username):
    return 'Hello %s' % username


app.run()