# Administrative Structure by District, 1981

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 2.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=62",
        "source_description": [
            "Table 2.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "AdministrativeStructure": "Administrative Structure by District, 1981"
        },
        "when": "1981",
        "where_who_types": [
            "province",
            "country",
            "district",
            "ed"
        ]
    },
    "AdministrativeStructure": {
        "1981": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "GramaSevakaDivisions": 121,
                    "AssistantGovernmentAgendDivisions": 8,
                    "TownCouncils": 6,
                    "UrbanCouncils": 4,
                    "MunicipalCouncils": 2
                },
...
```

- Source File: [lanka_data.json (34.3 kB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "assistant_government_agend_divisions": 8,
            "grama_sevaka_divisions": 121,
            "municipal_councils": 2,
            "urban_councils": 4,
            "town_councils": 6
        },
        "total_value": 141
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "assistant_government_agend_divisions": 13,
            "grama_sevaka_divisions": 389,
            "municipal_councils": 1,
            "urban_councils": 6,
            "town_councils": 9
        },
        "total_value": 418
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
...
```

- Source File: [data.json (17.6 kB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Government Agent",
        "Sewaka",
        "Councils",
        "Urban Councils",
        "Town Councils"
    ],
    [
        "",
        "Divisions",
        "Divisions",
        "",
        "",
        ""
    ],
    [
        "Total",
        "245",
        "4,113",
        "12",
        "39",
        "83"
    ],
    [
        "Colombo",
        "8",
        "121",
        "2",
...
```
- Source File: [raw_data.json (2.2 kB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/original.png)

- Source File: [original.pdf (91.7 kB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=62>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
