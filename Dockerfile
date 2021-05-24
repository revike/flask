FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run"]