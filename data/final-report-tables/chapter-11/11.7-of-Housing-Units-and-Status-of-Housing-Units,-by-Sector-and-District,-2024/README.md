# of Housing Units and Status of Housing Units, by Sector and District, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 11.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=207",
        "source_description": [
            "Table 11.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "HouseholdStatus": "of Housing Units and Status of Housing Units, by Sector and District, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "ed",
            "country",
            "district",
            "province"
        ]
    },
    "HouseholdStatus": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "Permanent": 645260,
                    "SemiPermanent": 8256,
                    "NotPermanent": 340,
                    "Improvised": 195
                },
                "total_value": 654051,
...
```

- Source File: [lanka_data.json (27.8 kB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "permanent": 645260,
            "semi_permanent": 8256,
            "improvised": 195,
            "not_permanent": 340
        },
        "total_value": 654051
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "permanent": 673967,
            "semi_permanent": 8381,
            "improvised": 404,
            "not_permanent": 273
        },
        "total_value": 683025
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
...
```

- Source File: [data.json (14.7 kB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 11.7 :Number of Housing Units and Status of Housing Units, by Sector and District, 2024",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "Housing units",
        "",
        "",
        "",
        "",
        "Status of housing units",
        "",
        "",
        "",
        ""
    ],
    [
        "Sector/District",
        "Total",
...
```
- Source File: [raw_data.json (6.0 kB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/original.png)

- Source File: [original.pdf (92.8 kB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=207>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
