#!/bin/bash
cd /code/trading_course
alembic -c migrations/alembic.ini upgrade head
python api/main.py
