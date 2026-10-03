import pytest
import requests


@pytest.fixture
def github_session():
    session = requests.Session()

    session.headers.update({
        "Accept": "application/vnd.github+json"
    })

    yield session

    session.close()