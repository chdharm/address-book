FROM ubuntu:18.04
MAINTAINER Dharmpal Chaudhary <chaudharydharmpal95@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
RUN apt-get update --fix-missing
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN apt-get install -y libsqlite3-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y p7zip-full
RUN apt-get install -y p7zip-rar
RUN pip3 install --upgrade pip
ADD requirements.txt /config/
RUN pip3 install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src
COPY . /src