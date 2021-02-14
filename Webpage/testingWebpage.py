from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("roomWebpage.html")



@app.route("/page2")
def home():
    title = "Rooms"
    paragraph = ["Here's where I'm entering all the cool stuff", "This is the first part", "This is the second part"]
    return render_template("testingLogic.html", title = title, paragraph = paragraph)


# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")

# @app.route("/<usr>")
# def user(usr):
#     return  f"<h1>{usr}</h1>"





@app.route(("/admin"))
def admin():
    return  redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
