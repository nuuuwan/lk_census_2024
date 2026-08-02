# Distribution of Population by Religion and District, 2012

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Table 6.1.14, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2012": {
            "District:colombo": {
                "Religion:buddhist": {
                    "Count": "Int:1632225"
                },
                "Religion:hindu": {
                    "Count": "Int:186454"
                },
                "Religion:islam": {
                    "Count": "Int:274087"
                },
                "Religion:roman_catholic": {
                    "Count": "Int:162314"
                },
                "Religion:other_christian": {
                    "Count": "Int:66994"
                },
                "Religion:other": {
                    "Count": "Int:2275"
                }
            },
            "District:gampaha": {
                "Religion:buddhist": {
                    "Count": "Int:1642767"
                },
                "Religion:hindu": {
                    "Count": "Int:52973"
                },
...
```

- Source File: [lanka_data.json (11.7 KB)](../../../../data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District-2012/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "buddhist": 1632225,
            "hindu": 186454,
            "islam": 274087,
            "roman_catholic": 162314,
            "other_christian": 66994,
            "other": 2275
        },
        "total_value": 2324349
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "buddhist": 1642767,
            "hindu": 52973,
            "islam": 112746,
            "roman_catholic": 449398,
            "other_christian": 46080,
            "other": 869
        },
        "total_value": 2304833
    },
    {
...
```

- Source File: [data.json (17.0 KB)](../../../../data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District-2012/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "District",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "Total",
        "Buddhist",
        "Hindu",
        "Islam",
        "Roman \nCatholic",
        "Other \nChristian",
        "Other"
    ],
    [
        "Sri Lanka",
        "20,359,439",
        "14,272,056",
        "2,561,299",
        "1,967,523",
        "1,261,194",
        "290,967",
        "6,400"
...
```
- Source File: [raw_data.json (5.1 KB)](../../../../data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District-2012/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District-2012/original.png)

- Source File: [original.pdf (46.9 KB)](../../../../data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District-2012/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=123>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
