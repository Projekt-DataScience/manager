FROM python:3.10-alpine

COPY create_db.py /create_db.py
COPY requirements.txt /requirements.txt

RUN apk update && apk upgrade && \
    apk add --no-cache git 
RUN pip install -r /requirements.txt

CMD ["python", "/create_db.py"]