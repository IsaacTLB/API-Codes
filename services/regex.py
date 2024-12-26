import httpx
import re
from utils.config import REGEX_URL


async def process_with_regex(data: dict):
    """Process data asynchronously with an external regex service."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{REGEX_URL}/process", json=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
    except httpx.HTTPStatusError as e:
        raise ValueError(f"HTTP error occurred: {e.response.status_code}") from e
    except httpx.RequestError as e:
        raise ValueError(f"Request error occurred: {e}") from e


def process_data(text: str, pattern: str):
    """Process the given text with the provided regex pattern."""
    try:
        compiled_pattern = re.compile(pattern)
        return compiled_pattern.findall(text)
    except re.error as e:
        raise ValueError(f"Invalid regex pattern: {e}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error: {e}") from e
