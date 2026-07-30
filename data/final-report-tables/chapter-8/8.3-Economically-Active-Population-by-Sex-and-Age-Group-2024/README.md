# Economically Active Population by Sex and Age Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 8.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "AgeGroup:0To125Years": {
                "Sex:male": {
                    "CountEconomicallyActive": "Int:5550374"
                },
                "Sex:female": {
                    "CountEconomicallyActive": "Int:2612567"
                }
            },
            "AgeGroup:15To19Years": {
                "Sex:male": {
                    "CountEconomicallyActive": "Int:105358"
                },
                "Sex:female": {
                    "CountEconomicallyActive": "Int:44085"
                }
            },
            "AgeGroup:20To24Years": {
                "Sex:male": {
                    "CountEconomicallyActive": "Int:431002"
                },
                "Sex:female": {
                    "CountEconomicallyActive": "Int:229585"
                }
            },
            "AgeGroup:25To29Years": {
                "Sex:male": {
                    "CountEconomicallyActive": "Int:548881"
...
```

- Source File: [lanka_data.json (2.9 KB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "Sri Lanka",
        "values": {
            "male": 5550374,
            "female": 2612567
        },
        "total_value": 8162941
    },
    {
        "age_group": "15 - 19",
        "values": {
            "male": 105358,
            "female": 44085
        },
        "total_value": 149443
    },
    {
        "age_group": "20 - 24",
        "values": {
            "male": 431002,
            "female": 229585
        },
        "total_value": 660587
    },
    {
        "age_group": "25 - 29",
        "values": {
            "male": 548881,
            "female": 289710
...
```

- Source File: [data.json (1.8 KB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group-2024/data.json)

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
- Source File: [raw_data.json (2.0 KB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group-2024/original.png)

- Source File: [original.pdf (56.6 KB)](../../../../data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=165>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
