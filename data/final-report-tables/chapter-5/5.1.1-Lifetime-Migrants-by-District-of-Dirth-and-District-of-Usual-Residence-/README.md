# Lifetime Migrants by District of Dirth and District of Usual Residence,

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Table 5.1.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:colombo": {
                "MigrationStatus:local": {
                    "Count": "Int:1876288"
                },
                "MigrationStatus:foreign": {
                    "Count": "Int:7345"
                },
                "MigrationStatus:migrant": {
                    "Count": "Int:491236"
                }
            },
            "District:gampaha": {
                "MigrationStatus:local": {
                    "Count": "Int:1941334"
                },
                "MigrationStatus:foreign": {
                    "Count": "Int:3718"
                },
                "MigrationStatus:migrant": {
                    "Count": "Int:490861"
                }
            },
            "District:kalutara": {
                "MigrationStatus:local": {
                    "Count": "Int:1123880"
                },
                "MigrationStatus:foreign": {
...
```

- Source File: [lanka_data.json (6.7 KB)](../../../../data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence-/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "local": 1876288,
            "foreign": 7345,
            "migrant": 491236
        },
        "total_value": 2374869
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "local": 1941334,
            "foreign": 3718,
            "migrant": 490861
        },
        "total_value": 2435913
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
            "local": 1123880,
            "foreign": 951,
...
```

- Source File: [data.json (5.4 KB)](../../../../data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence-/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "migrated back to the district of birth at the time of the census. Accordingly, if a person's district of birth and"
    ],
    [
        "district of usual residence are the same at the time of the census, he or she is defined as a life-time non-"
    ],
    [
        "migrant."
    ],
    [
        "Net Migration Rate"
    ],
    [
        "The  'Net  Migration  Rate'  is  defined  as  the  number of  net  migrants  per  thousand  of the  usually  resident"
    ],
    [
        "population in a district. A positive net migration rate indicates that in-migration to the district is relatively"
    ],
    [
        "higher, whereas a negative value indicates that out-migration from the district is relatively higher."
    ],
    [
        "Lifetime Migration Effectiveness Ratio (LMER)"
    ],
    [
        "The LMER is a demographic indicator that measures the \u201cefficiency\u201d or net impact of migration flows into"
...
```
- Source File: [raw_data.json (4.2 KB)](../../../../data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence-/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence-/original.png)

- Source File: [original.pdf (64.6 KB)](../../../../data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence-/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=82>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
