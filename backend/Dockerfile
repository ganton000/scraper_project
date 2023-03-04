FROM tiangolo/uvicorn-gunicorn:python3.11 AS install

ARG ENVIRONMENT

ENV PYROOT /app
ENV PYTHONUSERBASE /usr/local/bin
ENV PYTHONPATH ${PYROOT}:${PYTHONPATH}
ENV PATH /usr/local/bin:${PATH}:${PYTHONUSERBASE}/bin

COPY requirements.txt ${PYROOT}/requirements.txt

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && pip install -r ${PYROOT}requirements.txt \
#    && apk del .build-deps

#RUN if [ "${ENVIRONMENT}" == "tst" ]; then pip install --user -r -e .[tst]; \
#	else pip install --user -r ${PYROOT}/backend/requirements.txt --no-deps; fi

RUN pip install -r ${PYROOT}/requirements.txt

FROM tiangolo/uvicorn-gunicorn:python3.11

#RUN addgroup -S myapp && adduser -S -G myapp --system backenduser

ENV PYROOT /app
ENV PYTHONUSERBASE /usr/local/bin
ENV PYTHONPATH ${PYROOT}:${PYTHONPATH}
ENV PATH /usr/local/bin:${PATH}:${PYTHONUSERBASE}

COPY --from=install ${PYROOT}/ ${PYROOT}/

COPY . ${PYROOT}

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]