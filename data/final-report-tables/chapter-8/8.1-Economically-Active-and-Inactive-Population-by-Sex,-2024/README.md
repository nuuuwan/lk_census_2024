# Economically Active and Inactive Population by Sex, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 8.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=163",
        "source_description": [
            "Table 8.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "EconomicActivityBySex": "Economically Active and Inactive Population by Sex, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "sex"
        ]
    },
    "EconomicActivityBySex": {
        "2024": {
            "Male": {
                "sex": "Male",
                "values": {
                    "EconomicallyActive": 5550374,
                    "EconomicallyInactive": 2681440
                },
                "total_value": 8231814,
                "pct_values": {
                    "EconomicallyActive": 0.6743,
                    "EconomicallyInactive": 0.3257
                }
            },
            "Female": {
                "sex": "Female",
...
```

- Source File: [lanka_data.json (1.1 kB)](../../../../data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sex": "Male",
        "values": {
            "economically_active": 5550374,
            "economically_inactive": 2681440
        },
        "total_value": 8231814
    },
    {
        "sex": "Female",
        "values": {
            "economically_active": 2612567,
            "economically_inactive": 6430580
        },
        "total_value": 9043147
    }
]
```

- Source File: [data.json (314 B)](../../../../data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing - 2024"
    ],
    [
        "8.3 Working-Age Population"
    ],
    [
        "According to the current Census of Population and Housing, the population aged 15 years and over is"
    ],
    [
        "reported  as  17,274,961.  Of  this  total,  8,231,814  are  males  and  9,043,147  are  females.  During  the"
    ],
    [
        "relevant reference period, the number of economically active individuals was 8,162,941. Among them,"
    ],
    [
        "7,671,232 were employed, while the number of unemployed persons stood at  491,709. Despite being"
    ],
    [
        "within the working-age population, 9,112,020 individuals were identified as economically inactive based"
    ],
    [
        "on their activities during the reference period. This group consists of full-time students aged 15 and over,"
    ],
    [
        "those engaged in household duties, retirees, and individuals with illnesses or disabilities."
    ],
    [
        "",
...
```
- Source File: [raw_data.json (2.0 kB)](../../../../data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024/original.png)

- Source File: [original.pdf (33.1 kB)](../../../../data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=163>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
