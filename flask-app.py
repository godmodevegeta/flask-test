from flask import Flask, request, make_response

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return "You made a GET request\n", 200
    elif (request.method == "POST"):
        return "You made a POST request\n", 201   
    return "<h1>Hello, World!</h1>\n"

@app.route("/hello/")
def hello():   
    response = make_response("Hello World!\n")
    response.status_code = 200
    response.content_type = "text/plain"
    return response

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

