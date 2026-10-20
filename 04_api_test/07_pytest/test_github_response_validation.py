import pytest
import requests
from unittest.mock import Mock

from github_api import (
    validate_repository_data,
    get_repository_data,
)

@pytest.fixture
def make_mock_session():
    def _make_mock_session(status_code=200, json_data=None):
        session = Mock()
        response = Mock()

        response.status_code = status_code
        response.json.return_value = json_data
        session.get.return_value = response

        return session, response

    return _make_mock_session

VALID_DATA = {
    "name": "Hello-World",
    "private": False,
    "owner": {
        "login": "octocat"
    }
}


def test_validate_repository_data_success():
    result = validate_repository_data(VALID_DATA)

    assert result is True


@pytest.mark.parametrize(
    "invalid_data",
    [
        # name 필드 누락
        {
            "private": False,
            "owner": {"login": "octocat"},
        },

        # private 필드 누락
        {
            "name": "Hello-World",
            "owner": {"login": "octocat"},
        },

        # owner 필드 누락
        {
            "name": "Hello-World",
            "private": False,
        },

        # owner 안에 login 필드 누락
        {
            "name": "Hello-World",
            "private": False,
            "owner": {},
        },

        # owner가 문자열인 경우
        {
            "name": "Hello-World",
            "private": False,
            "owner": "octocat",
        },
        # name이 공백으로만 구성된 경우
        {
            "name": "   ",
            "private": False,
            "owner": {"login": "octocat"},
        },
        # name이 숫자인 경우
        {
            "name": 123,
            "private": False,
            "owner": {"login": "octocat"},
        },
        # name이 None인 경우
        {
            "name": None,
            "private": False,
            "owner": {"login": "octocat"},
        },
        # private가 정수 0인 경우
        {
            "name": "Hello-World",
            "private": 0,
            "owner": {"login": "octocat"},
        },
        # owner.login이 숫자인 경우
        {
            "name": "Hello-World",
            "private": False,
            "owner": {"login": 123},
        },
        None,
        {},
        {
            "name": "",
            "private": False,
            "owner": {"login": "octocat"},
        },
        {
            "name": "Hello-World",
            "private": "false",
            "owner": {"login": "octocat"},
        },
        {
            "name": "Hello-World",
            "private": False,
            "owner": None,
        },
        {
            "name": "Hello-World",
            "private": False,
            "owner": {"login": ""},
        },
    ],
)
def test_validate_repository_data_invalid(invalid_data):
    with pytest.raises(ValueError):
        validate_repository_data(invalid_data)



@pytest.mark.parametrize(
    ("invalid_data", "expected_message"),
    [
        (
            {
                "private": False,
                "owner": {"login": "octocat"},
            },
            "Repository name must be a non-empty string",
        ),
        (
            {
                "name": "Hello-World",
                "owner": {"login": "octocat"},
            },
            "Repository private must be a boolean",
        ),
        (
            {
                "name": "Hello-World",
                "private": False,
                "owner": {},
            },
            "Owner login must be a non-empty string",
        ),
    ],
)
def test_validate_repository_data_error_message(
    invalid_data,
    expected_message,
):
    with pytest.raises(ValueError, match=expected_message):
        validate_repository_data(invalid_data)



def test_get_repository_data_success(make_mock_session):
    valid_data = {
        "name": "Hello-World",
        "private": False,
        "owner": {"login": "octocat"},
    }

    session, _ = make_mock_session(
        status_code=200,
        json_data=valid_data,
    )

    result = get_repository_data(session, "octocat/Hello-World")

    assert result["name"] == "Hello-World"
    assert result["private"] is False
    assert result["owner"]["login"] == "octocat"
    session.get.assert_called_once()


def test_get_repository_data_http_error(make_mock_session):
    session, _ = make_mock_session(status_code=404)

    with pytest.raises(requests.HTTPError, match="404"):
        get_repository_data(session, "octocat/Hello-World")


def test_get_repository_data_invalid_json_data(make_mock_session):
    invalid_data = {
        "name": "",
        "private": False,
        "owner": {"login": "octocat"},
    }

    session, _ = make_mock_session(
        status_code=200,
        json_data=invalid_data,
    )

    with pytest.raises(
        ValueError,
        match="Repository name must be a non-empty string",
    ):
        get_repository_data(session, "octocat/Hello-World")
