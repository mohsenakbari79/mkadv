
# Pull base image
FROM python:3.8-slim-buster
# LABEL MAINTAINER=" https://giahino "
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
RUN mkdir /app
WORKDIR /app
# Install dependencies
# COPY Pipfile Pipfile.lock /code/
ADD core/requirements.txt /app

COPY ./core/ /giahino/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python manage.py collectstatic --no-input