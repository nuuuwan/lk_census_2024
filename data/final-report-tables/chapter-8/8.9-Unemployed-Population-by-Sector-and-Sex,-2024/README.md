# Unemployed Population by Sector and Sex, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 8.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=171",
        "source_description": [
            "Table 8.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "UnemploymentBySectorAndSex": "Unemployed Population by Sector and Sex, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "sector"
        ]
    },
    "UnemploymentBySectorAndSex": {
        "2024": {
            "Urban": {
                "sector": "Urban",
                "values": {
                    "Female": 44965,
                    "Male": 43342
                },
                "total_value": 88307,
                "pct_values": {
                    "Female": 0.5092,
                    "Male": 0.4908
                }
            },
            "Estate - Urban": {
                "sector": "Estate - Urban",
...
```

- Source File: [lanka_data.json (1.6 kB)](../../../../data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Urban",
        "values": {
            "male": 43342,
            "female": 44965
        },
        "total_value": 88307
    },
    {
        "sector": "Estate - Urban",
        "values": {
            "male": 151,
            "female": 112
        },
        "total_value": 263
    },
    {
        "sector": "Rural",
        "values": {
            "male": 175144,
            "female": 199089
        },
        "total_value": 374233
    },
    {
        "sector": "Estate - Rural",
        "values": {
            "male": 14034,
            "female": 14872
...
```

- Source File: [data.json (509 B)](../../../../data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "Census of Population and Housing - 2024",
        "",
        "",
        "",
        ""
    ],
    [
        "8.7 Unemployed Population (Unemployment)",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "The unemployed population refers to individuals who were not engaged in any economic activity during",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "the reference period but were actively seeking employment and have taken steps to find employment in",
...
```
- Source File: [raw_data.json (2.0 kB)](../../../../data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024/original.png)

- Source File: [original.pdf (54.4 kB)](../../../../data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=171>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
