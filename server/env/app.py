from flask import Flask, jsonify, render_template_string, render_template
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

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