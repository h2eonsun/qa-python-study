import importlib
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