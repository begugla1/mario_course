# Base Dockerfile for all python services: api, celery, flower

FROM python:alpine3.17

RUN mkdir /envs && cd /envs
RUN python -m venv env
RUN chmod +x env/bin/activate
RUN ./env/bin/activate

COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

RUN chmod a+x docker/scripts/*.sh
