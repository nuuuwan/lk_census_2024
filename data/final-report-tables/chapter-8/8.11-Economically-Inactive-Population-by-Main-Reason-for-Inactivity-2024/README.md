# Economically Inactive Population by Main Reason for Inactivity, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 8.11, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "EconomicInactivityReason:household_work": {
                "Count": "Int:3358527"
            },
            "EconomicInactivityReason:education_training": {
                "Count": "Int:2365048"
            },
            "EconomicInactivityReason:unable_or_retired": {
                "Count": "Int:2190230"
            },
            "EconomicInactivityReason:illness_or_disabled": {
                "Count": "Int:517647"
            },
            "EconomicInactivityReason:not_interested": {
                "Count": "Int:447121"
            },
            "EconomicInactivityReason:other": {
                "Count": "Int:173895"
            },
            "EconomicInactivityReason:income_recipient": {
                "Count": "Int:59552"
            }
        }
    }
}
```

- Source File: [lanka_data.json (682.0 B)](../../../../data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "reason_for_being_inactive": "Engaged in Household work/Childcare/Elder Care",
        "values": {
            "population": 3358527
        }
    },
    {
        "reason_for_being_inactive": "Engage in educational/Vocational training",
        "values": {
            "population": 2365048
        }
    },
    {
        "reason_for_being_inactive": "Unable/Too old to work/Retired",
        "values": {
            "population": 2190230
        }
    },
    {
        "reason_for_being_inactive": "Long term illness/Disabled",
        "values": {
            "population": 517647
        }
    },
    {
        "reason_for_being_inactive": "Does not want/interest to do any economic activity",
        "values": {
            "population": 447121
        }
...
```

- Source File: [data.json (928.0 B)](../../../../data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing - 2024"
    ],
    [
        "8.9 Economically Inactive Population"
    ],
    [
        "The economically inactive population, which accounts for 52% of the working-age population, may remain"
    ],
    [
        "inactive for various reasons. During the census, the primary reason for being economically inactive were"
    ],
    [
        "examined.  As  shown  in  Table  8.11,  36.8  percent  of  the  economically  inactive  are  due  to  household"
    ],
    [
        "work/child  or  adult  care.  Further,  26.0  percent  are  inactive  because  they  are  engaged  in  education  or"
    ],
    [
        "vocational training and 24 percent are inactive since they are unable/too old to work/retired."
    ],
    [
        "Reason for being inactive",
        "Number",
        "%"
    ],
    [
        "Total",
        "9,112,020",
...
```
- Source File: [raw_data.json (1.8 KB)](../../../../data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity-2024/original.png)

- Source File: [original.pdf (32.2 KB)](../../../../data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=174>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
