# In, Out and Net Lifetime Migrants by District, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 5.1.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:LK-11": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:491236"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:299712"
                }
            },
            "District:LK-12": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:490861"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:133333"
                }
            },
            "District:LK-13": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:180877"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:118645"
                }
            },
            "District:LK-21": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:157921"
...
```

- Source File: [lanka_data.json (5.1 KB)](../../../../data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 491236,
            "out_migrants": 299712
        }
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 490861,
            "out_migrants": 133333
        }
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 180877,
            "out_migrants": 118645
        }
    },
    {
        "region_id": "LK-21",
...
```

- Source File: [data.json (4.4 KB)](../../../../data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Lifetime",
        "Lifetime",
        "Lifetime",
        "Migration \nEffectiveness Ratio"
    ],
    [
        "District",
        "In-migrants",
        "Out-migrants",
        "Net-migrants",
        ""
    ],
    [
        "",
        "(1)",
        "(2)",
        "(1) - (2) = (3)",
        "((3)/ (1) +(2)) *100"
    ],
    [
        "Colombo",
        "491,236",
        "299,712",
        "+191,524",
        "24.2"
    ],
    [
...
```
- Source File: [raw_data.json (2.6 KB)](../../../../data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024/original.png)

- Source File: [original.pdf (97.7 KB)](../../../../data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=84>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
