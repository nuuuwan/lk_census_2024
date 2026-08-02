# Distribution of Persons Aged 5 Years and Over with Disabilities by Highest Educational Qualification andDomain of Disability, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Table 6.2.12, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "HighestEducationLevel:no_schooling": {
                "DisabilityTypes:difficulty_in_seeing": {
                    "Count": "Int:30146"
                },
                "DisabilityTypes:hearing_difficulty": {
                    "Count": "Int:27485"
                },
                "DisabilityTypes:walking_difficulty": {
                    "Count": "Int:61681"
                },
                "DisabilityTypes:cognitive_difficulty": {
                    "Count": "Int:46627"
                },
                "DisabilityTypes:selfcare_difficulty": {
                    "Count": "Int:43022"
                },
                "DisabilityTypes:social_difficulty": {
                    "Count": "Int:39767"
                },
                "DisabilityTypes:no_disability": {
                    "Count": "Int:437737"
                }
            },
            "HighestEducationLevel:passed_grade_1_5": {
                "DisabilityTypes:difficulty_in_seeing": {
                    "Count": "Int:66400"
                },
...
```

- Source File: [lanka_data.json (4.7 KB)](../../../../data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "highest_educational_qualification": "Sri Lanka",
        "values": {
            "difficulty_in_seeing": 192578,
            "difficulty_in_hearing": 130097,
            "difficulty_in_walking_or_climbing_steps": 447969,
            "difficulty_in_remembering_or_concentrating": 167826,
            "difficulty_in_selfcare_such_as_washing_or_dressing": 189292,
            "difficulty_in_communicating_with_others": 112798,
            "no_disability": 19326120
        },
        "total_value": 1240560
    },
    {
        "highest_educational_qualification": "Never attended School",
        "values": {
            "difficulty_in_seeing": 30146,
            "difficulty_in_hearing": 27485,
            "difficulty_in_walking_or_climbing_steps": 61681,
            "difficulty_in_remembering_or_concentrating": 46627,
            "difficulty_in_selfcare_such_as_washing_or_dressing": 43022,
            "difficulty_in_communicating_with_others": 39767,
            "no_disability": 437737
        },
        "total_value": 248728
    },
    {
        "highest_educational_qualification": "Passed Grade 1-5*",
        "values": {
...
```

- Source File: [data.json (3.6 KB)](../../../../data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Number of",
        "",
        "",
        "",
        "",
        "",
        "",
        "Domain of Disability",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        "Highest Education",
        "Persons Aged",
        "Seeing",
        "",
        "Hearing",
        "",
        "steps",
        "Walking or climbing",
        "",
        "Remembering or \nconcentrating",
        "",
        "Selfcare, such as \nwashing  or dressing",
...
```
- Source File: [raw_data.json (2.6 KB)](../../../../data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability-2024/original.png)

- Source File: [original.pdf (70.9 KB)](../../../../data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability-2024/original.pdf)

(Table 1 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=136>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
