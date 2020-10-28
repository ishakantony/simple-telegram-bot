FROM python:3-slim  

COPY . /

RUN pip3 install --upgrade google-api-python-client oauth2client python-telegram-bot requests --upgrade

EXPOSE 4444
