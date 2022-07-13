# pull official base image
FROM python:3.9-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app
# WORKDIR /tecnoelectrocomercioonline

# install system dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add bash postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install python dependencies
RUN pip install --upgrade pip
# COPY requirements.txt /tecnoelectrocomercioonline/
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip3 install -r requirements.txt

# copy project
# COPY . .
COPY . /usr/src/app/

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]