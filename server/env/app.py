from flask import Flask, jsonify, render_template_string, render_template
from flask_cors import CORS
import markdown2

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
    md_content =  """
        # Testing
        ## Its going well
        ### This is my test
        """
    html_content = markdown2.markdown_path("./env/markdown/sample1.md", extras=["fenced-code-blocks", "markdown-in-html"])
    return render_template('index.html', content=html_content)

if __name__ == '__main__':
    app.run()