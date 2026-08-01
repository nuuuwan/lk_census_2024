# Percentage of Housing Units Owned by Household Members and Sector, 2012 and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 11.5, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Sector:urban": {
            "Time:2012": {
                "OwnedByMembersPercent": "Percent:0.75"
            },
            "Time:2024": {
                "OwnedByMembersPercent": "Percent:0.769"
            }
        },
        "Sector:rural": {
            "Time:2012": {
                "OwnedByMembersPercent": "Percent:0.88"
            },
            "Time:2024": {
                "OwnedByMembersPercent": "Percent:0.89"
            }
        },
        "Sector:estate_rural": {
            "Time:2012": {
                "OwnedByMembersPercent": "Percent:0.222"
            },
            "Time:2024": {
                "OwnedByMembersPercent": "Percent:0.295"
            }
        }
    }
}
```

- Source File: [lanka_data.json (581.0 B)](../../../../data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector-2012-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Sri Lanka",
        "values": {
            "p_households_owned_by_members_2012": 0.829,
            "p_households_owned_by_members_2024": 0.846
        }
    },
    {
        "sector": "Urban*",
        "values": {
            "p_households_owned_by_members_2012": 0.75,
            "p_households_owned_by_members_2024": 0.769
        }
    },
    {
        "sector": "Rural",
        "values": {
            "p_households_owned_by_members_2012": 0.88,
            "p_households_owned_by_members_2024": 0.89
        }
    },
    {
        "sector": "Estate- Rural**",
        "values": {
            "p_households_owned_by_members_2012": 0.222,
            "p_households_owned_by_members_2024": 0.295
        }
    }
]
```

- Source File: [data.json (634.0 B)](../../../../data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector-2012-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "Percentage of housing units owned by"
    ],
    [
        "Sector",
        "",
        "household members"
    ],
    [
        "",
        "2012",
        "2024"
    ],
    [
        "Sri Lanka",
        "82.9",
        "84.6"
    ],
    [
        "Urban*",
        "75.0",
        "76.9"
    ],
    [
        "Rural",
        "88.0",
        "89.0"
...
```
- Source File: [raw_data.json (360.0 B)](../../../../data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector-2012-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector-2012-and-2024/original.png)

- Source File: [original.pdf (51.6 KB)](../../../../data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector-2012-and-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=205>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
