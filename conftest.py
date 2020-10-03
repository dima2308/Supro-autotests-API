import pytest

from api.client import Client
from config import host


@pytest.fixture(scope="session")
def client():
    client = Client(host)
    return client
