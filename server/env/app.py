from flask import Flask, jsonify, render_template_string, render_template, request, session, make_response
from flask_cors import CORS, cross_origin
from dotenv import dotenv_values
from flask_pymongo import PyMongo 
from uuid import uuid4
from bson import ObjectId

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
    result = mongo.db.documents.insert_one(document)
    return jsonify({'_id': str(result.inserted_id), 'message': 'Document created'}), 201

@app.route('/viewDocuments', methods=['GET'])
@cross_origin(supports_credentials=True)
def viewDocuments(): 
    if 'user' not in session: 
        return jsonify({'message': 'Unauthorized'}), 401
    
    userDocuments = mongo.db.documents.find({'owner': session['user']})
    userDocList = []

    for doc in userDocuments: 
        doc['_id'] = str(doc['_id'])
        userDocList.append(doc)

    return jsonify(userDocList), 200

@app.route('/getDocument/<document_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def getDocument(document_id): 
    if 'user' not in session: 
        return jsonify({'message': 'Must be logged in'}), 401

    document_id = ObjectId(document_id)
    document = mongo.db.documents.find_one({'_id': document_id})

    if document is None: 
        return jsonify({'message': 'Document not found'}), 404

    document['_id'] = str(document['_id'])
    return jsonify(document), 200

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