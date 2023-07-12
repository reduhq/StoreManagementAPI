#! /usr/bin/env bash

# Run the migrations
./wait-for-it.sh db:5432 -s -- python /StoreManagementAPI/StoreManagementAPI/manage.py migrate

# Run the api
exec python /StoreManagementAPI/StoreManagementAPI/manage.py runserver 0.0.0.0:8000