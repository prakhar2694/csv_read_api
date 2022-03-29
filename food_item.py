from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from flask_cors import CORS
import ast

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class Foods(Resource):
	def get(self):
		food=pd.read_csv('C:\\Users\\hi\\Downloads\\food.csv')
		food.columns = [c.replace(' ', '_') for c in food.columns]
		food.columns = [c.replace('.', '_') for c in food.columns]
		pd.set_option('display.max_columns', None)
		pd.set_option('display.max_rows', None)
		a=food.Description
		b=a.tolist()
		return b
	@app.after_request
	def after_request(response):
  		response.headers.add('Access-Control-Allow-Origin', '*')
  		response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  		response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  		return response
 
    # methods go here

api.add_resource(Foods, '/foods')


if __name__ == '__main__':
    app.run()  # run our Flask app