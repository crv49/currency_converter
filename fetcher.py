# currency_converter/fetcher.py

import requests
import json
from typing import Any
from logger_config import setup_logging

logger = setup_logging()

MOCK_DATA_PATH = "data/mock_rates.json"
API_URL_TEMPLATE = "https://open.er-api.com/v6/latest/{base}"

def get_exchange_rate(base: str, target: str, use_mock: bool = False) -> float:
    if use_mock:
        logger.info(f"Using mock data for conversion from {base} to {target}")
        return get_mock_rate(base, target)
    else:
        logger.info(f"Fetching live rate from API for {base} to {target}")
        return get_live_rate(base, target)

def get_mock_rate(base: str, target: str) -> float:
    try:
        with open(MOCK_DATA_PATH) as f:
            data = json.load(f)

        if data.get("base") != base:
            raise ValueError(f"Base currency '{base}' not found in mock data.")

        rate = data.get("rates", {}).get(target)
        if rate is None:
            raise ValueError(f"Target currency '{target}' not found in mock data.")
        
        return rate

    except FileNotFoundError:
        logger.error("Mock rates file not found.")
        raise RuntimeError("Mock rates file is missing.")
    except json.JSONDecodeError:
        logger.error("Invalid JSON format in mock rates.")
        raise RuntimeError("Mock rates file is corrupted.")
    except Exception as e:
        logger.error(f"Unexpected error in mock fetch: {e}")
        raise

def get_live_rate(base: str, target: str) -> float:
    try:
        url = API_URL_TEMPLATE.format(base=base, target=target)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data: dict[str, Any] = response.json()
        logger.info(f"API response: {data}")  # Helpful for debugging

        rate = data.get("rates", {}).get(target)
        if rate is None:
            raise ValueError(f"Currency '{target}' not found in API response.")

        return rate

    except requests.RequestException as e:
        logger.error(f"Request error: {e}")
        raise ConnectionError("Failed to fetch rates from API.")
    except Exception as e:
        logger.error(f"Unexpected error in live fetch: {e}")
        raise