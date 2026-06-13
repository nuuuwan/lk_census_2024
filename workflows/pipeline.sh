#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "[1/4] Downloading original docs..."
python3 workflows/original_docs_download.py

echo "[2/4] Extracting XLSX data tables..."
python3 workflows/xlsx_data_tables_extract.py

echo "[3/4] Building dataset READMEs..."
python3 workflows/dataset_readme_build.py

echo "[4/4] Building main README..."
python3 workflows/readme_build.py

echo "Done."

git add data
git add README.md

git commit -m "Ran pipeline.sh"