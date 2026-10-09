# 실제 API 호출 기능

import requests
from settings import API_TIMEOUT_SECONDS, GITHUB_API_BASE_URL


def get_repository(session, repository):
    url = f"{GITHUB_API_BASE_URL}/repos/{repository}"

    return session.get(
        url,
        timeout=API_TIMEOUT_SECONDS
    )
