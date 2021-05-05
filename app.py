from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("startscreen.html")

@app.route('/termsandconditions')
def termsandconditions():
    return render_template("termsandconditions.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/helpchoosing', methods=["GET","POST"])
def helpchoosing():
    return render_template("helpchoosing.html", request=request)


@app.route('/seatselect')
def seatselect():
    return render_template("seatselect.html")

