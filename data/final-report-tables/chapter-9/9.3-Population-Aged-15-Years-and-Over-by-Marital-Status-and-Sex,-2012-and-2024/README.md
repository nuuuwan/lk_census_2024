# Population Aged 15 Years and Over by Marital Status and Sex, 2012 and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 9.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=178",
        "source_description": "Table 9.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka",
        "what": {
            "MaritalStatusBySex": "Population Aged 15 Years and Over by Marital Status and Sex, 2012 and 2024"
        },
        "when": [
            "2012",
            "2024"
        ],
        "where_who_types": [
            "marital_status"
        ]
    },
    "MaritalStatusBySex": {
        "2012": {
            "Never married": {
                "marital_status": "Never married",
                "values": {
                    "Male": 2179099,
                    "Female": 1748503
                },
                "total_value": 3927602,
                "pct_values": {
                    "Male": 0.5548,
                    "Female": 0.4452
                }
            },
            "Married": {
...
```

- Source File: [lanka_data.json (3.8 KB)](../../../../data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "marital_status": "Never married",
        "values": {
            "male_2012": 2179099,
            "female_2012": 1748503,
            "male_2024": 2527794,
            "female_2024": 2065535
        }
    },
    {
        "marital_status": "Married",
        "values": {
            "male_2012": 4921044,
            "female_2012": 5401061,
            "male_2024": 5417431,
            "female_2024": 5743629
        }
    },
    {
        "marital_status": "Widow",
        "values": {
            "male_2012": 97532,
            "female_2012": 695415,
            "male_2024": 175421,
            "female_2024": 1058997
        }
    },
    {
        "marital_status": "Divorced",
...
```

- Source File: [data.json (1.1 KB)](../../../../data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Marital status",
        "Male",
        "",
        "Female",
        "",
        "Male",
        "",
        "Female",
        ""
    ],
    [
        "",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%"
    ],
    [
        "Total",
        "7,266,234",
        "100.0",
        "7,961,539",
        "100.0",
        "",
...
```
- Source File: [raw_data.json (2.3 KB)](../../../../data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024/original.png)

- Source File: [original.pdf (125.1 KB)](../../../../data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=178>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
