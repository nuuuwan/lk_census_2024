# Percentage Distribution of Population by Age Group, 1946–2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 6.1.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=105",
        "source_description": "Table 6.1.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka",
        "what": {
            "PercentagePopulationByCensus": "Percentage Distribution of Population by Age Group, 1946\u20132024"
        },
        "when": [
            "1946",
            "1953",
            "1963",
            "1971",
            "1981",
            "2001",
            "2012",
            "2024"
        ],
        "where_who_types": [
            "age_group"
        ]
    },
    "PercentagePopulationByCensus": {
        "1946": {
            "Sri Lanka": {
                "age_group": "Sri Lanka",
                "pct_values": {
                    "Census1946": 1.0
                }
            },
            "00-04": {
...
```

- Source File: [lanka_data.json (14.0 KB)](../../../../data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "Sri Lanka",
        "values": {
            "p_census_1946": 1.0,
            "p_census_1953": 1.0,
            "p_census_1963": 1.0,
            "p_census_1971": 1.0,
            "p_census_1981": 1.0,
            "p_census_2001": 1.0,
            "p_census_2012": 1.0,
            "p_census_2024": 1.0
        }
    },
    {
        "age_group": "00-04",
        "values": {
            "p_census_1946": 0.129,
            "p_census_1953": 0.149,
            "p_census_1963": 0.152,
            "p_census_1971": 0.131,
            "p_census_1981": 0.125,
            "p_census_2001": 0.085,
            "p_census_2012": 0.086,
            "p_census_2024": 0.056
        }
    },
    {
        "age_group": "05-09",
        "values": {
...
```

- Source File: [data.json (4.0 KB)](../../../../data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing - 2024"
    ],
    [
        "As shown in Table 6.1.4, data from the Censuses of Population and Housing between 1946 and 2024"
    ],
    [
        "reveal significant shifts in age structure of Sri Lanka across five-year age groups. During the 35-year period"
    ],
    [
        "from 1946 to 1981, the elderly population (aged 60 and over) increased by only 1.1 percentage points,"
    ],
    [
        "rising from 5.5 percent to 6.6 percent. However, in the short span of 12 years between 2012 and 2024,"
    ],
    [
        "this figure grew remarkably by 5.6 percentage points, from 12.4 percent to 18.0 percent. According to the"
    ],
    [
        "2024 census data, 18 out of every 100 persons in Sri Lanka are now over the age of 60. Similarly, the"
    ],
    [
        "percentage of the youngest segment, the new addition to the population (ages 0\u20134) has more than halved,"
    ],
    [
        "dropping from 12.9 percent in 1946 to 5.6 percent in 2024."
    ],
    [
        "",
...
```
- Source File: [raw_data.json (2.8 KB)](../../../../data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024/original.png)

- Source File: [original.pdf (71.1 KB)](../../../../data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=105>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
