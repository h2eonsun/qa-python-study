import pytest
import importlib
from unittest.mock import Mock

import github_api
import settings


def test_settings_uses_default_values_when_environment_variables_are_missing(
    monkeypatch,
):
    try:
        with monkeypatch.context() as m:
            m.delenv("GITHUB_API_BASE_URL", raising=False)
            m.delenv("API_TIMEOUT_SECONDS", raising=False)

            reloaded_settings = importlib.reload(settings)

            assert (
                reloaded_settings.GITHUB_API_BASE_URL
                == "https://api.github.com"
            )
            assert reloaded_settings.API_TIMEOUT_SECONDS == 5.0
    finally:
        importlib.reload(settings)


def test_settings_reads_environment_variables(monkeypatch):
    try:
        with monkeypatch.context() as m:
            m.setenv("GITHUB_API_BASE_URL", "https://example.com/")
            m.setenv("API_TIMEOUT_SECONDS", "10")

            reloaded_settings = importlib.reload(settings)

            assert (
                reloaded_settings.GITHUB_API_BASE_URL
                == "https://example.com"
            )
            assert reloaded_settings.API_TIMEOUT_SECONDS == 10.0
    finally:
        importlib.reload(settings)


def test_get_repository_uses_environment_settings(monkeypatch):
    try:
        with monkeypatch.context() as m:
            m.setenv("GITHUB_API_BASE_URL", "https://example.com/")
            m.setenv("API_TIMEOUT_SECONDS", "10")

            importlib.reload(settings)
            importlib.reload(github_api)

            session = Mock()
            expected_response = Mock()
            session.get.return_value = expected_response

            result = github_api.get_repository(
                session,
                "octocat/Hello-World",
            )

            session.get.assert_called_once_with(
                "https://example.com/repos/octocat/Hello-World",
                timeout=10.0,
            )

            assert result is expected_response

    finally:
        importlib.reload(settings)
        importlib.reload(github_api)


# URL 끝의 슬래시 제거 테스트
@pytest.mark.parametrize(
    ("base_url", "expected_url"),
    [
        ("https://example.com", "https://example.com"),
        ("https://example.com/", "https://example.com"),
        ("https://example.com///", "https://example.com"),
    ],
    ids=[
        "without-trailing-slash",
        "one-trailing-slash",
        "multiple-trailing-slashes",
    ],
)
def test_settings_removes_trailing_slashes(
    monkeypatch,
    base_url,
    expected_url,
):
    try:
        with monkeypatch.context() as m:
            m.setenv("GITHUB_API_BASE_URL", base_url)

            reloaded_settings = importlib.reload(settings)

            assert reloaded_settings.GITHUB_API_BASE_URL == expected_url

    finally:
        importlib.reload(settings)


# 타임아웃 숫자형 변환 테스트
@pytest.mark.parametrize(
    ("timeout_value", "expected_timeout"),
    [
        ("5", 5.0),
        ("10", 10.0),
        ("2.5", 2.5),
    ],
    ids=[
        "integer-string",
        "ten-seconds",
        "decimal-string",
    ],
)
def test_settings_converts_timeout_to_float(
    monkeypatch,
    timeout_value,
    expected_timeout,
):
    try:
        with monkeypatch.context() as m:
            m.setenv("API_TIMEOUT_SECONDS", timeout_value)

            reloaded_settings = importlib.reload(settings)

            assert (
                reloaded_settings.API_TIMEOUT_SECONDS
                == expected_timeout
            )

    finally:
        importlib.reload(settings)


@pytest.mark.parametrize(
    ("timeout_value", "expected_message"),
    [
        (
            "abc",
            "API_TIMEOUT_SECONDS must be a valid number",
        ),
        (
            "",
            "API_TIMEOUT_SECONDS must be a valid number",
        ),
        (
            "five",
            "API_TIMEOUT_SECONDS must be a valid number",
        ),
        (
            "0",
            "API_TIMEOUT_SECONDS must be a finite number greater than 0",
        ),
        (
            "-1",
            "API_TIMEOUT_SECONDS must be a finite number greater than 0",
        ),
        (
            "nan",
            "API_TIMEOUT_SECONDS must be a finite number greater than 0",
        ),
        (
            "inf",
            "API_TIMEOUT_SECONDS must be a finite number greater than 0",
        ),
    ],
    ids=[
        "alphabetic-value",
        "empty-value",
        "word-value",
        "zero-value",
        "negative-value",
        "not-a-number",
        "infinite-value",
    ],
)
def test_settings_rejects_invalid_timeout_values(
    monkeypatch,
    timeout_value,
    expected_message,
):
    try:
        with monkeypatch.context() as m:
            m.setenv("API_TIMEOUT_SECONDS", timeout_value)

            with pytest.raises(ValueError, match=expected_message):
                importlib.reload(settings)

    finally:
        importlib.reload(settings)