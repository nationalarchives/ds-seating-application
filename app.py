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
                zoneID = "quiet"
            else:
                zoneID = "main"
        else:
            zoneID = "group"
        if windowseat == "yes":
            hasLight = 1
        else:
            hasLight = 0
        accessType = accessrequirements

        cur.execute(f"SELECT * FROM seats WHERE zoneID = {zoneID} AND hasLight = {hasLight} AND accessType = {accessType}") 

        con.close()
        return render_template("recommended.html", researchingbyself = researchingbyself, quietzone= quietzone, windowseat= windowseat, accessrequirements = accessrequirements)
    else:
        return render_template("helpchoosing.html", request=request)



@app.route('/seatselect')
def seatselect():
    return render_template("seatselect.html")

