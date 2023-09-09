#!/bin/bash

# Run latest migrations
cd /code
alembic upgrade head

# Run main file
cd src
python main.py
