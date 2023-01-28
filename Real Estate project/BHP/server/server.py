from flask import Flask, request, jsonify
from fontTools.feaLib import location
from flask_cors import CORS, cross_origin

import util
app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    print(util.get_location_names())
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-control-Allow-orgin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    print(request.json)
    req = request.json
    total_sqft = float(req['total_sqft'])
    loaction = req['location']
    bhk = int(req['bhk'])
    bath = int(req['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
