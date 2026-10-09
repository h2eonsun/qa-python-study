import os

GITHUB_API_BASE_URL = os.getenv(
    "GITHUB_API_BASE_URL",
    "https://api.github.com"
).rstrip("/")

API_TIMEOUT_SECONDS = float(
    os.getenv("API_TIMEOUT_SECONDS", "5")
)