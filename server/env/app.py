from flask import Flask, jsonify, render_template_string, render_template, request, session, make_response
from flask_cors import CORS, cross_origin
from dotenv import dotenv_values
from flask_pymongo import PyMongo 
from datetime import timedelta
from uuid import uuid4

app = Flask(__name__)
app.config.from_object(__name__)
config = dotenv_values(".env")
app.secret_key = "randomstring"

CORS(app) # Enable CORS
mongo = PyMongo(app, uri=config["DB_URI"])

@app.route('/createDocument', methods=['POST'])
@cross_origin(supports_credentials=True)
def createDocument(): 
    if 'user' not in session: 
        return jsonify({'message': 'Unauthorized'}), 401
    req = request.json
    content = req.get('content')
    title = req.get('title')
    document = {'title': title, 'content': content, 'owner': session.get('user')}
    mongo.db.documents.insert_one(document)
    return jsonify({'message': 'Document created'}), 201

@app.route('/register', methods=['POST'])
def register(): 
    content = request.json
    username = content.get('username')
    password = content.get('password')
    newUser = {'username': username, 'password': password}
    mongo.db.users.insert_one(newUser)
    return "Created user", 201

@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login(): 
    content = request.json
    result = mongo.db.users.find_one_or_404({"username" : content.get('username')})

    if result["password"] == content.get('password'):
        session["user"] = content.get('username')
        session["session_id"] = str(uuid4())
        session.permanent = True
        print(session)
        return jsonify({'message': 'Login successful'}), 200
    else: 
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout')
def logout(): 
    session.clear()
    return "Logged out", 200

@app.route('/sessiondata', methods=['GET'])
@cross_origin(supports_credentials=True)
def sessiondata(): 
    print(session)
    return jsonify(session)

if __name__ == '__main__':
    app.run()