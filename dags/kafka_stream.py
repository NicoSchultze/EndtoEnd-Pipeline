"""
File: kafka_stream.py
Author: Nico
Date: 5.3.2024
Description: DAG will be run from this file.
"""
from datetime import datetime

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
import json

# Define default arguments for the DAG
default_args = {
    'owner':'nico',
    'start_date':datetime(2024, 3, 5, 23, 30)
}

# Function to fetch data from an API
def get_data():
    # Making a GET request to the API endpoint
    res = requests.get("https://randomuser.me/api/")
    # Converting the response to JSON format
    res = res.json()
    # Extracting the first result from the response
    res = res['results'][0]
    return res

# Function to format data fetched from the API
def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

# Function to stream formatted data
def stream_data():
    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent=3))


stream_data()
