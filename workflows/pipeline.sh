#!/bin/bash
python3 workflows/xlsx_data_tables_extract.py

python3 workflows/dataset_readme_build.py

python3 workflows/readme_build.py

echo "Done."
