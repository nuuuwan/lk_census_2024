# Officers who have  Assigned for Census of Population and Housing 2024 Activities

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 1.1.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:colombo": {
                "CensusOfficer:area_supervisors": {
                    "Count": "Int:14"
                },
                "CensusOfficer:asst_commissioners": {
                    "Count": "Int:14"
                },
                "CensusOfficer:circle_officers": {
                    "Count": "Int:18"
                },
                "CensusOfficer:deputy_commissioners": {
                    "Count": "Int:13"
                },
                "CensusOfficer:divisional_officer": {
                    "Count": "Int:53"
                },
                "CensusOfficer:enumerators_byoad": {
                    "Count": "Int:98"
                },
                "CensusOfficer:enumerators_capi": {
                    "Count": "Int:70"
                },
                "CensusOfficer:other_non_technical": {
                    "Count": "Int:1104"
                },
                "CensusOfficer:zonal_supervisors": {
                    "Count": "Int:1986"
...
```

- Source File: [lanka_data.json (19.5 KB)](../../../../data/final-report-tables/chapter-1/1.1.1-Officers-who-have-Assigned-for-Census-of-Population-and-Housing-2024-Activities/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "CensusOfficer:area_supervisors": 14,
            "CensusOfficer:asst_commissioners": 14,
            "CensusOfficer:circle_officers": 18,
            "CensusOfficer:deputy_commissioners": 13,
            "CensusOfficer:divisional_officer": 53,
            "CensusOfficer:enumerators_byoad": 98,
            "CensusOfficer:enumerators_capi": 70,
            "CensusOfficer:other_non_technical": 1104,
            "CensusOfficer:zonal_supervisors": 1986
        },
        "total_value": 3370
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "CensusOfficer:area_supervisors": 14,
            "CensusOfficer:asst_commissioners": 14,
            "CensusOfficer:circle_officers": 13,
            "CensusOfficer:deputy_commissioners": 13,
            "CensusOfficer:divisional_officer": 48,
            "CensusOfficer:enumerators_byoad": 90,
            "CensusOfficer:enumerators_capi": 70,
...
```

- Source File: [data.json (30.9 KB)](../../../../data/final-report-tables/chapter-1/1.1.1-Officers-who-have-Assigned-for-Census-of-Population-and-Housing-2024-Activities/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Total",
        "365",
        "365",
        "120",
        "Officer \n340",
        "601",
        "1,026",
        "1,825",
        "15,321",
        "14,396"
    ],
    [
        "Colombo",
        "14",
        "14",
        "18",
        "13",
        "53",
        "98",
        "70",
        "1,104",
        "1,986"
    ],
    [
        "Gampaha",
        "14",
        "14",
        "13",
...
```
- Source File: [raw_data.json (3.0 KB)](../../../../data/final-report-tables/chapter-1/1.1.1-Officers-who-have-Assigned-for-Census-of-Population-and-Housing-2024-Activities/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-1/1.1.1-Officers-who-have-Assigned-for-Census-of-Population-and-Housing-2024-Activities/original.png)

- Source File: [original.pdf (48.6 KB)](../../../../data/final-report-tables/chapter-1/1.1.1-Officers-who-have-Assigned-for-Census-of-Population-and-Housing-2024-Activities/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=23>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
