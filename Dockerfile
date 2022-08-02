FROM python:3.9.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY command.py command.py

COPY req.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "command.py"]