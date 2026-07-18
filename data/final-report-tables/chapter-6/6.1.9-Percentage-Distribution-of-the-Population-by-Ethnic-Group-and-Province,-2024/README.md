# Percentage Distribution of the Population by Ethnic Group and Province, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 6.1.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=112",
        "source_description": "Table 6.1.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka",
        "what": {
            "Ethnicity": "Percentage Distribution of the Population by Ethnic Group and Province, 2024"
        },
        "when": [
            "2024"
        ],
        "where_who_types": [
            "province"
        ]
    },
    "Ethnicity": {
        "2024": {
            "LK-1": {
                "region_id": "LK-1",
                "region_name": "Western",
                "region_ent_type": "province",
                "pct_values": {
                    "Sinhalese": 0.836,
                    "SlMoor": 0.089,
                    "SlTamil": 0.063,
                    "IndAndMalaiyagaTamil": 0.005,
                    "Malay": 0.003,
                    "Burgher": 0.003,
                    "Other": 0.001,
                    "SlChetty": 0.0,
                    "Bharatha": 0.0,
...
```

- Source File: [lanka_data.json (4.4 KB)](../../../../data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "p_sinhalese": 0.836,
            "p_sl_tamil": 0.063,
            "p_ind_and_malaiyaga_tamil": 0.005,
            "p_sl_moor": 0.089,
            "p_malay": 0.003,
            "p_burgher": 0.003,
            "p_sl_chetty": 0.0,
            "p_bharatha": 0.0,
            "p_veddahs": 0.0,
            "p_other": 0.001
        }
    },
    {
        "region_id": "LK-2",
        "region_name": "Central",
        "region_ent_type": "province",
        "values": {
            "p_sinhalese": 0.658,
            "p_sl_tamil": 0.083,
            "p_ind_and_malaiyaga_tamil": 0.15,
            "p_sl_moor": 0.107,
            "p_malay": 0.001,
            "p_burgher": 0.001,
            "p_sl_chetty": 0.0,
...
```

- Source File: [data.json (3.4 KB)](../../../../data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "0.5",
        "",
        "2012",
        "",
        "",
        "",
        "0.3",
        "2024",
        ""
    ],
    [
        "",
        "9.3",
        "",
        "",
        "",
        "Sinhalese",
        "",
        "10.5",
        "",
        "",
        "Sinhalese"
    ],
    [
        "4.1",
        "",
...
```
- Source File: [raw_data.json (2.5 KB)](../../../../data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024/original.png)

- Source File: [original.pdf (72.4 KB)](../../../../data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=112>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
