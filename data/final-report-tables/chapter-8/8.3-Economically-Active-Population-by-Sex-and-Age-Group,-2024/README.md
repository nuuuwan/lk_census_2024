# Economically Active Population by Sex and Age Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 8.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=165",
        "source_description": [
            "Table 8.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "EconomicActivityByAgeGroupAndSex": "Economically Active Population by Sex and Age Group, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "age_group"
        ]
    },
    "EconomicActivityByAgeGroupAndSex": {
        "2024": {
            "Sri Lanka": {
                "age_group": "Sri Lanka",
                "values": {
                    "MaleEconomicallyActive": 5550374,
                    "FemaleEconomicallyActive": 2612567
                },
                "total_value": 8162941,
                "pct_values": {
                    "MaleEconomicallyActive": 0.6799,
                    "FemaleEconomicallyActive": 0.3201
                }
            },
            "15 - 19": {
                "age_group": "15 - 19",
...
```

- Source File: [lanka_data.json (5.2 kB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "Sri Lanka",
        "values": {
            "male_economically_active": 5550374,
            "female_economically_active": 2612567
        },
        "total_value": 8162941
    },
    {
        "age_group": "15 - 19",
        "values": {
            "male_economically_active": 105358,
            "female_economically_active": 44085
        },
        "total_value": 149443
    },
    {
        "age_group": "20 - 24",
        "values": {
            "male_economically_active": 431002,
            "female_economically_active": 229585
        },
        "total_value": 660587
    },
    {
        "age_group": "25 - 29",
        "values": {
            "male_economically_active": 548881,
            "female_economically_active": 289710
...
```

- Source File: [data.json (2.4 kB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "Table 8.3 : Economically Active Population by Sex and Age Group, 2024",
        "",
        "",
        "",
        ""
    ],
    [
        "Age Group",
        "",
        "Economically Active Population",
        "",
        "",
        "Percentage",
        ""
    ],
    [
        "(Years)",
        "Total",
        "Male",
        "Female",
        "Total",
        "Male",
        "Female"
    ],
    [
        "Sri Lanka",
...
```
- Source File: [raw_data.json (2.0 kB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024/raw_data.json)

## Original PDF

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024/original.png)

- Source File: [original.pdf (58.0 kB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=165>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
