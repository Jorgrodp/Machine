#!/usr/bin/python

from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment import predict_proba
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

api = Api(
    app, 
    version='1.0', 
    title='Phishing Prediction API',
    description='Phishing Prediction API')

ns = api.namespace('predict', 
     description='Phishing Classifier')
   
parser = api.parser()

parser.add_argument(
    'URL', 
    type=str, 
    required=True, 
    help='URL to be analyzed', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        data = []

        for year in range(2000, 2024):
            value = random.uniform(80, 130)  # Generating a random value between 80 and 130
            data.append({"Year": year, "Value": value})

        json_data = json.dumps(data, indent=4)

        return json_data, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
