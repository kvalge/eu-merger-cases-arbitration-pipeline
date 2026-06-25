import os

URL = "https://compcases-open-data-portal-files-prod.s3.eu-west-1.amazonaws.com/case-data-M.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "..", "..", "data", "raw")
FILE_PREFIX = "case-data-M"
DATE_FORMAT = "%Y-%m-%d"
DOWNLOAD_REQUEST_TIMEOUT = 20
