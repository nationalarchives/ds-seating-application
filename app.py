from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("startscreen.html")

@app.route('/termsandconditions')
def termsandconditions():
    return render_template("termsandconditions.html")

@app.route('/readersnumber', methods=["GET","POST"])
def readersnumber():
    if request.method == "POST":
        givenReaders = request.form["readersnumber"]
        try:
            int(givenReaders)
        except:
            return render_template("readersnumber.html", errorMessage="Invalid reader's number: invalid format")
        if len(givenReaders) != 6:
            return render_template("readersnumber.html", errorMessage="Invalid reader's number: invalid format")

        con = sqlite3.connect('readersnumber.db')
        cur = con.cursor()
        readersSearch = cur.execute(f"SELECT * FROM readers WHERE readersNumber={givenReaders}").fetchall()
        con.close()

        if len(readersSearch) == 0:
            return render_template("readersnumber.html", errorMessage="Invalid reader's number: reader's number not found")

        global readersNumber
        readersNumber = readersSearch[0][0]
        global readersName
        readersName = readersSearch[0][1]
        
        return render_template("home.html")
    return render_template("readersnumber.html", errorMessage="")

def getSeatLength(seatList):
    count = 0
    for i in seatList:
        count += 1
    return count

@app.route('/seatchosen', methods=["POST"])
def seatchosen():
    bookedSeat = request.form["seat"]

    con = sqlite3.connect('seatbooking.db')
    cur = con.cursor()
    cur.execute(f"UPDATE seats SET isBooked=1 WHERE seatID='{bookedSeat}'")
    cur.execute(f"UPDATE seats SET bookingHolder={readersNumber} WHERE seatID='{bookedSeat}'")
    con.commit()
    con.close()

    con2 = sqlite3.connect('readersnumber.db')
    cur2 = con2.cursor()
    cur2.execute(f"UPDATE readers SET readersSeatID='{bookedSeat}' WHERE readersNumber={readersNumber}")
    cur2.execute(f"UPDATE readers SET hasBooking=1 WHERE readersNumber={readersNumber}")
    con2.commit()
    con2.close()

    return render_template("confirmation.html", userSeat=bookedSeat)


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

        availableSeats = cur.execute(f"SELECT * FROM seats WHERE roomID='{roomID}' AND zoneID='{zone}' AND hasLight={hasLight} AND accessType='{accessType}' AND isBooked=0").fetchall()
        
        count = getSeatLength(availableSeats)
        while count == 0:
            availableSeats = cur.execute(f"SELECT * FROM seats WHERE roomID='{roomID}' AND zoneID='{zone}' AND accessType='{accessType}' AND isBooked=0").fetchall()
            count = getSeatLength(availableSeats)
            if count == 0:
                availableSeats = cur.execute(f"SELECT * FROM seats WHERE roomID='{roomID}' AND accessType='{accessType}' AND isBooked=0").fetchall()
                count = getSeatLength(availableSeats)
                if count == 0:
                    availableSeats = cur.execute(f"SELECT * FROM seats WHERE roomID='{roomID}' AND isBooked=0").fetchall()
                    count = getSeatLength(availableSeats)
                    if count == 0:
                        return render_template("noseats.html")
                
        randomSeat = availableSeats[random.randint(0, count-1)]
        
        selectedSeat = randomSeat[0]
        selectedRoom = randomSeat[2]
        selectedZone = randomSeat[3]

        con.close()
        return render_template("recommended.html", seatID = selectedSeat, roomID = selectedRoom, zoneID = selectedZone)
    else:
        return render_template("helpchoosing.html", request=request)