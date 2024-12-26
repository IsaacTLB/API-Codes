import httpx
from utils.config import SCRAPER_URL


async def get_scraper_data(payload: dict):
    """Fetch scraper data by sending a POST request with the given payload."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{SCRAPER_URL}/scrape", json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
    except httpx.RequestError as e:
        raise ValueError(f"Request failed: {e}") from e
    except httpx.HTTPStatusError as e:
        raise ValueError(f"HTTP error occurred: {e.response.status_code}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error occurred: {e}") from e


async def scrape_data(url: str):
    """Asynchronously scrape data from the given URL."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Will raise an error for non-2xx status codes
            return response.text  # Return the page content as text
    except httpx.RequestError as e:
        raise ValueError(f"Request failed: {e}") from e
    except httpx.HTTPStatusError as e:
        raise ValueError(f"HTTP error occurred: {e.response.status_code}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error occurred: {e}") from e
