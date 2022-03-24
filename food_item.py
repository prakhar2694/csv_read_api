from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
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
 
    # methods go here

api.add_resource(Foods, '/foods')

if __name__ == '__main__':
    app.run()  # run our Flask app