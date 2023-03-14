FROM tiangolo/uvicorn-gunicorn:python3.11 AS install

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend/

EXPOSE 8000

RUN [ "python3", "main.py" ]
