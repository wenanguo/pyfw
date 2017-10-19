FROM python:3.6

ADD ./code /app 

WORKDIR   /app

ENV FLASK_CONFIG production

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/bin/bash","./run.sh"]
