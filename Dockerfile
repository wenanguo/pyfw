FROM python:3.6

ADD ./code /app 

WORKDIR   /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["run.sh"]
