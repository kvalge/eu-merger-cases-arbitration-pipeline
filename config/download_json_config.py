import os

URL = "https://compcases-open-data-portal-files-prod.s3.eu-west-1.amazonaws.com/case-data-M.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
FILE_PREFIX = "case-data-M"
DATE_FORMAT = "%Y-%m-%d_%H-%M-%S"
DOWNLOAD_REQUEST_TIMEOUT = 20
