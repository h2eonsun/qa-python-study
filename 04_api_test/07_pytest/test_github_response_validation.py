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
