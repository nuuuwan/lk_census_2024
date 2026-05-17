#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "[1/5] Downloading original docs..."
python3 workflows/original_docs_download.py

echo "[2/5] Extracting PDF data tables..."
python3 workflows/pdf_data_tables_extract.py

echo "[3/5] Extracting XLSX data tables..."
python3 workflows/xlsx_data_tables_extract.py

echo "[4/5] Building dataset READMEs..."
python3 workflows/dataset_readme_build.py

echo "[5/5] Building main README..."
python3 workflows/readme_build.py

echo "Done."
