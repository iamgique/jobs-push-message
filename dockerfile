FROM python:3

ADD pushmsg.py /

RUN pip install APScheduler
RUN pip install requests

CMD [ "python", "./pushmsg.py" ]