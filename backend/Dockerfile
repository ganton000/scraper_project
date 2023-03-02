FROM python:3.10-alpine AS install

ENV PYROOT /pyroot
ENV PYTHONPATH ${PYROOT}:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin

COPY requirements.txt ${PYROOT}/backend/

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && pip install -r ${PYROOT}/backend/requirements.txt \
#    && apk del .build-deps

RUN pip install --user -r ${PYROOT}/backend/requirements.txt

WORKDIR ${PYROOT}/backend

FROM python:3.10-alpine

RUN addgroup -S myapp && adduser -S -G myapp --system backenduser

ENV PYROOT /pyroot
ENV PYTHONPATH ${PYROOT}:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin

COPY --chown=myapp:backenduser --from=install ${PYROOT}/ ${PYROOT}/

COPY --chown=myapp:backenduser . ./

COPY --chown=myapp:backenduser main.py ./

USER backenduser

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]