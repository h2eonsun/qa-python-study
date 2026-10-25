import pytest
from unittest.mock import MagicMock, Mock
from github_api import get_repository
from settings import API_TIMEOUT_SECONDS, GITHUB_API_BASE_URL

def test_get_repository_status_200():
    mock_session = MagicMock()

    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_session.get.return_value = mock_response

    response = get_repository(
        mock_session,
        "octocat/Hello-World"
    )

    assert response.status_code == 200


def test_get_repository_status_404():
    mock_session = MagicMock()

    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {
        "message": "Not Found"
    }

    mock_session.get.return_value = mock_response

    response = get_repository(
        mock_session,
        "octocat/ThisRepositoryDoesNotExist"
    )

    assert response.status_code == 404
    assert response.json()["message"] == "Not Found"


def test_get_repository_status_500():
    mock_session = MagicMock()

    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.json.return_value = {
        "message": "Internal Server Error"
    }

    mock_session.get.return_value = mock_response

    response = get_repository(
        mock_session,
        "octocat/Hello-World"
    )

    assert response.status_code == 500
    assert response.json()["message"] == "Internal Server Error"


def test_get_repository_request():
    mock_session = MagicMock()

    mock_response = MagicMock()
    mock_response.status_code = 200

    mock_session.get.return_value = mock_response

    get_repository(
        mock_session,
        "octocat/Hello-World"
    )

    mock_session.get.assert_called_once_with(
    f"{GITHUB_API_BASE_URL}/repos/octocat/Hello-World",
    timeout=API_TIMEOUT_SECONDS
    )


def test_get_repository_response_data():
    mock_session = MagicMock()

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Hello-World",
        "full_name": "octocat/Hello-World",
        "private": False
    }

    mock_session.get.return_value = mock_response

    response = get_repository(
        mock_session,
        "octocat/Hello-World"
    )

    data = response.json()

    assert data["name"] == "Hello-World"
    assert data["full_name"] == "octocat/Hello-World"
    assert data["private"] is False


@pytest.mark.parametrize(
    "repository",
    [
        "octocat/Hello-World",
        "psf/requests",
    ],
)
def test_get_repository_calls_api_with_url_and_timeout(repository):
    session = Mock()
    expected_response = Mock()
    session.get.return_value = expected_response

    result = get_repository(session, repository)

    expected_url = f"{GITHUB_API_BASE_URL}/repos/{repository}"

    session.get.assert_called_once_with(
        expected_url,
        timeout=API_TIMEOUT_SECONDS,
    )

    assert result is expected_response