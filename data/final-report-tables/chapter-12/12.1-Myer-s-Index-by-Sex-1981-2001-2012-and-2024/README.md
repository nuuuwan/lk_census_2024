# Myer’s Index by Sex, 1981, 2001, 2012 and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 12.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Sex:both_sexes": {
            "Time:1981": {
                "MyersIndex": "Float:9.7"
            },
            "Time:2001": {
                "MyersIndex": "Float:2.7"
            },
            "Time:2012": {
                "MyersIndex": "Float:1.7"
            },
            "Time:2024": {
                "MyersIndex": "Float:1.2"
            }
        },
        "Sex:male": {
            "Time:1981": {
                "MyersIndex": "Float:8.7"
            },
            "Time:2001": {
                "MyersIndex": "Float:2.7"
            },
            "Time:2012": {
                "MyersIndex": "Float:1.8"
            },
            "Time:2024": {
                "MyersIndex": "Float:1.2"
            }
        },
...
```

- Source File: [lanka_data.json (869.0 B)](../../../../data/final-report-tables/chapter-12/12.1-Myer-s-Index-by-Sex-1981-2001-2012-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sex": "Both sexes",
        "values": {
            "1981": 9.7,
            "2001": 2.7,
            "2012": 1.7,
            "2024": 1.2
        }
    },
    {
        "sex": "Male",
        "values": {
            "1981": 8.7,
            "2001": 2.7,
            "2012": 1.8,
            "2024": 1.2
        }
    },
    {
        "sex": "Female",
        "values": {
            "1981": 11.2,
            "2001": 3.0,
            "2012": 1.7,
            "2024": 1.1
        }
    }
]
```

- Source File: [data.json (386.0 B)](../../../../data/final-report-tables/chapter-12/12.1-Myer-s-Index-by-Sex-1981-2001-2012-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 12.1 : Myer\u2019s Index by Sex, 1981, 2001, 2012 and 2024",
        "",
        "",
        ""
    ],
    [
        "Sex",
        "",
        "Myers\u2019 Index",
        "",
        ""
    ],
    [
        "",
        "1981",
        "2001*",
        "2012",
        "2024"
    ],
    [
        "Both sexes",
        "9.7",
        "2.7",
        "1.7",
        "1.2"
    ],
    [
...
```
- Source File: [raw_data.json (442.0 B)](../../../../data/final-report-tables/chapter-12/12.1-Myer-s-Index-by-Sex-1981-2001-2012-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-12/12.1-Myer-s-Index-by-Sex-1981-2001-2012-and-2024/original.png)

- Source File: [original.pdf (75.7 KB)](../../../../data/final-report-tables/chapter-12/12.1-Myer-s-Index-by-Sex-1981-2001-2012-and-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=218>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
