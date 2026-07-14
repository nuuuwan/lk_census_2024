# Population Distribution by District and Sector, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Table 3.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=72",
        "source_description": [
            "Table 3.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "Sector": "Population Distribution by District and Sector, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "province",
            "district",
            "country",
            "ed"
        ]
    },
    "Sector": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "PopulationUrban": 1773222,
                    "PopulationRural": 593669,
                    "PopulationEstateRural": 4650,
                    "PopulationEstateUrban": 3874
                },
                "total_value": 2375415,
...
```

- Source File: [lanka_data.json (30.8 kB)](../../../../data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "population_urban": 1773222,
            "population_estate_urban": 3874,
            "population_rural": 593669,
            "population_estate_rural": 4650
        },
        "total_value": 2375415
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "population_urban": 350441,
            "population_estate_urban": 0,
            "population_rural": 2085307,
            "population_estate_rural": 394
        },
        "total_value": 2436142
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
...
```

- Source File: [data.json (16.5 kB)](../../../../data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "In the Census of Population and Housing -2012, the areas referred to as the Estate Sector correspond to"
    ],
    [
        "what is identified as the Estate Rural sector in 2024. In 2012, the Estate Rural Sector population accounted"
    ],
    [
        "for 4.4 percent of the total population, while in the 2024 Census this percentage has declined to 4 percent."
    ],
    [
        "Furthermore, most of the population in Sri Lanka resides in the Rural sector, accounting for 78.5 percent"
    ],
    [
        "of the total population. This represents an increase of 1.1 percentage points compared to the population"
    ],
    [
        "District",
        "",
        "Urban",
        "",
        "Estate Urban",
        "",
        "Rural",
        "",
        "",
        "Estate Rural"
...
```
- Source File: [raw_data.json (4.6 kB)](../../../../data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024/original.png)

- Source File: [original.pdf (62.9 kB)](../../../../data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=72>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
