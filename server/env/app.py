from flask import Flask, jsonify, render_template_string, render_template, request
from flask_cors import CORS
from dotenv import dotenv_values
from flask_pymongo import PyMongo 


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}) # Enable CORS

config = dotenv_values(".env")
mongo = PyMongo(app, uri=config["DB_URI"])

@app.route('/login/<username>', methods=['GET'])
def login(username): 
    result = mongo.db.users.find_one_or_404({"username" : username})
    result.pop("_id")
    return result

@app.route('/register', methods=['POST'])
def register(): 
    if request.method != 'POST':
        return 400
    
    content = request.json
    username = content.get('username')
    password = content.get('password')
    newUser = {'username': username, 'password': password}
    result = mongo.db.users.insert_one(newUser)
    return "Created user", 201

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/', methods=['GET'])
def hello_world(): 
    return "<h1> Hello, world! </h1> "

@app.route('/markdown')
def md():
    with open("./env/markdown/sample1.md", "r") as file: 
        md_content = file.read()
    return md_content

if __name__ == '__main__':
    app.run()