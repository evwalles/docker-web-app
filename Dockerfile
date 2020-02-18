FROM python:alpine3.10

COPY . /app

WORKDIR /app

RUN apk add --update python py-pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "/app/app.py", "-p 8000"]