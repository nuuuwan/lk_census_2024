# Distribution of Persons with a Single Disability and with Multiple Disabilities by Age Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Table 6.2.8, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "AgeGroup:5To9Years": {
                "SingleOrMultipleDisabilities:single_disability": {
                    "Count": "Int:7320"
                },
                "SingleOrMultipleDisabilities:multi_disability": {
                    "Count": "Int:5419"
                },
                "SingleOrMultipleDisabilities:no_disability": {
                    "Count": "Int:1543784"
                }
            },
            "AgeGroup:10To14Years": {
                "SingleOrMultipleDisabilities:single_disability": {
                    "Count": "Int:6995"
                },
                "SingleOrMultipleDisabilities:multi_disability": {
                    "Count": "Int:6400"
                },
                "SingleOrMultipleDisabilities:no_disability": {
                    "Count": "Int:1721801"
                }
            },
            "AgeGroup:15To19Years": {
                "SingleOrMultipleDisabilities:single_disability": {
                    "Count": "Int:7643"
                },
                "SingleOrMultipleDisabilities:multi_disability": {
...
```

- Source File: [lanka_data.json (5.4 KB)](../../../../data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "Sri Lanka",
        "values": {
            "with_single_disability": 452247,
            "with_more_than_one_disability": 275046,
            "no_disability": 19839387
        },
        "total_value": 727293
    },
    {
        "age_group": "05 - 09",
        "values": {
            "with_single_disability": 7320,
            "with_more_than_one_disability": 5419,
            "no_disability": 1543784
        },
        "total_value": 12739
    },
    {
        "age_group": "10 - 14",
        "values": {
            "with_single_disability": 6995,
            "with_more_than_one_disability": 6400,
            "no_disability": 1721801
        },
        "total_value": 13395
    },
    {
        "age_group": "15 - 19",
...
```

- Source File: [data.json (3.3 KB)](../../../../data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "Table 6.2.7 presents the distribution of persons with disabilities by age group. Among the population aged"
    ],
    [
        "80 years and over, one in every three individuals has at least one physical or mental disability"
    ],
    [
        "Table 6.2.8 presents the distribution of persons with a single disability and with multiple disabilities by age"
    ],
    [
        "group.  The  rate  of  persons  with  multiple  disabilities  increases  with age.  According  to the  table,  among"
    ],
    [
        "persons aged 80 years and over, 63,071 individuals were reported to have a single disability, while 79,306"
    ],
    [
        "individuals were reported to have multiple disabilities"
    ],
    [
        "Table 6.2.8 : Distribution of Persons with a Single Disability and with Multiple Disabilities by Age Group, 2024"
    ],
    [
        "",
        "Table 6.2.8 : Distribution of Persons with a Single Disability and with Multiple Disabilities by Age Group, 2024",
        "",
        "",
...
```
- Source File: [raw_data.json (2.8 KB)](../../../../data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group-2024/original.png)

- Source File: [original.pdf (81.0 KB)](../../../../data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=134>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
