
FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

COPY . /home
WORKDIR /home

RUN pip3 install -r requirements.txt
RUN pip3 install email_validator

RUN ls /home

ENV FLASK_APP app.py
RUN echo $FLASK_APP

RUN flask db init
RUN flask db migrate
RUN flask db upgrade
RUN ls /home


