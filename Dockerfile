FROM python:3.7

MAINTAINER Tristan Andersen "tristanpn02@gmail.com"

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "spilum:app"]
