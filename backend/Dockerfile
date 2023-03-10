FROM tiangolo/uvicorn-gunicorn:python3.11 AS install

#ARG ENVIRONMENT

#ENV PYROOT /pyroot
#ENV PYTHONUSERBASE ${PYROOT}/backend/packages
#ENV PYTHONPATH ${PYROOT}/backend/:${PYTHONPATH}
#ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin:${PYROOT}/backend/venv/lib/python3.10/site-packages/

COPY requirements.txt /app/requirements.txt

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && pip install -r ${PYROOT}requirements.txt \
#    && apk del .build-deps

#RUN if [ "${ENVIRONMENT}" == "tst" ]; then pip install --user -r -e .[tst]; \
#	else pip install --user -r ${PYROOT}/backend/requirements.txt --no-deps; fi

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

FROM tiangolo/uvicorn-gunicorn:python3.11

ENV APP_MODULE main:app
ENV PORT 80008000
ENV HOST 0.0.0.0
ENV LOG_LEVEL debug

#RUN addgroup -S myapp && adduser -S -G myapp --system backenduser

COPY --from=install /app /app

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "/usr/local/bin/python3", "-m", "main.py" ]