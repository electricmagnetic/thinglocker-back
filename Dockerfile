FROM python:3.6-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /src /src

CMD ["gunicorn", "--pythonpath", "src", "--bind", "0.0.0.0:8000", "thinglocker.wsgi"]
