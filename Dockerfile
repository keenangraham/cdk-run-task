FROM --platform=linux/x86_64 python:3.9.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY command.py command.py

COPY req.txt requirements.txt

RUN pip install -r requirements.txt

COPY script.sh script.sh

RUN chmod 755 script.sh

CMD ["python", "command.py"]