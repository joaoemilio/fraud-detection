FROM ubuntu:20.04

RUN apt-get update -y && \
    apt install git python3-pip python python-setuptools -y

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /usr/src/
COPY build.txt .
RUN cat build.txt && git clone https://github.com/joaoemilio/fraud-detection.git
WORKDIR /usr/src/fraud-detection
RUN pip3 install gunicorn json-logging-py 
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install dateutils 

EXPOSE 5000
#WORKDIR /opt/bot_server

ENTRYPOINT ["python3", "Server.py"]