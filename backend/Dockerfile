FROM python:3.8.3-slim

WORKDIR /app

LABEL maintainer="Marcelo Lino"
LABEL email="mdslino@gmail.com"

ARG environment

ENV ENV_FOR_DYNACONF=$environment \
POETRY_VIRTUALENVS_CREATE=false \
PIP_NO_CACHE_DIR=true

RUN apt-get update && apt-get install --no-install-recommends -y curl && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

COPY . .

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80","-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--access-logfile=-", "--error-logfile=-", "emprega_vale.app:create_app()"]