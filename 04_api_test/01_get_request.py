import requests

url = "https://postman-echo.com/get"

params = {
    "test": "123"
}

response = requests.get(url, params=params, timeout=5)
data = response.json()

response_time_ms = response.elapsed.total_seconds() * 1000

assert response.status_code == 200
assert isinstance(data, dict)
assert "test" in data["args"]
assert data["args"]["test"] == "123"

if response_time_ms <= 1000:
    result = "PASS"
else:
    result = "FAIL"

print(f"Status Code: {response.status_code}")
print(f"Response Time: {response_time_ms:.2f} ms")
print(f"Result: {result}")



