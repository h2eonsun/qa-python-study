import pytest
import requests


@pytest.fixture
def github_response():
    url = "https://api.github.com/repos/octocat/Hello-World"

    return requests.get(url, timeout=5)


def test_status_code(github_response):
    assert github_response.status_code == 200


def test_response_type(github_response):
    data = github_response.json()

    assert isinstance(data, dict)


@pytest.mark.parametrize(
    "test_id,expected,actual",
    [
        ("TC001", "PASS", "PASS"),
        ("TC002", "PASS", "FAIL"),
        ("TC003", "FAIL", "FAIL"),
        ("TC004", "PASS", "PASS"),
    ]
)
def test_result(test_id, expected, actual):
    assert expected == actual