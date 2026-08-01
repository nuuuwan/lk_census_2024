# Employed Population by Sector and Sex, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 8.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Sector:urban": {
                "Sex:male": {
                    "EconomicallyActive": "Int:900141"
                },
                "Sex:female": {
                    "EconomicallyActive": "Int:393746"
                }
            },
            "Sector:estate_urban": {
                "Sex:male": {
                    "EconomicallyActive": "Int:3025"
                },
                "Sex:female": {
                    "EconomicallyActive": "Int:1577"
                }
            },
            "Sector:rural": {
                "Sex:male": {
                    "EconomicallyActive": "Int:4220045"
                },
                "Sex:female": {
                    "EconomicallyActive": "Int:1847052"
                }
            },
            "Sector:estate_rural": {
                "Sex:male": {
                    "EconomicallyActive": "Int:194492"
...
```

- Source File: [lanka_data.json (817.0 B)](../../../../data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Urban",
        "values": {
            "male": 900141,
            "female": 393746
        },
        "total_value": 1293887
    },
    {
        "sector": "Estate - Urban",
        "values": {
            "male": 3025,
            "female": 1577
        },
        "total_value": 4602
    },
    {
        "sector": "Rural",
        "values": {
            "male": 4220045,
            "female": 1847052
        },
        "total_value": 6067097
    },
    {
        "sector": "Estate - Rural",
        "values": {
            "male": 194492,
            "female": 111154
...
```

- Source File: [data.json (522.0 B)](../../../../data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "Table 8.6 : Employed Population by Sector and Sex, 2024",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "Employed population",
        "",
        "",
        ""
    ],
    [
        "Sector",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
...
```
- Source File: [raw_data.json (1.5 KB)](../../../../data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex-2024/original.png)

- Source File: [original.pdf (37.0 KB)](../../../../data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=168>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
