# EU Merger Cases Arbitration Pipeline

A data pipeline that downloads EU merger case data from the European Commission webpage https://data.europa.eu/data/datasets/cc7e224e-6569-40f0-8037-d3389aa0fae7?locale=en, 
processes PDF documents to detect arbitration-related clauses, and outputs structured CSV files.

## Pipeline Overview

1. Download merger cases JSON from European Commission
2. Process decision-related PDF documents
3. Extract text from PDFs and scan for arbitration keywords
4. Export processed data to CSV

## Tech Stack

- Python
    - requests
    - pdfplumber (or similar)

## Project Structure

## Setup

```bash
git clone https://github.com/kasutajanimi/eu-merger-cases-arbitration-pipeline.git
cd eu-merger-cases-arbitration-pipeline
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Status

In progress