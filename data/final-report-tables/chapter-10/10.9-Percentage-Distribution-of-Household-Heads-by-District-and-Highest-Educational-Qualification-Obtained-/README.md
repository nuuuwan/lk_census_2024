# Percentage Distribution of Household Heads by District and Highest Educational Qualification Obtained,

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 10.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "District:colombo": {
                "HighestEducationLevel3:no_schooling": {
                    "Count": "Int:9113"
                },
                "HighestEducationLevel3:passed_1_5_years": {
                    "Count": "Int:41277"
                },
                "HighestEducationLevel3:passed_6_10_years": {
                    "Count": "Int:189119"
                },
                "HighestEducationLevel3:gce_ol": {
                    "Count": "Int:178500"
                },
                "HighestEducationLevel3:gce_al": {
                    "Count": "Int:243813"
                }
            },
            "District:gampaha": {
                "HighestEducationLevel3:no_schooling": {
                    "Count": "Int:6336"
                },
                "HighestEducationLevel3:passed_1_5_years": {
                    "Count": "Int:45940"
                },
                "HighestEducationLevel3:passed_6_10_years": {
                    "Count": "Int:254321"
                },
...
```

- Source File: [lanka_data.json (12.0 KB)](../../../../data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained-/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "no_schooling": 9113,
            "passed_1_5_years": 41277,
            "passed_6_10_years": 189119,
            "gce_ol": 178500,
            "gce_al": 243813
        },
        "total_value": 661822
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "no_schooling": 6336,
            "passed_1_5_years": 45940,
            "passed_6_10_years": 254321,
            "gce_ol": 194820,
            "gce_al": 187218
        },
        "total_value": 688635
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
...
```

- Source File: [data.json (16.1 KB)](../../../../data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained-/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Total",
        "",
        "",
        "",
        "",
        "",
        "Highest Educational Qualification Obtained",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "District",
        "Number of \nHousehold",
        "%",
        "Never",
        "",
        "Passed",
        "",
        "Passed",
        "",
        "G.C.E.",
        "",
        "G.C.E.",
        ""
...
```
- Source File: [raw_data.json (5.1 KB)](../../../../data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained-/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained-/original.png)

- Source File: [original.pdf (67.9 KB)](../../../../data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained-/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=199>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
