from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/sayHello/<username>')
def sayhello(username):
    return 'Hello {}' .format(username)


app.run()