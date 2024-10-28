FROM python:3-slim

WORKDIR /usr/src/app


COPY /container/ ./
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./app.py" ]
