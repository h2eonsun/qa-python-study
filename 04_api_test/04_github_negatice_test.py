import requests

url = "https://api.github.com/repos/octocat/ThisRepositoryDoesNotExist"

response = requests.get(url, timeout=5)

expected_status = 404
actual_status = response.status_code

assert actual_status == expected_status

print(f"Expected: {expected_status}")
print(f"Actual: {actual_status}")
print("Negative Test PASS")