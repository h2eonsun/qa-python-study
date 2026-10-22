QA Python Study

Python과 pytest를 활용해 API 테스트와 응답 데이터 검증을 연습하는 개인 학습 프로젝트입니다. 기존 QA 경험을 바탕으로 테스트 자동화의 기본 구조를 익히고, 정상·오류 상황을 코드로 검증하는 과정을 정리하고 있습니다.
프로젝트 유형: 개인 학습 프로젝트 · 진행 중
기술: Python · pytest · requests · unittest.mock · JSON · Git


[구현 내용]

API 요청 및 응답 검증
- GitHub REST API의 저장소 조회 요청을 구성했습니다.
- HTTP 상태 코드와 저장소 응답 데이터의 필드·자료형을 검증합니다.
- 필수 필드 누락, 빈 문자열, 잘못된 자료형과 중첩 구조 등 잘못된 데이터를 테스트합니다.

오류 상황 테스트
- Mock으로 API 응답을 재현해 외부 네트워크 호출 없이 테스트합니다.
- HTTP 오류, 타임아웃, 연결 오류 등 예외 상황을 검증합니다.
- return_value와 side_effect를 활용해 반환값과 예외 상황을 각각 설정합니다.

테스트 코드 재사용 및 실행 관리
- pytest.fixture와 conftest.py로 테스트 준비 코드를 재사용합니다.
- pytest.mark.parametrize로 여러 상태 코드와 입력 조건을 검증합니다.
- JSON 테스트 데이터와 integration 마커를 활용해 데이터 기반 테스트와 외부 API 통합 테스트를 구분합니다.


[테스트 실행 방법]
아래 명령은 저장소 최상위 폴더에서 Windows PowerShell 기준으로 실행합니다.

1. 환경 설정
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest requests

2. 로컬 테스트 실행
python -m pytest -v
기본 실행에서는 외부 API를 호출하는 통합 테스트를 건너뛰도록 설정되어 있습니다.

3. 통합 테스트 실행
python -m pytest -m integration --run-integration -v
로컬 테스트와 통합 테스트를 모두 실행하려면 다음 명령을 사용합니다.
python -m pytest --run-integration -v
통합 테스트는 네트워크 연결과 GitHub API 요청 한도의 영향을 받을 수 있습니다.


[주요 파일]

파 일	                             역 할
---------------------------------------------------------------------
github_api.py	                    API 요청 및 응답 처리·검증 로직
settings.py	                        API 기본 URL과 타임아웃 설정
conftest.py	                        공통 Fixture와 통합 테스트 실행 옵션
pytest.ini	                        pytest 테스트 경로 및 마커 설정
test_github_mock.py	                Mock을 활용한 API 동작 테스트
test_github_exceptions.py	        HTTP 오류와 예외 처리 테스트
test_github_response_validation.py	응답 데이터 검증 테스트
test_github_data_driven.py	        JSON 데이터 기반 테스트
data/github_repository_cases.json	데이터 기반 테스트 케이스


[설정값]

환경 변수	          용도	                기본값
---------------------------------------------------------------------
GITHUB_API_BASE_URL	 GitHub API 기본 URL   https://api.github.com
API_TIMEOUT_SECONDS	 요청 타임아웃(초)	     5

PowerShell에서 현재 터미널 세션에만 타임아웃을 설정하는 예시입니다.
$env:API_TIMEOUT_SECONDS = "10"
python -m pytest -v
Remove-Item Env:API_TIMEOUT_SECONDS


[프로젝트 범위]

이 저장소는 테스트 자동화 기초를 익히기 위한 개인 학습 프로젝트입니다. 통합 테스트의 결과는 외부 API 상태와 네트워크 환경에 따라 달라질 수 있습니다. 테스트 통과 개수는 변경될 수 있으므로, 최신 결과는 제출 시점에 전체 테스트를 실행해 확인합니다.