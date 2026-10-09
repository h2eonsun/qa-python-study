# Pytest API Test Automation

pytest와 requests를 활용한 API 테스트 자동화 학습

## Test Scope

- GitHub REST API GET 테스트
- Status Code 검증
- Response JSON 검증
- Header 검증
- Parameterized Test
- JSON 기반 Data-Driven Test
- Mock 기반 API 테스트

## Test Structure

- `conftest.py`: 공통 pytest fixture 관리
- `github_api.py`: GitHub API 호출 기능
- `test_github_api.py`: GitHub API 기본 검증
- `test_github_repository.py`: Repository parameterized test
- `test_github_data_driven.py`: JSON 기반 Data-Driven test
- `test_github_mock.py`: Mock 기반 API test

## Mock Test

외부 GitHub API 상태와 관계없이
200, 404, 500 등의 응답 상황을 재현하여
API 검증 로직을 독립적으로 테스트