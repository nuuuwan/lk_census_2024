# Administrative Structure by District, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 2.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "AdministrativeEntity": {
        "Time:2024": {
            "District:colombo": {
                "AdministrativeEntity:asst_govt_divisions": {
                    "Count": "Int:13"
                },
                "AdministrativeEntity:gs_divisions": {
                    "Count": "Int:557"
                },
                "AdministrativeEntity:municipal_councils": {
                    "Count": "Int:5"
                },
                "AdministrativeEntity:town_councils": {
                    "Count": "Int:5"
                },
                "AdministrativeEntity:urban_councils": {
                    "Count": "Int:3"
                }
            },
            "District:gampaha": {
                "AdministrativeEntity:asst_govt_divisions": {
                    "Count": "Int:13"
                },
                "AdministrativeEntity:gs_divisions": {
                    "Count": "Int:1177"
                },
                "AdministrativeEntity:municipal_councils": {
                    "Count": "Int:2"
                },
...
```

- Source File: [lanka_data.json (11.8 KB)](../../../../data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "AdministrativeEntity:asst_govt_divisions": 13,
            "AdministrativeEntity:gs_divisions": 557,
            "AdministrativeEntity:municipal_councils": 5,
            "AdministrativeEntity:town_councils": 5,
            "AdministrativeEntity:urban_councils": 3
        },
        "total_value": 583
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "AdministrativeEntity:asst_govt_divisions": 13,
            "AdministrativeEntity:gs_divisions": 1177,
            "AdministrativeEntity:municipal_councils": 2,
            "AdministrativeEntity:town_councils": 5,
            "AdministrativeEntity:urban_councils": 12
        },
        "total_value": 1209
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
...
```

- Source File: [data.json (22.0 KB)](../../../../data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Divisional",
        "Grama",
        "Number of",
        "Number of",
        "Number of"
    ],
    [
        "District",
        "Secretariat",
        "Niladhari",
        "Municipal",
        "Urban",
        "Pradeshiya Sabha"
    ],
    [
        "",
        "Divisions",
        "Divisions",
        "Councils",
        "Councils",
        ""
    ],
    [
        "Total",
        "340",
        "14,008",
        "29",
...
```
- Source File: [raw_data.json (4.1 KB)](../../../../data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District-2024/original.png)

- Source File: [original.pdf (54.3 KB)](../../../../data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=64>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
