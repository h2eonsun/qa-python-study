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

# pytest.ini에 정의된 옵션을 처리하는 hook 함수
def pytest_addoption(parser):
    parser.addoption(
        "--run-integration",
        action="store_true",
        default=False,
        help="Run tests that access live external APIs",
    )

# 테스트 수집 후 실행 전 목록을 조정하는 hook 함수
def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-integration"):
        return

    # integration 마커가 있는 테스트를 건너뛰도록 설정
    skip_integration = pytest.mark.skip(
        reason="Integration test skipped. Use --run-integration to run."
    )

    for item in items:
        if "integration" in item.keywords:
            item.add_marker(skip_integration)