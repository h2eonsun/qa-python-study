def test_github_status_code(github_session):
    url = "https://api.github.com/repos/octocat/Hello-World"

    response = github_session.get(url, timeout=5)

    assert response.status_code == 200
    
def test_github_response_type(github_session):
    url = "https://api.github.com/repos/octocat/Hello-World"

    response = github_session.get(url, timeout=5)
    data = response.json()

    assert isinstance(data, dict)

def test_github_required_fields(github_session):
    url = "https://api.github.com/repos/octocat/Hello-World"

    response = github_session.get(url, timeout=5)
    data = response.json()

    assert "name" in data
    assert "full_name" in data
    assert "private" in data