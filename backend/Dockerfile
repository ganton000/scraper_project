FROM tiangolo/uvicorn-gunicorn:python3.11 AS install

ARG ENVIRONMENT

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}/backend/packages
ENV PYTHONPATH ${PYROOT}/backend/:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin:${PYROOT}/backend/venv/lib/python3.10/site-packages/

COPY requirements.txt ${PYROOT}/backend/requirements.txt

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && pip install -r ${PYROOT}requirements.txt \
#    && apk del .build-deps

#RUN if [ "${ENVIRONMENT}" == "tst" ]; then pip install --user -r -e .[tst]; \
#	else pip install --user -r ${PYROOT}/backend/requirements.txt --no-deps; fi

RUN pip install -r ${PYROOT}/backend/requirements.txt

FROM tiangolo/uvicorn-gunicorn:python3.11

#RUN addgroup -S myapp && adduser -S -G myapp --system backenduser

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}/backend/packages
ENV PYTHONPATH ${PYROOT}/backend/:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin
ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin:${PYROOT}/backend/venv/lib/python3.10/site-packages/

COPY --from=install ${PYROOT}/ ${PYROOT}/

COPY . ${PYROOT}/backend

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]