FROM python:3.10-alpine AS builder

RUN apk update && apk upgrade

RUN pip install pipenv==2022.9.24

ENV PYROOT /pyroot
ENV PYTHONUSERBASE $PYROOT
WORKDIR /build

COPY Pipfile Pipfile.lock ./
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pipenv install --system --deploy

FROM python:3.10-alpine AS application

RUN apk update && apk upgrade

ENV PYROOT /pyroot
ENV PATH $PYROOT/bin:$PATH
ENV PYTHONPATH /code/:$PYROOT/lib/python3.10:$PATH
ENV PYTHONUSERBASE $PYROOT

COPY --from=builder $PYROOT/ $PYROOT/

ENV PORT=5000
ENV LOG_LEVEL="debug"
ENV WORKERS=2

WORKDIR /code

ADD app /code

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:$PORT --workers=$WORKERS --log-level=$LOG_LEVEL --timeout=3600 app:app"]
