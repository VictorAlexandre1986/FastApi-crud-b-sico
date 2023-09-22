import os
DATABASE_URL = 'sqlite:///db.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'True'

from typing import Generator
from fastapi.testclient import TestClient
import pytest 
from main import app
from criar_tabelas import configurar_banco

@pytest.fixture(scope="function")
def client() -> Generator:
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c
