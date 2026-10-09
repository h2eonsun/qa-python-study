# JSON + parameterize

import pytest
import requests
import json
from pathlib import Path
from github_api import get_repository

pytestmark = pytest.mark.integration

DATA_FILE = Path(__file__).parent / "data" / "github_repository_cases.json"


def load_test_cases():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


test_cases = load_test_cases()


@pytest.mark.parametrize(
    "test_case",
    test_cases,
    ids=[test_case["test_id"] for test_case in test_cases]
)
def test_repository_status(github_session, test_case):
    response = get_repository(
    github_session,
    test_case["repository"]
    )

    assert response.status_code == test_case["expected_status"]

    if response.status_code == 200:
        data = response.json()
        assert data["name"] == test_case["expected_name"]