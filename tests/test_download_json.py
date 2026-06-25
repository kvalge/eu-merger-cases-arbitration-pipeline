# test_download_json.py
# run command: pytest tests/test_download_json.py
# run command to stop after first failure: pytest tests/test_download_json.py -x


import os
from datetime import datetime
from unittest.mock import Mock, patch

import requests

from config.download_json_config import DOWNLOAD_REQUEST_TIMEOUT, FILE_PREFIX, URL

from scripts.ingest.download_json import (
    download_json,
    build_raw_file_path,
    save_raw_json,
    validate_response,
)


@patch("scripts.ingest.download_json.requests.get")
def test_download_json_calls_requests_get(mock_get):
    mock_response = Mock(spec=requests.Response)
    mock_get.return_value = mock_response

    result = download_json()

    mock_get.assert_called_once_with(
        URL,
        timeout=DOWNLOAD_REQUEST_TIMEOUT
    )

    assert result == mock_response


def test_download_json_source_url_is_reachable():
    response = download_json(URL)

    validate_response(response)

    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


@patch("scripts.ingest.download_json.datetime")
@patch("scripts.ingest.download_json.RAW_DATA_DIR", os.path.join("data", "raw"))
def test_build_raw_file_path_contains_prefix_and_extension(mock_datetime):
    mock_datetime.now.return_value = datetime(2026, 6, 25, 14, 30, 45)

    file_path = build_raw_file_path()

    assert os.path.basename(file_path).startswith(FILE_PREFIX)
    assert file_path.endswith(".json")
    assert file_path == os.path.join(
        "data", "raw", f"{FILE_PREFIX}_2026-06-25_14-30-45.json"
    )


def test_save_raw_json_creates_file(tmp_path, monkeypatch):
    sample_data = {"test": "value"}

    monkeypatch.setattr(
        "scripts.ingest.download_json.RAW_DATA_DIR",
        str(tmp_path)
    )

    file_path = save_raw_json(sample_data)

    assert os.path.exists(file_path)

    with open(file_path, encoding="utf-8") as f:
        assert '"test": "value"' in f.read()


