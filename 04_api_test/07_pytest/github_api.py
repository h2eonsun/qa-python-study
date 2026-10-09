# 실제 API 호출 기능

import requests

def get_repository(session, repository):
    url = f"https://api.github.com/repos/{repository}"

    return session.get(url, timeout=5)

