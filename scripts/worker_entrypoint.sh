#!/bin/bash

cd /code/src/api
celery -A celery_app.celery worker --loglevel=INFO
