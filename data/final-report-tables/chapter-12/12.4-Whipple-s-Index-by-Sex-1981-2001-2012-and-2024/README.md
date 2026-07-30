# Whipple’s Index by Sex, 1981, 2001, 2012 and 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 12.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Sex:both_sexes": {
            "Time:1981": {
                "WhippleIndex": "Float:118.6"
            },
            "Time:2001": {
                "WhippleIndex": "Float:97.0"
            },
            "Time:2012": {
                "WhippleIndex": "Float:100.2"
            },
            "Time:2024": {
                "WhippleIndex": "Float:99.2"
            }
        },
        "Sex:male": {
            "Time:1981": {
                "WhippleIndex": "Float:116.7"
            },
            "Time:2001": {
                "WhippleIndex": "Float:97.5"
            },
            "Time:2012": {
                "WhippleIndex": "Float:100.3"
            },
            "Time:2024": {
                "WhippleIndex": "Float:99.1"
            }
        },
...
```

- Source File: [lanka_data.json (910.0 B)](../../../../data/final-report-tables/chapter-12/12.4-Whipple-s-Index-by-Sex-1981-2001-2012-and-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sex": "Both sexes",
        "values": {
            "1981": 118.6,
            "2001": 97.0,
            "2012": 100.2,
            "2024": 99.2
        }
    },
    {
        "sex": "Male",
        "values": {
            "1981": 116.7,
            "2001": 97.5,
            "2012": 100.3,
            "2024": 99.1
        }
    },
    {
        "sex": "Female",
        "values": {
            "1981": 120.5,
            "2001": 96.4,
            "2012": 100.0,
            "2024": 99.2
        }
    }
]
```

- Source File: [data.json (403.0 B)](../../../../data/final-report-tables/chapter-12/12.4-Whipple-s-Index-by-Sex-1981-2001-2012-and-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "12.2 Whipple's Index"
    ],
    [
        "Whipple's Index is another numerical indicator that can verify the accuracy of age reporting in"
    ],
    [
        "population data. This represents the impact on the accuracy of 'age' when respondents report an"
    ],
    [
        "age ending in the digits 0 and 5 during the data collection stage. Based on the value obtained by"
    ],
    [
        "the Whipple's Index, it indicates the extent of clustering around ages ending in 0 and 5."
    ],
    [
        "According to the value obtained by the Whipple's Index, the accuracy of the data can be shown"
    ],
    [
        "as follows."
    ],
    [
        "Whipple\u2019s Index Value",
        "Level of Accuracy"
    ],
    [
...
```
- Source File: [raw_data.json (1.4 KB)](../../../../data/final-report-tables/chapter-12/12.4-Whipple-s-Index-by-Sex-1981-2001-2012-and-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-12/12.4-Whipple-s-Index-by-Sex-1981-2001-2012-and-2024/original.png)

- Source File: [original.pdf (106.2 KB)](../../../../data/final-report-tables/chapter-12/12.4-Whipple-s-Index-by-Sex-1981-2001-2012-and-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=221>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
