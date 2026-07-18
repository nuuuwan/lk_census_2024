# Percentage of Widowed Population Aged 15 Years and over, 1981, 2012, and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 9.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=181",
        "source_description": "Table 9.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka",
        "what": {
            "WidowedBySex": "Percentage of Widowed Population Aged 15 Years and over, 1981, 2012, and 2024"
        },
        "when": [
            "1981",
            "2012",
            "2024"
        ],
        "where_who_types": [
            "age_group"
        ]
    },
    "WidowedBySex": {
        "1981": {
            "Population 15 years and over": {
                "age_group": "Population 15 years and over",
                "pct_values": {
                    "WidowedFemale": 0.052,
                    "WidowedMale": 0.012
                }
            },
            "15-19": {
                "age_group": "15-19",
                "pct_values": {
                    "WidowedFemale": 0.001,
                    "WidowedMale": 0.0
...
```

- Source File: [lanka_data.json (6.2 KB)](../../../../data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "Population 15 years and over",
        "values": {
            "p_widowed_male_1981": 0.012,
            "p_widowed_male_2012": 0.013,
            "p_widowed_male_2024": 0.021,
            "p_widowed_female_1981": 0.052,
            "p_widowed_female_2012": 0.087,
            "p_widowed_female_2024": 0.117
        }
    },
    {
        "age_group": "15-19",
        "values": {
            "p_widowed_male_1981": 0.0,
            "p_widowed_male_2012": 0.0,
            "p_widowed_male_2024": 0.0,
            "p_widowed_female_1981": 0.001,
            "p_widowed_female_2012": 0.001,
            "p_widowed_female_2024": 0.0
        }
    },
    {
        "age_group": "20-24",
        "values": {
            "p_widowed_male_1981": 0.001,
            "p_widowed_male_2012": 0.0,
            "p_widowed_male_2024": 0.0,
            "p_widowed_female_1981": 0.005,
...
```

- Source File: [data.json (3.3 KB)](../../../../data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 9.6 : Percentage of Widowed Population Aged 15 Years and over, 1981, 2012, and 2024",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "Percentage of Widowed Persons",
        "",
        "",
        ""
    ],
    [
        "Age Group \n(Years)",
        "",
        "Male",
        "",
        "",
        "Female",
        ""
    ],
    [
        "",
...
```
- Source File: [raw_data.json (1.5 KB)](../../../../data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024/original.png)

- Source File: [original.pdf (56.3 KB)](../../../../data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=181>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
