# Distribution of Households by Main Source of Drinking Water, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 11.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "SourceOfDrinkingWater:protected_well": {
                "Count": "Int:1624506"
            },
            "SourceOfDrinkingWater:semi_protected_well": {
                "Count": "Int:267327"
            },
            "SourceOfDrinkingWater:unprotected_well": {
                "Count": "Int:77806"
            },
            "SourceOfDrinkingWater:tube_well": {
                "Count": "Int:270401"
            },
            "SourceOfDrinkingWater:spring_or_fountain": {
                "Count": "Int:230268"
            },
            "SourceOfDrinkingWater:pipe_borne_water_national_water_supply_and_drainage_board": {
                "Count": "Int:2374349"
            },
            "SourceOfDrinkingWater:pipe_borne_water_local_authority": {
                "Count": "Int:100764"
            },
            "SourceOfDrinkingWater:pipe_borne_water_community_based_organization": {
                "Count": "Int:419247"
            },
            "SourceOfDrinkingWater:pipe_borne_water_private_water_supply_project": {
                "Count": "Int:130394"
            },
...
```

- Source File: [lanka_data.json (1.4 KB)](../../../../data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "source_drinking_water": "Sri Lanka",
        "values": {
            "households": 6111315
        }
    },
    {
        "source_drinking_water": "Protected well",
        "values": {
            "households": 1624506
        }
    },
    {
        "source_drinking_water": "Semi protected well",
        "values": {
            "households": 267327
        }
    },
    {
        "source_drinking_water": "Unprotected well",
        "values": {
            "households": 77806
        }
    },
    {
        "source_drinking_water": "Tube well",
        "values": {
            "households": 270401
        }
...
```

- Source File: [data.json (1.8 KB)](../../../../data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "source of drinking water",
        "Number of \nHouseholds",
        "Percentage"
    ],
    [
        "Sri Lanka",
        "6,111,315",
        "100.0"
    ],
    [
        "Protected well",
        "1,624,506",
        "26.6"
    ],
    [
        "Semi protected well",
        "267,327",
        "4.3"
    ],
    [
        "Unprotected well",
        "77,806",
        "1.3"
    ],
    [
        "Tube well",
        "270,401",
        "4.4"
...
```
- Source File: [raw_data.json (1.1 KB)](../../../../data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water-2024/original.png)

- Source File: [original.pdf (58.9 KB)](../../../../data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water-2024/original.pdf)

(Table 1 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=208>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
