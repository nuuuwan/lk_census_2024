# Distribution of Persons Aged 5 Years and Over with Disabilities by Marital Status and Domain of Disability,2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 6.2.11, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "MaritalStatus:never_married": {
                "DisabilityTypes:difficulty_in_seeing": {
                    "Count": "Int:26799"
                },
                "DisabilityTypes:difficulty_in_hearing": {
                    "Count": "Int:24124"
                },
                "DisabilityTypes:difficulty_in_walking_or_climbing_steps": {
                    "Count": "Int:55653"
                },
                "DisabilityTypes:difficulty_in_remembering_or_concentrating": {
                    "Count": "Int:63731"
                },
                "DisabilityTypes:difficulty_in_selfcare_such_as_washing_or_dressing": {
                    "Count": "Int:47650"
                },
                "DisabilityTypes:difficulty_in_communicating_with_others": {
                    "Count": "Int:53285"
                },
                "DisabilityTypes:no_disability": {
                    "Count": "Int:7613788"
                }
            },
            "MaritalStatus:married": {
                "DisabilityTypes:difficulty_in_seeing": {
                    "Count": "Int:108272"
                },
...
```

- Source File: [lanka_data.json (4.6 KB)](../../../../data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "marital_status": "Sri Lanka",
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
        "marital_status": "Never Married",
        "values": {
            "difficulty_in_seeing": 26799,
            "difficulty_in_hearing": 24124,
            "difficulty_in_walking_or_climbing_steps": 55653,
            "difficulty_in_remembering_or_concentrating": 63731,
            "difficulty_in_selfcare_such_as_washing_or_dressing": 47650,
            "difficulty_in_communicating_with_others": 53285,
            "no_disability": 7613788
        },
        "total_value": 271242
    },
    {
        "marital_status": "Married",
        "values": {
...
```

- Source File: [data.json (3.0 KB)](../../../../data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "",
        "Years and Over",
        "",
        "",
        "",
        "",
        "steps",
        "",
        "concentrating",
        "",
        "washing  or dressing",
        "",
        "others",
        ""
    ],
    [
        "",
        "",
        "Number",
        "Rate  \n(per 1,000",
        "Number",
        "Rate  \n(per 1,000",
        "Number",
        "Rate  \n(per 1,000",
        "Number",
        "Rate  \n(per 1,000",
        "Number",
        "Rate  \n(per 1,000",
...
```
- Source File: [raw_data.json (1.8 KB)](../../../../data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability-2024/original.png)

- Source File: [original.pdf (70.9 KB)](../../../../data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=136>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
