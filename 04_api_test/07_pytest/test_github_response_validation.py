import pytest

from github_api import validate_repository_data


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
