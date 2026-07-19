# Population Temporarily Living Abroad by District and Main Reason for Living in Abroad, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 5.2.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:LK-11": {
                "EmmigrationReason:Employment": {
                    "Count": "Int:51449"
                },
                "EmmigrationReason:Education": {
                    "Count": "Int:12339"
                },
                "EmmigrationReason:AccompanyingFamilyMemberInNeed": {
                    "Count": "Int:7230"
                },
                "EmmigrationReason:Other": {
                    "Count": "Int:421"
                }
            },
            "District:LK-12": {
                "EmmigrationReason:Employment": {
                    "Count": "Int:67844"
                },
                "EmmigrationReason:Education": {
                    "Count": "Int:10894"
                },
                "EmmigrationReason:AccompanyingFamilyMemberInNeed": {
                    "Count": "Int:7028"
                },
                "EmmigrationReason:Other": {
                    "Count": "Int:311"
                }
...
```

- Source File: [lanka_data.json (9.3 KB)](../../../../data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "employment": 51449,
            "education": 12339,
            "accompanying_family_member_in_need": 7230,
            "other": 421
        },
        "total_value": 71439
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "employment": 67844,
            "education": 10894,
            "accompanying_family_member_in_need": 7028,
            "other": 311
        },
        "total_value": 86077
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
...
```

- Source File: [data.json (14.8 KB)](../../../../data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "When  compared  by  sex,  it  is  observed  that  in  both  the  urban  and  rural  sectors,  the  number  of  males"
    ],
    [
        "temporarily residing abroad exceeds that of females. However, in the estate rural sector, across all age"
    ],
    [
        "categories,  there  is  a  notably  higher  prevalence  of  females  temporarily  residing  abroad  compared  to"
    ],
    [
        "males."
    ],
    [
        "According to Table 5.2.3, the primary reason for temporary migration is employment. Accordingly, 86.0"
    ],
    [
        "percent (577,919) of the total population who migrated temporarily for employment purposes, while 8.0"
    ],
    [
        "percent (53,621) migrated for education. Additionally, 5.7 percent (38,218) migrated for reasons such as"
    ],
    [
        "a family member's education, employment, or lookafter. A very small percentage, specifically 0.3 percent"
    ],
    [
        "(2,491), migrated temporarily for other reasons."
...
```
- Source File: [raw_data.json (5.0 KB)](../../../../data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024/original.png)

- Source File: [original.pdf (56.5 KB)](../../../../data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=97>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
