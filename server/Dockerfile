FROM python:3.9
COPY requirements.txt /requirements/requirements.txt
RUN apt update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements/requirements.txt \
    && rm -rf /requirements
COPY ./src /app
WORKDIR /app
