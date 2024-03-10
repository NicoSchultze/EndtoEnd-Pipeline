#!/bin/bash
set -e
# first line specifies that this script isa interpreted by bash
# 'set -e' tells shell to exit if any command ends with a non zero value

if [ -e "/opt/airflow/requirements.txt" ]; then
  # if requirements.txt exists in airflow update pip with the python interpreter from path
  # and also install the requirements in the users home directory
  $(command python) pip install --upgrade pip
  $(command -v pip) install --user -r requirements.txt
fi

if [ ! -f "/opt/airflow/airflow.db" ]; then
  # check if airflow.db does not exist
  airflow db init &&
  # if so initialize the metadata db
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
  # and create an admin user
fi

$(command -v airflow) db upgrade
# upgrade database schema

exec airflow webserver
# start server
