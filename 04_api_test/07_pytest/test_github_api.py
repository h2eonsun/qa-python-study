# 실제 GitHub API 검증

import pytest

from github_api import get_repository


pytestmark = pytest.mark.integration


def test_github_status_code(github_session):
    response = get_repository(
        github_session,
        "octocat/Hello-World"
    )

    assert response.status_code == 200


def test_github_response_type(github_session):
    response = get_repository(
        github_session,
        "octocat/Hello-World"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)


def test_github_required_fields(github_session):
    response = get_repository(
        github_session,
        "octocat/Hello-World"
    )

    assert response.status_code == 200

    data = response.json()

    assert "name" in data
    assert "full_name" in data
    assert "private" in data