#!/bin/bash
cd /code/api
alembic -c migrations/alembic.ini upgrade head
python trading_course/main.py
