# Percentage Distribution of the Number and of Households by Sector, District and Household Type, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 10.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=193",
        "source_description": [
            "Table 10.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "HouseholdType": "Percentage Distribution of the Number and of Households by Sector, District and Household Type, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "province",
            "ed",
            "district",
            "country"
        ]
    },
    "HouseholdType": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "Nuclear": 368810,
                    "Extended": 204760,
                    "OnePerson": 69392,
                    "Composite": 18860
                },
                "total_value": 661822,
...
```

- Source File: [lanka_data.json (26.1 KB)](../../../../data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "one_person": 69392,
            "nuclear": 368810,
            "extended": 204760,
            "composite": 18860
        },
        "total_value": 661822
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "one_person": 79204,
            "nuclear": 378791,
            "extended": 220914,
            "composite": 9726
        },
        "total_value": 688635
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
...
```

- Source File: [data.json (13.8 KB)](../../../../data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "10.5 Distribution of Households by Household Type"
    ],
    [
        "The total number of households in Sri Lanka is reported to be 6,111,315, with the largest number being"
    ],
    [
        "nuclear  households.  The  lowest  number  being  composite  households.  Accordingly,  more  than  50.0"
    ],
    [
        "percent of the total households in Sri Lanka are nuclear households.  Furthermore, it is noteworthy that"
    ],
    [
        "more than 50.0 percent of households in all sectors and districts are nuclear households."
    ],
    [
        "When considering the distribution of household types, nuclear households (58.9%) represent the largest"
    ],
    [
        "pecentage,  followed  by  extended  households  (29.7%),  one-person  households  (10.5%),  and  composite"
    ],
    [
        "households (0.9%), in descending order."
    ],
    [
        "Sector and",
...
```
- Source File: [raw_data.json (6.0 KB)](../../../../data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024/original.png)

- Source File: [original.pdf (82.9 KB)](../../../../data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=193>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
