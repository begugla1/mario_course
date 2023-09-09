#!/bin/bash

# Start flower app in 5555 port
cd /code/src
celery -A celery_app.celery flower
