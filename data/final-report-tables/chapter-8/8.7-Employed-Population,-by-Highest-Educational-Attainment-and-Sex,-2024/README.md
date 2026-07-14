# Employed Population, by Highest Educational Attainment and Sex, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 8.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=169",
        "source_description": [
            "Table 8.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "EmploymentByEducationAndSex": "Employed Population, by Highest Educational Attainment and Sex, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "educational_level"
        ]
    },
    "EmploymentByEducationAndSex": {
        "2024": {
            "Never attended School": {
                "educational_level": "Never attended School",
                "values": {
                    "Male": 67915,
                    "Female": 49378
                },
                "total_value": 117293,
                "pct_values": {
                    "Male": 0.579,
                    "Female": 0.421
                }
            },
            "Studied in a special school / special unit": {
                "educational_level": "Studied in a special school / special unit",
...
```

- Source File: [lanka_data.json (2.9 kB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "educational_level": "Never attended School",
        "values": {
            "male": 67915,
            "female": 49378
        },
        "total_value": 117293
    },
    {
        "educational_level": "Studied in a special school / special unit",
        "values": {
            "male": 3923,
            "female": 2719
        },
        "total_value": 6642
    },
    {
        "educational_level": "Passed Grade 1 - 5",
        "values": {
            "male": 493163,
            "female": 183967
        },
        "total_value": 677130
    },
    {
        "educational_level": "Passed Grade 6 - 8",
        "values": {
            "male": 618673,
            "female": 171412
...
```

- Source File: [data.json (1.2 kB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 8.7 : Employed Population, by Highest Educational Attainment and Sex, 2024",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Education level",
        "Total",
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
        "%"
    ],
    [
        "Total",
...
```
- Source File: [raw_data.json (2.2 kB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/raw_data.json)

## Original PDF

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/original.png)

- Source File: [original.pdf (62.3 kB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=169>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
