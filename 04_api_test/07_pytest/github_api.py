# 실제 API 호출 기능

import requests
from settings import API_TIMEOUT_SECONDS, GITHUB_API_BASE_URL


def get_repository(session, repository):
    url = f"{GITHUB_API_BASE_URL}/repos/{repository}"
    return session.get(url, timeout=API_TIMEOUT_SECONDS)


# 요청 오류를 처리해서 결과 반환
def get_repository_safely(session, repository):
    try:
        response = get_repository(session, repository)

        # 상태 코드가 200~299인지 확인
        if not 200 <= response.status_code < 300:
            return {
                "success": False,
                "response": response,
                "error": "http_error",
            }

        # 정상적인 HTTP 상태 코드라면 성공 반환
        return {
            "success": True,
            "response": response,
            "error": None,
        }

    # 요청 시간이 초과된 경우
    except requests.Timeout:
        return {
            "success": False,
            "response": None,
            "error": "timeout",
        }

    # 서버 연결에 실패한 경우
    except requests.ConnectionError:
        return {
            "success": False,
            "response": None,
            "error": "connection_error",
        }
