import math
import os
from urllib.parse import urlparse


def _load_base_url():
    raw_value = os.getenv(
        "GITHUB_API_BASE_URL",
        "https://api.github.com"
    ).strip()

    if not raw_value:
        raise ValueError(
            "GITHUB_API_BASE_URL must not be empty"
        )

    parsed_url = urlparse(raw_value)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError(
            "GITHUB_API_BASE_URL must be a valid HTTP or HTTPS URL"
        )

    return raw_value.rstrip("/")


GITHUB_API_BASE_URL = _load_base_url()


def _load_timeout_seconds():
    raw_value = os.getenv("API_TIMEOUT_SECONDS", "5")

    try:
        timeout = float(raw_value)
    except ValueError as exc:
        raise ValueError(
            "API_TIMEOUT_SECONDS must be a valid number"
        ) from exc

    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError(
            "API_TIMEOUT_SECONDS must be a finite number greater than 0"
        )

    return timeout


API_TIMEOUT_SECONDS = _load_timeout_seconds()