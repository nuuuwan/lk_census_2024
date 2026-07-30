# Percentage Distribution of Ever-Married Women Aged 15 Years and Over by the Number of Live Births perWoman and Sector, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 9.12, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Sector:urban": {
                "LiveBirths:0": {
                    "FemalePopulationCount": "Int:155824"
                },
                "LiveBirths:1": {
                    "FemalePopulationCount": "Int:257291"
                },
                "LiveBirths:2": {
                    "FemalePopulationCount": "Int:410700"
                },
                "LiveBirths:3": {
                    "FemalePopulationCount": "Int:240380"
                },
                "LiveBirths:4": {
                    "FemalePopulationCount": "Int:83348"
                },
                "LiveBirths:5": {
                    "FemalePopulationCount": "Int:32614"
                },
                "LiveBirths:6": {
                    "FemalePopulationCount": "Int:14495"
                },
                "LiveBirths:7_or_more": {
                    "FemalePopulationCount": "Int:13287"
                }
            },
            "Sector:rural": {
...
```

- Source File: [lanka_data.json (2.1 KB)](../../../../data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "All Sectors",
        "values": {
            "0": 739589,
            "1": 1325678,
            "2": 2323426,
            "3": 1562905,
            "4": 565158,
            "5": 237227,
            "6": 111636,
            "7_plus": 111636
        },
        "total_value": 6977254
    },
    {
        "sector": "Urban*",
        "values": {
            "0": 155824,
            "1": 257291,
            "2": 410700,
            "3": 240380,
            "4": 83348,
            "5": 32614,
            "6": 14495,
            "7_plus": 13287
        },
        "total_value": 1207941
    },
    {
...
```

- Source File: [data.json (960.0 B)](../../../../data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "",
        "Woman and Sector, 2024",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Sector",
        "Number of Ever-\nMarried Women Aged",
        "",
        "",
        "Percentage of women by number of Live Births",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "15 Years and Over",
...
```
- Source File: [raw_data.json (1016.0 B)](../../../../data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector-2024/original.png)

- Source File: [original.pdf (80.7 KB)](../../../../data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector-2024/original.pdf)

(Table 1 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=184>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
