FROM python:3.8-slim-buster

COPY main.py .

ENTRYPOINT ["python","./main.py"]