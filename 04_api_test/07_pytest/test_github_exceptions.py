# pytest에서 제공하는 예외 검증

import pytest
import requests
from unittest.mock import Mock
from github_api import get_repository


def test_get_repository_timeout():
    # 가짜 세션 생성: 실제 서버에 접속하지 않음
    session = Mock()

    # [Mock 기능]
    # session.get()이 호출되면 타임아웃 예외를 발생시키도록 설정
    session.get.side_effect = requests.Timeout("Request timed out")

    # [pytest 기능]
    # get_repository()에서 Timeout 예외가 발생하는지 확인
    with pytest.raises(requests.Timeout):
        get_repository(session, "octocat/Hello-World")

    # [Mock 기능]
    # API 요청 함수가 실제로 호출되었는지도 확인
    session.get.assert_called_once()


    
def test_get_repository_connection_error():
    # [Mock 기능] 실제 서버에 접속하지 않는 가짜 세션 생성
    session = Mock()

    # [Mock 설정] get()이 호출되면 연결 실패 예외를 발생시킴
    session.get.side_effect = requests.ConnectionError(
        "Connection failed"
    )

    # [pytest 기능] 예상한 ConnectionError가 발생하는지 확인
    with pytest.raises(requests.ConnectionError):
        get_repository(session, "octocat/Hello-World")

    # [Mock 기능] get()이 정확히 한 번 호출됐는지 확인
    session.get.assert_called_once()
