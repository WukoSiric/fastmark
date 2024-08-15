from flask import Flask, jsonify, render_template_string, render_template, request, session
from flask_cors import CORS
from dotenv import dotenv_values
from flask_pymongo import PyMongo 
from datetime import timedelta


# instantiate the app
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}) # Enable CORS

config = dotenv_values(".env")
mongo = PyMongo(app, uri=config["DB_URI"])

@app.route('/register', methods=['POST'])
def register(): 
    content = request.json
    username = content.get('username')
    password = content.get('password')
    newUser = {'username': username, 'password': password}
    result = mongo.db.users.insert_one(newUser)
    return "Created user", 201

@app.route('/login', methods=['POST'])
def login(): 
    content = request.json
    received_username = content.get('username')
    received_password = content.get('password')

    result = mongo.db.users.find_one_or_404({"username" : received_username})
    if result["password"] == received_password:
        # Session data
        session["user"] = received_username
        return jsonify({'message': 'Login successful'}), 200
    else: 
        return jsonify({'message': 'Invalid credentials'}), 401
    

@app.route('/logout')
def logout(): 
    session.clear()
    return "Logged out", 200

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()