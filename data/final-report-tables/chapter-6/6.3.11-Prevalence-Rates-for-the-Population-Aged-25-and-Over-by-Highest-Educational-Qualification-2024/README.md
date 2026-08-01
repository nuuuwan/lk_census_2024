# Prevalence Rates for the Population Aged 25 and Over by Highest Educational Qualification, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 6.3.11, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "HighestEducationLevel:no_schooling": {
                "NonCommunicableDisease:diabetes": {
                    "Count": "Int:70779"
                },
                "NonCommunicableDisease:high_cholesterol": {
                    "Count": "Int:71178"
                },
                "NonCommunicableDisease:high_blood_pressure": {
                    "Count": "Int:109967"
                },
                "NonCommunicableDisease:heart_disease": {
                    "Count": "Int:24792"
                },
                "NonCommunicableDisease:kidney_disease": {
                    "Count": "Int:9597"
                },
                "NonCommunicableDisease:thalassemia": {
                    "Count": "Int:800"
                },
                "NonCommunicableDisease:cancer": {
                    "Count": "Int:3999"
                },
                "NonCommunicableDisease:stroke_or_paralysis": {
                    "Count": "Int:12396"
                },
                "NonCommunicableDisease:asthma": {
                    "Count": "Int:25992"
...
```

- Source File: [lanka_data.json (6.6 KB)](../../../../data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "education": "Population aged 25 and over*",
        "values": {
            "diabetes": 1844590,
            "high_cholesterol": 1789114,
            "high_blood_pressure": 2191318,
            "heart_disease": 513157,
            "kidney_disease": 166429,
            "thalassemia": 13869,
            "cancer": 83215,
            "stroke": 124822,
            "asthma": 332858,
            "epilepsy": 41607
        },
        "total_value": 13869099
    },
    {
        "education": "Never attended school",
        "values": {
            "diabetes": 70779,
            "high_cholesterol": 71178,
            "high_blood_pressure": 109967,
            "heart_disease": 24792,
            "kidney_disease": 9597,
            "thalassemia": 800,
            "cancer": 3999,
            "stroke": 12396,
            "asthma": 25992,
            "epilepsy": 5998
...
```

- Source File: [data.json (2.9 KB)](../../../../data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Attainment",
        "Population",
        "Diabetes",
        "High Cholesterol",
        "High Blood \nPressure",
        "Heart Disease",
        "Kidney Disease",
        "Thalassemia",
        "Cancer",
        "Stroke",
        "Asthma",
        "Epilepsy"
    ],
    [
        "Population aged 25 and over*",
        "13,869,099",
        "13.3",
        "12.9",
        "15.8",
        "3.7",
        "1.2",
        "0.1",
        "0.6",
        "0.9",
        "2.4",
        "0.3"
    ],
    [
...
```
- Source File: [raw_data.json (1.7 KB)](../../../../data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification-2024/original.png)

- Source File: [original.pdf (61.9 KB)](../../../../data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=147>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
