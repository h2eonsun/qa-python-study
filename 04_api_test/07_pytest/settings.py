import math
import os

GITHUB_API_BASE_URL = os.getenv(
    "GITHUB_API_BASE_URL",
    "https://api.github.com"
).rstrip("/")


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