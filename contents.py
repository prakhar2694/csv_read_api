import string
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
from flask_cors import CORS
import ast

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class Contents(Resource):
    def get(self):
        item = request.args.get('item')
        items={'protien':'','carbohydrate':'','fiber':'','water':'','sugar':'','saturated_fat':''}
        food = pd.read_csv('C:\\Users\\SPURGE\\csv_read_api\\food.csv')
        food.columns = [c.replace(' ', '_') for c in food.columns]
        food.columns = [c.replace('.', '_') for c in food.columns]
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        p = food[food['Description'] == item].index.values
        items['protien'] = food.Data_Protein[p].to_string().split()[1]
        items['carbohydrate']=food.Data_Carbohydrate[p].to_string().split()[1]
        items['fiber']=food.Data_Fiber[p].to_string().split()[1]
        items['water']=food.Data_Water[p].to_string().split()[1]
        items['sugar']=food.Data_Sugar_Total[p].to_string().split()[1]
        items['saturated_fat']=food.Data_Fat_Saturated_Fat[p].to_string().split()[1]
        return items
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # methods go here

api.add_resource(Contents, '/contents')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)  # run our Flask app
