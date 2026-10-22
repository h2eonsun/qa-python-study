# QA Python Study

Python과 pytest를 활용해 API 테스트와 응답 데이터 검증을 연습하는 개인 학습 프로젝트입니다. GitHub REST API를 대상으로 정상 응답과 오류 상황을 테스트하고, 테스트 코드를 재사용할 수 있도록 구조를 정리했습니다.

- **프로젝트 유형:** 개인 학습 프로젝트 · 진행 중
- **기술:** Python, pytest, requests, unittest.mock, JSON, Git

## 구현 내용

### API 요청 및 응답 검증

- GitHub REST API의 저장소 조회 요청 구현
- HTTP 상태 코드와 저장소 응답 데이터의 필드 및 자료형 검증
- 필수 필드 누락, 빈 문자열, 잘못된 자료형 및 중첩 구조에 대한 테스트 작성

### 오류 상황 테스트

- Mock으로 API 응답을 재현해 외부 네트워크 호출 없이 테스트
- HTTP 오류, 타임아웃, 연결 오류 상황 검증
- `return_value`와 `side_effect`를 사용해 반환값과 예외 상황 설정

### 테스트 코드 재사용 및 실행 관리

- `pytest.fixture`와 `conftest.py`를 활용해 테스트 준비 코드 재사용
- `pytest.mark.parametrize`로 여러 상태 코드와 입력 조건 검증
- JSON 테스트 데이터를 활용한 데이터 기반 테스트 구성
- `integration` 마커와 실행 옵션으로 로컬 테스트와 외부 API 통합 테스트 구분

## 실행 방법

아래 명령은 저장소 최상위 폴더에서 Windows PowerShell 기준으로 실행합니다.

### 1. 가상환경 구성 및 패키지 설치

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install pytest requests
```

### 2. 로컬 테스트 실행

```powershell
python -m pytest -v
```

기본 실행에서는 외부 API를 호출하는 통합 테스트를 건너뜁니다.

### 3. 통합 테스트만 실행

```powershell
python -m pytest -m integration --run-integration -v
```

로컬 테스트와 통합 테스트를 모두 실행하려면 다음 명령을 사용합니다.

```powershell
python -m pytest --run-integration -v
```

통합 테스트는 네트워크 연결과 GitHub API 요청 한도의 영향을 받을 수 있습니다.

## 주요 파일

| 파일 | 역할 |
|---|---|
| [`github_api.py`](04_api_test/07_pytest/github_api.py) | API 요청 및 응답 처리·검증 로직 |
| [`settings.py`](04_api_test/07_pytest/settings.py) | API 기본 URL과 타임아웃 설정 |
| [`conftest.py`](04_api_test/07_pytest/conftest.py) | 공통 Fixture와 통합 테스트 실행 옵션 |
| [`pytest.ini`](pytest.ini) | pytest 테스트 경로 및 마커 설정 |
| [`test_github_api.py`](04_api_test/07_pytest/test_github_api.py) | GitHub API 요청 및 응답 테스트 |
| [`test_github_repository.py`](04_api_test/07_pytest/test_github_repository.py) | 저장소 조회 관련 테스트 |
| [`test_github_data_driven.py`](04_api_test/07_pytest/test_github_data_driven.py) | JSON 데이터 기반 테스트 |
| [`test_github_mock.py`](04_api_test/07_pytest/test_github_mock.py) | Mock을 활용한 API 동작 테스트 |
| [`test_github_exceptions.py`](04_api_test/07_pytest/test_github_exceptions.py) | HTTP 오류와 예외 처리 테스트 |
| [`test_github_response_validation.py`](04_api_test/07_pytest/test_github_response_validation.py) | 응답 데이터 검증 테스트 |
| [`github_repository_cases.json`](04_api_test/07_pytest/data/github_repository_cases.json) | 데이터 기반 테스트 케이스 |

## 설정값

| 환경 변수 | 용도 | 기본값 |
|---|---|---|
| `GITHUB_API_BASE_URL` | GitHub API 기본 URL | `https://api.github.com` |
| `API_TIMEOUT_SECONDS` | 요청 타임아웃(초) | `5` |

PowerShell에서 현재 터미널 세션에만 타임아웃을 설정하는 예시입니다.

```powershell
$env:API_TIMEOUT_SECONDS = "10"
python -m pytest -v
Remove-Item Env:API_TIMEOUT_SECONDS
```

## 프로젝트 범위

테스트 자동화 기초를 익히기 위한 개인 학습 프로젝트입니다. 외부 API를 사용하는 통합 테스트 결과는 네트워크 환경과 API 요청 한도의 영향을 받을 수 있습니다. 테스트 결과는 코드 변경에 따라 달라지므로, 최신 결과는 실행 시점에 확인합니다.
