# Employed Population, by Highest Educational Attainment and Sex, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 8.7, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "HighestEducationLevel2:NeverAttendedSchool": {
                "Sex:Male": {
                    "EmployedCount": "Int:67915"
                },
                "Sex:Female": {
                    "EmployedCount": "Int:49378"
                }
            },
            "HighestEducationLevel2:StudiedInASpecialSchoolOrSpecialUnit": {
                "Sex:Male": {
                    "EmployedCount": "Int:3923"
                },
                "Sex:Female": {
                    "EmployedCount": "Int:2719"
                }
            },
            "HighestEducationLevel2:PassedGrade15": {
                "Sex:Male": {
                    "EmployedCount": "Int:493163"
                },
                "Sex:Female": {
                    "EmployedCount": "Int:183967"
                }
            },
            "HighestEducationLevel2:PassedGrade68": {
                "Sex:Male": {
                    "EmployedCount": "Int:618673"
...
```

- Source File: [lanka_data.json (1.7 KB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "educational_level": "Never attended School",
        "values": {
            "male": 67915,
            "female": 49378
        },
        "total_value": 117293
    },
    {
        "educational_level": "Studied in a special school / special unit",
        "values": {
            "male": 3923,
            "female": 2719
        },
        "total_value": 6642
    },
    {
        "educational_level": "Passed Grade 1 - 5",
        "values": {
            "male": 493163,
            "female": 183967
        },
        "total_value": 677130
    },
    {
        "educational_level": "Passed Grade 6 - 8",
        "values": {
            "male": 618673,
            "female": 171412
...
```

- Source File: [data.json (1.2 KB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Table 8.7 : Employed Population, by Highest Educational Attainment and Sex, 2024",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Education level",
        "Total",
        "",
        "Male",
        "",
        "Female",
        ""
    ],
    [
        "",
        "Number",
        "%",
        "Number",
        "%",
        "Number",
        "%"
    ],
    [
        "Total",
...
```
- Source File: [raw_data.json (2.2 KB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/original.png)

- Source File: [original.pdf (60.8 KB)](../../../../data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=169>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
