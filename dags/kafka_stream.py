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

default_args = {
    'owner':'nico',
    'start_date':datetime(2024, 3, 5, 23, 30)
} # will be used to be attached to the DAG (who owns the project, etc)

def stream_data():
    import json

    res = requests.get("https://randomuser.me/api/")
    res.json()
    print(res.json())

stream_data()
