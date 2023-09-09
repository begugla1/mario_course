#!/bin/bash

cd /code/src
celery -A celery_app.celery worker --loglevel=INFO
