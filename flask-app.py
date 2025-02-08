from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():   
    return "<h1>Hello, World!</h1>"

@app.route("/greet/<name>")
def greet(name):   
    return f"<h1>Hello, {name}!</h1>"

@app.route("/login")
def login():
    user = request.args["user"]
    password = request.args["password"]
    if password == "test1234":
        return f"<h2>User {user} successfully logged in!</h2>"
    return f"<h2>Authentication for user {user} failed!</h2>"

@app.route("/about")
def about_page():
    return "<p> this is the about page!</p>"

