FROM python:alpine3.17

COPY . /code
WORKDIR /code

RUN python -m venv env
RUN chmod +x env/bin/activate
RUN ./env/bin/activate
RUN pip install -r requirements.txt

RUN chmod a+x scripts/api_entrypoint.sh
ENTRYPOINT [ "sh", "scripts/api_entrypoint.sh" ]
