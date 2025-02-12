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

@app.route("/login", methods=['GET', 'POST'])
def login():
    # user = request.args["user"]
    # password = request.args["password"]
    # if password == "test1234":
    #     return f"<h2>User {user} successfully logged in!</h2>"
    # return f"<h2>Authentication for user {user} failed!</h2>"
    response = make_response("Please provide login credentials\n")
    if request.method=='POST':
        try:
            data = request.get_json()
            user = data.get('user')
            password = data.get('password')
            if user and password:
                response.data = "Successfully logged in user: {user}\n".format(user=user)
                response.status_code = 200
                return response
        except Exception as e:
            response.data = "Error while parsing JSON\n"
            response.status_code = 400
            return response
    else:
        response.status_code = 400
        return response

@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    response = make_response("hi")
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = data.get('user')
            password = data.get('password')
            if user and password:
                # print ("Created user: {user}\n".format(user=user))
                # response.data = jsonify({"message" : f"Created user: {user}\n"})
                # response.status_code = 201
                create_user(user, password)
                return jsonify({"message" : f"Created user {user}"}), 201
        except Exception as e:
            response.data = jsonify({"message" : "Error while parsing json"})
            response.status_code = 400
            return response
    else:
        response.data = "Please provide User and Password for sign up"
        response.status_code = 400
        return response

def create_user(user, password):
    print (f"found user {user} and password {password}")
    



@app.route("/about")
def about_page():
    return "<p> this is the about page!</p>"

if __name__=='__main__':
    print (sayWhat)
    print ()


