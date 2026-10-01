import requests

url = "https://api.github.com/repos/octocat/Hello-World"

response = requests.get(url, timeout=5)

data = response.json()

response_time_ms = response.elapsed.total_seconds() * 1000

#Repository 조회 요청 정상적 성공 검증
assert response.status_code == 200
#Response 데이터 타입 검증
assert isinstance(data, dict)

#필수 필드 존재 검증
assert "name" in data
assert "full_name" in data
assert "private" in data

#실제 값 검증
assert data["name"] == "Hello-World"
assert data["full_name"] == "octocat/Hello-World"
assert data["private"] is False

#Response Time 검증
assert response_time_ms <= 1000

print(f"Status Code: {response.status_code}")
print(f"Repository: {data['full_name']}")
print(f"Response Time: {response_time_ms:.2f} ms")
print("GitHub API Test PASS")


