FROM python:3.10

WORKDIR /StoreManagementAPI/

#Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /StoreManagementAPI/

# Installing dependencies
RUN bash -c "poetry install --no-root --no-dev"

COPY . /StoreManagementAPI/

ENV PYTHONUNBUFFERED=1

ENV PYTHONPATH =/StoreManagementAPI/storemanagementapi/StoreManagement/