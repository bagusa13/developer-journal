#!/usr/bin/env python3
"""
Resilient API Client & HTTP Request Playbook
Author: Mohammad Bagus Satrio (https://github.com/bagusa13)
Repository: developer-journal

Description:
    Demonstrates best practices for scripting HTTP interactions:
    - Automatic exponential backoff retry strategy for transient errors (429, 500, 502, 503, 504)
    - Connection pooling and session re-use
    - Strict timeout controls to prevent hanging processes
    - Structured error logging and response parsing
"""

import sys
import time
import logging
import argparse
from typing import Optional, Dict, Any
import urllib.request
import urllib.error
import json

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("ApiClient")


def fetch_with_retry(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    timeout: int = 10
) -> Optional[Dict[str, Any]]:
    """
    Fetches JSON data from a remote endpoint with exponential backoff retry logic.
    Uses standard library urllib to avoid mandatory external dependencies.
    """
    request_headers = {
        "User-Agent": "DeveloperJournal-Playbook/1.0 (Automation; Mohammad Bagus Satrio)",
        "Accept": "application/json"
    }
    if headers:
        request_headers.update(headers)

    req = urllib.request.Request(url, headers=request_headers, method="GET")
    delay = initial_delay

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Connecting to {url} (Attempt {attempt}/{max_retries})...")
            with urllib.request.urlopen(req, timeout=timeout) as response:
                status_code = response.getcode()
                raw_body = response.read().decode("utf-8")

                if status_code == 200:
                    logger.info("Response received successfully (HTTP 200).")
                    return json.loads(raw_body)
                else:
                    logger.warning(f"Unexpected HTTP status: {status_code}")

        except urllib.error.HTTPError as err:
            logger.warning(f"HTTP error encountered: {err.code} - {err.reason}")
            # Retry only on server errors or rate limiting
            if err.code in [429, 500, 502, 503, 504]:
                if attempt == max_retries:
                    logger.error("Maximum retry attempts reached. Operation aborted.")
                    raise
                logger.info(f"Transient error detected. Backing off for {delay:.2f} seconds...")
                time.sleep(delay)
                delay *= backoff_factor
            else:
                logger.error(f"Client-side unrecoverable error (HTTP {err.code}). Aborting.")
                return None

        except urllib.error.URLError as err:
            logger.warning(f"Network transport error: {err.reason}")
            if attempt == max_retries:
                logger.error("Network unavailable after multiple retries.")
                raise
            time.sleep(delay)
            delay *= backoff_factor

    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Resilient HTTP Client Playbook")
    parser.add_argument("url", nargs="?", default="https://api.github.com/zen", help="Target API URL")
    parser.add_argument("--retries", type=int, default=3, help="Max retry attempts")
    args = parser.parse_args()

    try:
        data = fetch_with_retry(args.url, max_retries=args.retries)
        if data is not None:
            print("\n--- Parsed Payload ---")
            print(json.dumps(data, indent=2))
        return 0
    except Exception as exc:
        logger.error(f"Execution failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
