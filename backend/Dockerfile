FROM python:3.10-alpine AS install

ARG ENVIRONMENT

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}/backend/packages
ENV PYTHONPATH ${PYROOT}/backend/:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin

COPY requirements.txt ${PYROOT}/backend/requirements.txt

#RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
#    && pip install -r ${PYROOT}requirements.txt \
#    && apk del .build-deps

RUN if [ "${ENVIRONMENT}" == "tst" ]; then pip install --user -r -e .[tst]; \
	else pip install --user -r ${PYROOT}/backend/requirements.txt --no-deps; fi

FROM python:3.10-alpine

RUN addgroup -S myapp && adduser -S -G myapp --system backenduser

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}/backend/packages
ENV PYTHONPATH ${PYROOT}/backend/:${PYTHONPATH}
ENV PATH=${PATH}:${PYROOT}/bin:${PYTHONUSERBASE}/bin

WORKDIR ${PYROOT}/backend

COPY --chown=backenduser:myapp --from=install ${PYROOT}/ ${PYROOT}/

COPY --chown=backenduser:myapp . ./

USER backenduser

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]