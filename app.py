from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/seat-select')
def seatselect():
    return render_template("seatselect.html")

@app.route('/idk-help')
def idkhelp():
    return render_template("idkhelp.html")
