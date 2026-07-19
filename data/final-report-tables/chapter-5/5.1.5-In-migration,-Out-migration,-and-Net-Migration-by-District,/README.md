# In-migration, Out-migration, and Net Migration by District,

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 5.1.5, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:LK-11": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:519379"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:384245"
                }
            },
            "District:LK-12": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:524737"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:155712"
                }
            },
            "District:LK-13": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:192833"
                },
                "MigrationDirection:OutMigrants": {
                    "Count": "Int:126566"
                }
            },
            "District:LK-21": {
                "MigrationDirection:InMigrants": {
                    "Count": "Int:172489"
...
```

- Source File: [lanka_data.json (5.1 KB)](../../../../data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 519379,
            "out_migrants": 384245
        }
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 524737,
            "out_migrants": 155712
        }
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
            "in_migrants": 192833,
            "out_migrants": 126566
        }
    },
    {
        "region_id": "LK-21",
...
```

- Source File: [data.json (4.4 KB)](../../../../data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 5.1.5 : In-migration, Out-migration, and Net Migration by District, 2024",
        "",
        ""
    ],
    [
        "District",
        "In migration",
        "Out migration",
        "Net migration"
    ],
    [
        "Colombo",
        "519,379",
        "384,245",
        "+135,134"
    ],
    [
        "Gampaha",
        "524,737",
        "155,712",
        "+369,025"
    ],
    [
        "Kalutara",
        "192,833",
        "126,566",
        "+66,267"
...
```
- Source File: [raw_data.json (3.1 KB)](../../../../data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,/original.png)

- Source File: [original.pdf (23.2 KB)](../../../../data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=89>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
