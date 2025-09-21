import pytest
from helpers import configure_logging

@pytest.fixture(scope="session", autouse=True)
def _setup_logging_once():
    configure_logging()
    yield