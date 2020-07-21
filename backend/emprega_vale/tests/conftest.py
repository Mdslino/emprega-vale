from typing import Generator

import pytest
from starlette.testclient import TestClient
from emprega_vale.app import create_app

from emprega_vale.db.session import SessionLocal


@pytest.fixture(scope='module')
def app() -> Generator:
    yield create_app()


@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app) as c:
        yield c
