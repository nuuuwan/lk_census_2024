# Mean Age at Marriage, 1953–2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Table 9.8, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:1953": {
            "Sex:male": {
                "MedianAge": "Float:27.2"
            },
            "Sex:female": {
                "MedianAge": "Float:20.9"
            }
        },
        "Time:1963": {
            "Sex:male": {
                "MedianAge": "Float:27.9"
            },
            "Sex:female": {
                "MedianAge": "Float:22.1"
            }
        },
        "Time:1971": {
            "Sex:male": {
                "MedianAge": "Float:28.0"
            },
            "Sex:female": {
                "MedianAge": "Float:23.5"
            }
        },
        "Time:1981": {
            "Sex:male": {
                "MedianAge": "Float:27.9"
            },
...
```

- Source File: [lanka_data.json (938.0 B)](../../../../data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage-1953-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "census_year": "1953",
        "values": {
            "male": 27.2,
            "female": 20.9
        }
    },
    {
        "census_year": "1963",
        "values": {
            "male": 27.9,
            "female": 22.1
        }
    },
    {
        "census_year": "1971",
        "values": {
            "male": 28.0,
            "female": 23.5
        }
    },
    {
        "census_year": "1981",
        "values": {
            "male": 27.9,
            "female": 24.4
        }
    },
    {
...
```

- Source File: [data.json (596.0 B)](../../../../data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage-1953-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 9.8 : Mean Age at Marriage, 1953\u20132024",
        "",
        ""
    ],
    [
        "Census Year",
        "",
        "Mean Age at Marriage (Years)",
        ""
    ],
    [
        "",
        "Male",
        "Female",
        "Difference"
    ],
    [
        "1953",
        "27.2",
        "20.9",
        "6.3"
    ],
    [
        "1963",
        "27.9",
        "22.1",
        "5.8"
...
```
- Source File: [raw_data.json (556.0 B)](../../../../data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage-1953-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage-1953-2024/original.png)

- Source File: [original.pdf (76.7 KB)](../../../../data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage-1953-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=182>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
