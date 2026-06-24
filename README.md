# EU Merger Cases Arbitration Pipeline

A Python-based data pipeline that downloads EU merger case data from the [European Commission open data portal](https://data.europa.eu/data/datasets/cc7e224e-6569-40f0-8037-d3389aa0fae7?locale=en), stores raw JSON data, and prepares a processing workflow for extracting arbitration-related information from PDF documents.

The goal of this project is to build an end-to-end data pipeline that:

- Ingests structured JSON data
- Stores raw datasets for reproducibility
- Processes PDF documents linked to merger cases
- Extracts arbitration-related content using keyword detection
- Outputs structured CSV datasets for analysis

---

## Pipeline Overview

The pipeline is designed in modular stages:

1. **Ingestion**
   - Download merger case data (JSON) from European Commission source
   - Validate HTTP responses
   - Store raw JSON files locally with timestamps

2. **Exploration (WIP)**
   - Inspect dataset structure
   - Identify key fields and metadata
   - Locate PDF document references

3. **Processing (Planned)**
   - Download and parse PDF documents
   - Extract text content
   - Detect arbitration-related clauses

4. **Output (Planned)**
   - Generate structured CSV files for analysis

---

## Tech Stack

- Python 3.x
- requests – HTTP data ingestion
- json – data serialization
- logging – pipeline observability
- pathlib / os – file system handling
- pdfplumber (planned) – PDF text extraction
- pandas (planned) – structured output generation

---

## Project Structure

```
├── config/
│   ├── __init__.py
│   └── config.py
├── data/
│   └── raw/              # Raw ingested JSON files (created at runtime)
├── scripts/
│   └── ingest/
│       └── download_json.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone https://github.com/kvalge/eu-merger-cases-arbitration-pipeline.git
cd eu-merger-cases-arbitration-pipeline

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

---

## Usage

### Run ingestion pipeline

```bash
python -m scripts.ingest.download_json
```

### Run exploration (coming soon)

```bash
python -m scripts.explore.explore_json
```

---

## Current Features

- Download EU merger case dataset from official EC source
- Validate HTTP responses with proper error handling
- Save raw JSON file with date-based versioning
- Structured logging for pipeline observability
- Modular project structure (ingest / explore / transform-ready)

---

## Status

Work in progress

**Next steps:**

- Build dataset exploration module
- Extract PDF links from JSON
- Implement PDF text extraction pipeline
- Detect arbitration-related keywords
- Export structured CSV datasets

---

## Design Principles

- Fail-fast pipeline design (no silent failures)
- Modular separation of ingestion and processing
- Reproducible raw data storage
- Logging-based observability instead of print statements

---

## License

MIT (or specify later)
