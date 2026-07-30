# Mean Age at Marriage by Sector, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 9.9, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Sector:urban": {
                "Sex:male": {
                    "MeanAgeAtMarriage": "Float:29.8"
                },
                "Sex:female": {
                    "MeanAgeAtMarriage": "Float:26.6"
                }
            },
            "Sector:rural": {
                "Sex:male": {
                    "MeanAgeAtMarriage": "Float:29.0"
                },
                "Sex:female": {
                    "MeanAgeAtMarriage": "Float:25.4"
                }
            },
            "Sector:estate_rural": {
                "Sex:male": {
                    "MeanAgeAtMarriage": "Float:28.4"
                },
                "Sex:female": {
                    "MeanAgeAtMarriage": "Float:24.5"
                }
            }
        }
    }
}
```

- Source File: [lanka_data.json (616.0 B)](../../../../data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Sri Lanka",
        "values": {
            "male": 29.2,
            "female": 25.6
        }
    },
    {
        "sector": "Urban *",
        "values": {
            "male": 29.8,
            "female": 26.6
        }
    },
    {
        "sector": "Rural",
        "values": {
            "male": 29.0,
            "female": 25.4
        }
    },
    {
        "sector": "Estate Rural **",
        "values": {
            "male": 28.4,
            "female": 24.5
        }
    }
]
```

- Source File: [data.json (398.0 B)](../../../../data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 9.9 : Mean Age at Marriage by Sector, 2024",
        "",
        ""
    ],
    [
        "",
        "",
        "Mean Age at Marriage (Years)",
        ""
    ],
    [
        "Sector",
        "Male",
        "Female",
        "Difference"
    ],
    [
        "Sri Lanka",
        "29.2",
        "25.6",
        "3.6"
    ],
    [
        "Urban *",
        "29.8",
        "26.6",
        "3.2"
...
```
- Source File: [raw_data.json (464.0 B)](../../../../data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector-2024/original.png)

- Source File: [original.pdf (76.7 KB)](../../../../data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector-2024/original.pdf)

(Table 1 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=182>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
