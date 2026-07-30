# Percentage Distribution of Households by Type of Toilet Facilities, 2012 and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 11.15, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2012": {
            "ToiletFacilities:within_the_housing_unit_exclusively_for_the_household": {
                "Count": "Int:1748249"
            },
            "ToiletFacilities:within_the_housing_unit_sharing_with_another_household": {
                "Count": "Int:82078"
            },
            "ToiletFacilities:within_premises_exclusively_for_the_household": {
                "Count": "Int:2817362"
            },
            "ToiletFacilities:within_premises_sharing_with_another_household": {
                "Count": "Int:358453"
            },
            "ToiletFacilities:no_toilet_but_sharing_with_another_housing_unit_or_units": {
                "Count": "Int:133772"
            },
            "ToiletFacilities:common_or_public_toilet": {
                "Count": "Int:36088"
            },
            "ToiletFacilities:not_using_a_toilet_use_jungle_beach_and_open_ground": {
                "Count": "Int:88280"
            }
        },
        "Time:2024": {
            "ToiletFacilities:within_the_housing_unit_exclusively_for_the_household": {
                "Count": "Int:3798777"
            },
            "ToiletFacilities:within_the_housing_unit_sharing_with_another_household": {
...
```

- Source File: [lanka_data.json (1.6 KB)](../../../../data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities-2012-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "toilet_facilities": "Toilet facilities",
        "values": {
            "units_2012": 2012,
            "units_2024": 2024
        }
    },
    {
        "toilet_facilities": "Within the housing unit - Exclusively for the household",
        "values": {
            "units_2012": 1748249,
            "units_2024": 3798777
        }
    },
    {
        "toilet_facilities": "Within the housing unit - Sharing with another household",
        "values": {
            "units_2012": 82078,
            "units_2024": 157456
        }
    },
    {
        "toilet_facilities": "Within Premises - Exclusively for the household",
        "values": {
            "units_2012": 2817362,
            "units_2024": 1832587
        }
    },
    {
...
```

- Source File: [data.json (1.2 KB)](../../../../data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities-2012-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Toilet facilities",
        "2012",
        "",
        "2024",
        ""
    ],
    [
        "",
        "Number",
        "%",
        "Number",
        "%"
    ],
    [
        "Total",
        "5,264,282",
        "100.0",
        "6,111,315",
        "100.0"
    ],
    [
        "Within the housing unit - Exclusively for the household",
        "1,748,249",
        "33.2",
        "3,798,777",
        "62.2"
    ],
    [
...
```
- Source File: [raw_data.json (1.1 KB)](../../../../data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities-2012-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities-2012-and-2024/original.png)

- Source File: [original.pdf (95.3 KB)](../../../../data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities-2012-and-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=213>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
