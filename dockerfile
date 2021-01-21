FROM python:3.6-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .

RUN flask db init && flask db migrate && flask db upgrade

CMD ["python", "app.py"]