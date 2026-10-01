import requests

url = "https://api.github.com/repos/octocat/Hello-World"

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10"
}

response = requests.get(
    url,
    headers=headers,
    timeout=5
)

data = response.json()

assert response.status_code == 200
assert "application/json" in response.headers.get("content-type", "")

assert isinstance(data, dict)
assert isinstance(data["id"], int)
assert isinstance(data["name"], str)
assert isinstance(data["full_name"], str)
assert isinstance(data["private"], bool)

assert data["name"] == "Hello-World"
assert data["full_name"] == "octocat/Hello-World"
assert data["private"] is False

print("GitHub API Test PASS")