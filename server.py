from flask import Flask 
#import flask 
app = Flask(__name__)

#pip install flask -i https://frs-art.jpmchase.net/artifactory/api/pypi/jpmc-public-pypi/simple/
#Run it like - python server.py
#in browser, open http://127.0.0.1:5000/
@app.route("/") #http://127.0.0.1:5000/  => called API endpoint
def home():
    return """
        <html><body>
        <h1> Hello World </h1>
        </body></html>    
        """
        
from flask import jsonify 
@app.route("/helloj") #http://127.0.0.1:5000/helloj  => called API endpoint
def helloj():
    obj = { "message" : "Hello World" }
    resp = jsonify(obj)
    return resp 
        
        
if __name__ == '__main__':
    app.run() #default port is 5000