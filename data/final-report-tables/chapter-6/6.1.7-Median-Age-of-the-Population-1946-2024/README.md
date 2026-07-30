# Median Age of the Population, 1946-2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 6.1.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Census:1946": {
                "Sex:both_sexes": {
                    "MedianAge": "Float:21.3"
                },
                "Sex:male": {
                    "MedianAge": "Float:22.1"
                },
                "Sex:female": {
                    "MedianAge": "Float:20.5"
                }
            },
            "Census:1953": {
                "Sex:both_sexes": {
                    "MedianAge": "Float:20.8"
                },
                "Sex:male": {
                    "MedianAge": "Float:21.7"
                },
                "Sex:female": {
                    "MedianAge": "Float:19.9"
                }
            },
            "Census:1963": {
                "Sex:both_sexes": {
                    "MedianAge": "Float:19.4"
                },
                "Sex:male": {
...
```

- Source File: [lanka_data.json (1.7 KB)](../../../../data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population-1946-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "census_year": "1946",
        "values": {
            "both_sexes": 21.3,
            "male": 22.1,
            "female": 20.5
        }
    },
    {
        "census_year": "1953",
        "values": {
            "both_sexes": 20.8,
            "male": 21.7,
            "female": 19.9
        }
    },
    {
        "census_year": "1963",
        "values": {
            "both_sexes": 19.4,
            "male": 20.0,
            "female": 18.4
        }
    },
    {
        "census_year": "1971",
        "values": {
            "both_sexes": 19.7,
            "male": 20.0,
...
```

- Source File: [data.json (877.0 B)](../../../../data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population-1946-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing - 2024"
    ],
    [
        "Median Age of the Population"
    ],
    [
        "The median age is the specific age that divides a population into two numerically equal groups. Simply, a"
    ],
    [
        "half of the population (50%) is older than the median age, while the other half is younger. A low median"
    ],
    [
        "age  indicates  a  population  structure  with  a  large  child  population  and  high  birth  rates,  leading  to  an"
    ],
    [
        "increased  demand  for  education,  pediatric  healthcare,  and  youth-oriented  services.  Conversely,  a  high"
    ],
    [
        "median age reflects a trend of population aging and a growing elderly population."
    ],
    [
        "According to Table 6.1.7, the median age of population of Sri Lanka remained at a relatively low level"
    ],
    [
        "between  1946  and  1971,  reaching  a  notable  low  of  19.4  years  in  1963.  By  1981,  the  median  age"
    ],
    [
        "increased to 21.4 years, showing no significant difference between males and females. However, notable"
...
```
- Source File: [raw_data.json (1.8 KB)](../../../../data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population-1946-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population-1946-2024/original.png)

- Source File: [original.pdf (40.8 KB)](../../../../data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population-1946-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=110>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
