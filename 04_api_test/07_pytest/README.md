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

## Configuration

`settings.py`에서 GitHub API 기본 주소와 요청 timeout을 관리

- `GITHUB_API_BASE_URL`: GitHub API 기본 주소
- `API_TIMEOUT_SECONDS`: API 요청 timeout (초)

환경변수가 설정되지 않으면 기본값을 사용

## API Client

`github_api.py`는 Repository 조회 요청을 담당

테스트 코드에서 API 호출 기능을 재사용하며
각 테스트는 Response의 상태 코드와 데이터를 검증

## Mock Tests

`test_github_mock.py`는 실제 네트워크 요청 없이
Mock Session과 Response를 사용하여 API 호출과 응답 검증을 수행