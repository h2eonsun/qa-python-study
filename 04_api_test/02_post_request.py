import requests

url = "https://postman-echo.com/post"

payload = {
    "name": "Hyunsun",
    "job": "QA"
}

response = requests.post(
    url,
    json=payload,
    timeout=5
)

data = response.json()

assert response.status_code == 200
assert "json" in data
assert data["json"]["name"] == "Hyunsun"
assert data["json"]["job"] == "QA"

print("POST API Test PASS")

