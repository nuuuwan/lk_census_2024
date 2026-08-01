# Percentage Pistribution of Population Aged 03 Years and Over by Educational Activity and Age Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 7.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "AgeGroup:3To4Years": {
                "EducationActivity:preschool_education": {
                    "Count": "Int:239687"
                },
                "EducationActivity:school_education": {
                    "Count": "Int:0"
                },
                "EducationActivity:degree_or_postgrad": {
                    "Count": "Int:0"
                },
                "EducationActivity:vocational_training": {
                    "Count": "Int:0"
                },
                "EducationActivity:other_education": {
                    "Count": "Int:568"
                },
                "EducationActivity:not_studying": {
                    "Count": "Int:327724"
                }
            },
            "AgeGroup:5To14Years": {
                "EducationActivity:preschool_education": {
                    "Count": "Int:243587"
                },
                "EducationActivity:school_education": {
                    "Count": "Int:2909880"
                },
...
```

- Source File: [lanka_data.json (2.9 KB)](../../../../data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "age_group": "3 - 4",
        "values": {
            "pre_school": 239687,
            "school_education": 0,
            "undergraduate_or_postgraduate_education": 0,
            "vocational_training_or_technical_education": 0,
            "other_educational_activity": 568,
            "not_studying": 327724
        },
        "total_value": 567979
    },
    {
        "age_group": "5 -14",
        "values": {
            "pre_school": 243587,
            "school_education": 2909880,
            "undergraduate_or_postgraduate_education": 0,
            "vocational_training_or_technical_education": 0,
            "other_educational_activity": 23042,
            "not_studying": 115210
        },
        "total_value": 3291719
    },
    {
        "age_group": "15 -18",
        "values": {
            "pre_school": 0,
            "school_education": 1148649,
...
```

- Source File: [data.json (1.6 KB)](../../../../data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "",
        "",
        "Census of Population and Housing  - 2024",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Disaggregated  by  sex,  the  percentage  of females  engaged  in  degree/postgraduate  education  is  higher",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "than the corresponding percentage of males.",
        "",
        "",
        "",
        "",
        "",
...
```
- Source File: [raw_data.json (1.8 KB)](../../../../data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group-2024/original.png)

- Source File: [original.pdf (87.6 KB)](../../../../data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=150>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
