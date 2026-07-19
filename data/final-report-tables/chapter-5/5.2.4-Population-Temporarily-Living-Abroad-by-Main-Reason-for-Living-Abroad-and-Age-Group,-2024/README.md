# Population Temporarily Living Abroad by Main Reason for Living Abroad and Age Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 5.2.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "AgeGroup:0To125Years": {
                "EmmigrationReason:Employment": {
                    "Count": "Int:577919"
                },
                "EmmigrationReason:Education": {
                    "Count": "Int:53621"
                },
                "EmmigrationReason:AccompanyingFamilyMemberInNeed": {
                    "Count": "Int:38218"
                },
                "EmmigrationReason:Other": {
                    "Count": "Int:2491"
                }
            },
            "AgeGroup:0To18Years": {
                "EmmigrationReason:Employment": {
                    "Count": "Int:0"
                },
                "EmmigrationReason:Education": {
                    "Count": "Int:1486"
                },
                "EmmigrationReason:AccompanyingFamilyMemberInNeed": {
                    "Count": "Int:17862"
                },
                "EmmigrationReason:Other": {
                    "Count": "Int:35"
                }
...
```

- Source File: [lanka_data.json (1.9 KB)](../../../../data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age": "Total",
        "values": {
            "employment": 577919,
            "education": 53621,
            "accompanying_family_member_in_need": 38218,
            "other": 2491
        },
        "total_value": 672249
    },
    {
        "age": "Less than 18",
        "values": {
            "employment": 0,
            "education": 1486,
            "accompanying_family_member_in_need": 17862,
            "other": 35
        },
        "total_value": 19383
    },
    {
        "age": "18 - 29",
        "values": {
            "employment": 142256,
            "education": 38053,
            "accompanying_family_member_in_need": 6348,
            "other": 716
        },
        "total_value": 187373
...
```

- Source File: [data.json (1014.0 B)](../../../../data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "",
        "Employment",
        "",
        "Education",
        "",
        "family \nmember\u2019s need",
        "",
        "Other",
        ""
    ],
    [
        "",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%"
    ],
    [
        "Total",
        "672,249",
...
```
- Source File: [raw_data.json (1.0 KB)](../../../../data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024/original.png)

- Source File: [original.pdf (45.2 KB)](../../../../data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=98>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
