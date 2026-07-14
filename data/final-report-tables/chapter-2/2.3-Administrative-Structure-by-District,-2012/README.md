# Administrative Structure by District, 2012

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 2.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=63",
        "source_description": [
            "Table 2.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "AdministrativeStructure": "Administrative Structure by District, 2012"
        },
        "when": "2012",
        "where_who_types": [
            "ed",
            "province",
            "country",
            "district"
        ]
    },
    "AdministrativeStructure": {
        "2012": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "GramaSevakaDivisions": 557,
                    "AssistantGovernmentAgendDivisions": 13,
                    "MunicipalCouncils": 5,
                    "UrbanCouncils": 5,
                    "TownCouncils": 3
                },
...
```

- Source File: [lanka_data.json (35.1 kB)](../../../../data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "assistant_government_agend_divisions": 13,
            "grama_sevaka_divisions": 557,
            "municipal_councils": 5,
            "urban_councils": 5,
            "town_councils": 3
        },
        "total_value": 583
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "assistant_government_agend_divisions": 13,
            "grama_sevaka_divisions": 1177,
            "municipal_councils": 2,
            "urban_councils": 5,
            "town_councils": 12
        },
        "total_value": 1209
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
...
```

- Source File: [data.json (18.0 kB)](../../../../data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Secretariat",
        "Divisions",
        "Councils",
        "Councils",
        "Sabha"
    ],
    [
        "",
        "Divisions",
        "",
        "",
        "",
        ""
    ],
    [
        "Total",
        "331",
        "14,021",
        "23",
        "41",
        "271"
    ],
    [
        "Colombo",
        "13",
        "557",
        "5",
...
```
- Source File: [raw_data.json (2.1 kB)](../../../../data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012/raw_data.json)

## Original PDF

![Download the original PDF](../../../../data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012/original.png)

- Source File: [original.pdf (72.0 kB)](../../../../data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=63>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
