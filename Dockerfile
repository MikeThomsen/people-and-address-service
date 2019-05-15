FROM python:3.7-stretch

WORKDIR /usr/src/app

RUN pip install usaddress probablepeople flask

COPY . .

CMD [ "python", "./app.py" ]
