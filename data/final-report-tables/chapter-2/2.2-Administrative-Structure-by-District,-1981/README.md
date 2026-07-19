# Administrative Structure by District, 1981

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 2.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "District": {
        "Time:1981": {
            "District:LK-11": {
                "AdministrativeEntity:AssistantGovernmentAgendDivisions": {
                    "Count": "Int:8"
                },
                "AdministrativeEntity:GramaSevakaDivisions": {
                    "Count": "Int:121"
                },
                "AdministrativeEntity:MunicipalCouncils": {
                    "Count": "Int:2"
                },
                "AdministrativeEntity:UrbanCouncils": {
                    "Count": "Int:4"
                },
                "AdministrativeEntity:TownCouncils": {
                    "Count": "Int:6"
                }
            },
            "District:LK-12": {
                "AdministrativeEntity:AssistantGovernmentAgendDivisions": {
                    "Count": "Int:13"
                },
                "AdministrativeEntity:GramaSevakaDivisions": {
                    "Count": "Int:389"
                },
                "AdministrativeEntity:MunicipalCouncils": {
                    "Count": "Int:1"
                },
...
```

- Source File: [lanka_data.json (11.7 KB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "AdministrativeEntity:AssistantGovernmentAgendDivisions": 8,
            "AdministrativeEntity:GramaSevakaDivisions": 121,
            "AdministrativeEntity:MunicipalCouncils": 2,
            "AdministrativeEntity:UrbanCouncils": 4,
            "AdministrativeEntity:TownCouncils": 6
        },
        "total_value": 141
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "AdministrativeEntity:AssistantGovernmentAgendDivisions": 13,
            "AdministrativeEntity:GramaSevakaDivisions": 389,
            "AdministrativeEntity:MunicipalCouncils": 1,
            "AdministrativeEntity:UrbanCouncils": 6,
            "AdministrativeEntity:TownCouncils": 9
        },
        "total_value": 418
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
...
```

- Source File: [data.json (22.5 KB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/data.json)

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
- Source File: [raw_data.json (2.1 KB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/original.png)

- Source File: [original.pdf (89.6 KB)](../../../../data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=62>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
