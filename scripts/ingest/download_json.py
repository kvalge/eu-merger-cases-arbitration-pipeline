# download_json.py

import json
import os
import requests
from datetime import datetime

URL = "https://compcases-open-data-portal-files-prod.s3.eu-west-1.amazonaws.com/case-data-M.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def download_json(url: str = URL) -> requests.Response:
    response = requests.get(url, timeout=20)
    return response

def validate_response(response: requests.Response):
    if response.status_code != 200:
        raise ValueError(f"Invalid response: {response.status_code}")

def save_raw_json(data, file) -> None:
    save_dir = os.path.join(BASE_DIR, "..", "..", "data", "raw")
    os.makedirs(save_dir, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{file}_{date_str}.json"
    file_path = os.path.join(save_dir, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def run_pipeline():
    response = download_json()
    validate_response(response)
    data = response.json()
    save_raw_json(data, "case-data-M")

if __name__ == "__main__":
    run_pipeline()