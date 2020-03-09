from flask import Flask, request, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    return json_response([{"name":"Hello World!"}])

def json_response(payload, status=200):
     return (json.dumps(payload), status, {'content-type': 'application/json'})