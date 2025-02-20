from flask import Flask, request, make_response, jsonify

app = Flask(__name__, template_folder="templates")
sayWhat = "hi, accessing var above"

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


