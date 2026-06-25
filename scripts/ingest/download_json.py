# download_json.py

# run command: python -m scripts.ingest.download_json

import os
import json
import logging
from datetime import datetime

import requests

from config.download_json_config import DATE_FORMAT, DOWNLOAD_REQUEST_TIMEOUT, FILE_PREFIX, RAW_DATA_DIR, URL
from config.logging_config import configure_logging


logger = logging.getLogger(__name__)


def download_json(url: str = URL) -> requests.Response:
    response = requests.get(url, timeout=DOWNLOAD_REQUEST_TIMEOUT)
    return response


def validate_response(response: requests.Response) -> None:
    response.raise_for_status()


def save_raw_json(data: dict) -> str:
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    file_path = build_raw_file_path()

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return file_path


def build_raw_file_path() -> str:
    timestamp_str = datetime.now().strftime(DATE_FORMAT)

    file_name = f"{FILE_PREFIX}_{timestamp_str}.json"

    return os.path.join(RAW_DATA_DIR, file_name)


def run_pipeline() -> None:
    try:
        logger.info(f"Starting download of merger case data from source URL: {URL}")

        response = download_json()

        validate_response(response)

        logger.info(
            f"HTTP response validation completed"
            f"(status_code={response.status_code})"
        )

        data = response.json()

        logger.info(
            f"Successfully parsed JSON payload"
            f"containing {len(data):,} merger cases"
        )

        saved_file = save_raw_json(data)

        logger.info(f"Raw dataset successfully saved to file: {saved_file}")

        logger.info("Merger cases ingestion pipeline completed successfully")

    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    configure_logging()
    run_pipeline()
