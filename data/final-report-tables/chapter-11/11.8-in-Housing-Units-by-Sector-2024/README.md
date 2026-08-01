# in Housing Units by Sector, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 11.8, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Sector:urban": {
                "OneRoomOrMore:with_only_one_room": {
                    "Count": "Int:80249"
                },
                "OneRoomOrMore:more_than_one_room": {
                    "Count": "Int:945081"
                }
            },
            "Sector:estate_urban": {
                "OneRoomOrMore:with_only_one_room": {
                    "Count": "Int:377"
                },
                "OneRoomOrMore:more_than_one_room": {
                    "Count": "Int:2656"
                }
            },
            "Sector:rural": {
                "OneRoomOrMore:with_only_one_room": {
                    "Count": "Int:251344"
                },
                "OneRoomOrMore:more_than_one_room": {
                    "Count": "Int:4521992"
                }
            },
            "Sector:estate_rural": {
                "OneRoomOrMore:with_only_one_room": {
                    "Count": "Int:26388"
...
```

- Source File: [lanka_data.json (893.0 B)](../../../../data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Sri Lanka",
        "values": {
            "with_only_one_room": 358358,
            "with_only_more_than_one_room": 5672183
        },
        "total_value": 6030541
    },
    {
        "sector": "Urban",
        "values": {
            "with_only_one_room": 80249,
            "with_only_more_than_one_room": 945081
        },
        "total_value": 1025330
    },
    {
        "sector": "Estate- Urban",
        "values": {
            "with_only_one_room": 377,
            "with_only_more_than_one_room": 2656
        },
        "total_value": 3033
    },
    {
        "sector": "Rural",
        "values": {
            "with_only_one_room": 251344,
            "with_only_more_than_one_room": 4521992
...
```

- Source File: [data.json (828.0 B)](../../../../data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "Table 11.8 :Rooms in Housing Units by Sector, 2024",
        "",
        "",
        "",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "Rooms in housing units",
        ""
    ],
    [
        "Sector",
        "Total housing \nunits",
        "Percentages",
        "",
        "",
        "Houses with",
        ""
    ],
    [
        "",
...
```
- Source File: [raw_data.json (1.0 KB)](../../../../data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector-2024/original.png)

- Source File: [original.pdf (58.9 KB)](../../../../data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=208>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
