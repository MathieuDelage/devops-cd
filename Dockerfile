FROM python:3.9-alpine3.14

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

CMD python app.py