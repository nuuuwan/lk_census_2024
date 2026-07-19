# of Housing Units and Status of Housing Units, by Sector and District, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 11.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:LK-11": {
                "TypeOfUnit:Permanent": {
                    "Count": "Int:645260"
                },
                "TypeOfUnit:SemiPermanent": {
                    "Count": "Int:8256"
                },
                "TypeOfUnit:Improvised": {
                    "Count": "Int:195"
                },
                "TypeOfUnit:NotPermanent": {
                    "Count": "Int:340"
                }
            },
            "District:LK-12": {
                "TypeOfUnit:Permanent": {
                    "Count": "Int:673967"
                },
                "TypeOfUnit:SemiPermanent": {
                    "Count": "Int:8381"
                },
                "TypeOfUnit:Improvised": {
                    "Count": "Int:404"
                },
                "TypeOfUnit:NotPermanent": {
                    "Count": "Int:273"
                }
...
```

- Source File: [lanka_data.json (8.4 KB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/lanka_data.json)

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

- Source File: [data.json (14.3 KB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/data.json)

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
- Source File: [raw_data.json (5.8 KB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/original.png)

- Source File: [original.pdf (90.6 KB)](../../../../data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=207>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
