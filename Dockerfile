FROM python:3.8

COPY main.py .

ENTRYPOINT ["python","./main.py"]