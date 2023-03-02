FROM python:3.10-alpine

WORKDIR /backend

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN addgroup -S myapp && adduser -S -G myapp backenduser -u 1234
USER backenduser

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]