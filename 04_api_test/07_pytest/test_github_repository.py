# parameterize

import pytest

pytestmark = pytest.mark.integration

@pytest.mark.parametrize(
    "repository, expected_status",
    [
        pytest.param(
            "octocat/Hello-World",
            200,
            id="TC001-valid-repository"
        ),
        pytest.param(
            "octocat/Spoon-Knife",
            200,
            id="TC002-valid-repository"
        ),
        pytest.param(
            "octocat/ThisRepositoryDoesNotExist",
            404,
            id="TC003-not-found"
        ),
    ]
)
def test_repository_status(
    github_session,
    repository,
    expected_status
):
    url = f"https://api.github.com/repos/{repository}"

    response = github_session.get(url, timeout=5)

    assert response.status_code == expected_status