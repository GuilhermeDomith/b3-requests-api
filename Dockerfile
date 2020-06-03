FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk update
RUN apk --update add bash nano
RUN apk add firefox-esr
RUN apk add xvfb
RUN apk add chromium
RUN apk add chromium-chromedriver

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt