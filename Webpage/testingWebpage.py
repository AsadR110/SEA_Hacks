from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route("/", methods= ["POST", "GET"])
# def homepage():
#     if request.method == "POST" :
#         totalRooms = request.form["rnumber"]
#         return redirect(url_for("totalRooms", usr=totalRooms))
#     else : render_template("roomWebpage.html")

# @app.route("/")
# def homepage():
#     return render_template("index.html")



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
        return render_template("secondPage.html")
    else:
        return render_template("secondPage.html")

@app.route(("/admin"))
def admin():
    return  redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
