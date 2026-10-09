import pytest
import requests


@pytest.fixture(scope="function")
def github_session():
    session = requests.Session()

    session.headers.update({
        "Accept": "application/vnd.github+json"
    })

    yield session

    session.close()

def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run tests that access live external APIs",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-integration"):
        return

    skip_integration = pytest.mark.skip(
        reason="Use --run-integration to run live API tests"
    )

    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)