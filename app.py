from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import random

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
    if request.method == "POST":
        researchingbyself = request.form["researchingbyself"]
        try:
            quietzone = request.form["quietzone"]
        except:
            quietzone = "no"
        windowseat = request.form["windowseat"]
        accessrequirements = request.form["accessrequirements"]

        con = sqlite3.connect('seatbooking.db')
        cur = con.cursor()

        roomID = "main"

        if researchingbyself == "yes":
            if quietzone == "yes":
                zone = "quiet"
            else:
                zone = "main"
        else:
            zone = "group"
        if windowseat == "yes":
            hasLight = 1
        else:
            hasLight = 0
        accessType = accessrequirements


        availableSeats = cur.execute(f"SELECT * FROM seats WHERE zoneID='{zone}' AND hasLight={hasLight} AND accessType='{accessType}' AND isBooked=0").fetchall()
        
        count = 0
        for i in availableSeats:
            count += 1
        randomSeat = availableSeats[random.randint(0, count-1)]

        selectedSeat = randomSeat[0]
        selectedRoom = randomSeat[2]
        selectedZone = randomSeat[3]

        con.close() 
        return render_template("recommended.html", seatID = selectedSeat, roomID = selectedRoom, zoneID = selectedZone)
    else:
        return render_template("helpchoosing.html", request=request)



@app.route('/seatselect')
def seatselect():
    return render_template("seatselect.html")

