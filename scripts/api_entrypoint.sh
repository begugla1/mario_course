#!/bin/bash

cd /code/src
alembic -c migrations/alembic.ini upgrade head
python main.py
