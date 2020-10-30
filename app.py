from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/help-choosing')
def helpchoosing():
    return render_template("helpchoosing.html")

@app.route('/seat-select')
def seatselect():
    return render_template("seatselect.html")

#@app.route("/does-not-know-if-help-choosing-seat-is-needed")
#def idontknowhelp():
#    return render_template("idontknowhelp.html")
