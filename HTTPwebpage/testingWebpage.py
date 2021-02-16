from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/page2")
def home():
    title = "Rooms"
    paragraph = ["Here's where I'm entering all the cool stuff", "This is the first part", "This is the second part"]
    return render_template("testingLogic.html", title = title, paragraph = paragraph)


@app.route("/", methods = ["POST", "GET"])
def mainpage():
    if request.method == "POST":
        rNum = request.form["roomNums"]
        return redirect(url_for("secondPage"))
    else:
        return render_template("firstPage.html")

@app.route("/<total>")
def rNums(total):
    return  f"<h1>{total}</h1>"

@app.route("/Room-Type", methods = ["POST", "GET"])
def secondPage():
    if request.method == "POST":
        rType = request.form["roomType"]
        if rType == "fcorner":
            return redirect(url_for("fCorners"))
        elif rType == "scorner":
            return redirect(url_for("sCorners"))
    else:
        return render_template("secondPage.html")

@app.route(("/admin"))
def admin():
    return  redirect(url_for("home"))

@app.route("/Four-Corners")
def fCorners():
    return  render_template("fourCorners.html")

@app.route("/Six-Corners")
def sCorners():
    return  render_template("sixCorners.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
