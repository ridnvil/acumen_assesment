import os

from flask import json

# Get all data from json file
def get_customers_from_json():
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    json_path = os.path.join(base_path, '..', 'data/customers.json') 
    
    with open(json_path, 'r') as f:
        return json.load(f)