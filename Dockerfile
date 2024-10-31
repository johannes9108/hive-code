FROM python:3-slim

WORKDIR /usr/src/app
USER root

RUN apt update
RUN apt install -y tree
RUN pip install pipenv

# COPY /container/ ./
COPY data/version.txt ./data/version.txt
COPY hiveMod/ ./hiveMod/
COPY tests/ ./tests/
COPY Pipfile ./

RUN pipenv --python $(which python)
RUN pipenv install
# RUN pipenv shell

ENV FLASK_RUN_HOST='0.0.0.0'
ENV FLASK_RUN_PORT=5000
RUN pipenv run python -m unittest discover
CMD [ "pipenv", "run","flask","--app", "hiveMod/flaskApp.py","run" ]
# CMD [ "bash"]