# Prevalence Rates of Self-Reported Illnesses by Sector, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 6.3.5, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Sector:urban": {
                "NonCommunicableDisease:diabetes": {
                    "Count": "Int:397050"
                },
                "NonCommunicableDisease:high_cholesterol": {
                    "Count": "Int:339783"
                },
                "NonCommunicableDisease:high_blood_pressure": {
                    "Count": "Int:393232"
                },
                "NonCommunicableDisease:heart_disease": {
                    "Count": "Int:91627"
                },
                "NonCommunicableDisease:kidney_disease": {
                    "Count": "Int:19089"
                },
                "NonCommunicableDisease:thalassemia": {
                    "Count": "Int:3818"
                },
                "NonCommunicableDisease:cancer": {
                    "Count": "Int:11453"
                },
                "NonCommunicableDisease:stroke": {
                    "Count": "Int:15271"
                },
                "NonCommunicableDisease:asthma": {
                    "Count": "Int:53449"
...
```

- Source File: [lanka_data.json (2.8 KB)](../../../../data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "sector": "Urban*",
        "values": {
            "diabetes": 397050,
            "high_cholesterol": 339783,
            "high_blood_pressure": 393232,
            "heart_disease": 91627,
            "kidney_disease": 19089,
            "thalassemia": 3818,
            "cancer": 11453,
            "stroke": 15271,
            "asthma": 53449,
            "epilepsy": 7636
        },
        "total_value": 3817786
    },
    {
        "sector": "Rural",
        "values": {
            "diabetes": 1418971,
            "high_cholesterol": 1418971,
            "high_blood_pressure": 1726700,
            "heart_disease": 427401,
            "kidney_disease": 153864,
            "thalassemia": 17096,
            "cancer": 68384,
            "stroke": 102576,
            "asthma": 324825,
            "epilepsy": 51288
...
```

- Source File: [data.json (1.1 KB)](../../../../data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Sector",
        "Total \nPopulation",
        "Diabetes",
        "High \nCholesterol",
        "High Blood \nPressure",
        "Heart Disease",
        "Kidney \nDisease",
        "Thalassemia",
        "Cancer",
        "Stroke",
        "Asthma",
        "Epilepsy"
    ],
    [
        "Total",
        "21,779,483",
        "8.5",
        "8.2",
        "10.1",
        "2.5",
        "0.8",
        "0.1",
        "0.4",
        "0.6",
        "1.8",
        "0.3"
    ],
    [
...
```
- Source File: [raw_data.json (849.0 B)](../../../../data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector-2024/original.png)

- Source File: [original.pdf (60.9 KB)](../../../../data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector-2024/original.pdf)

(Table 0 on this page.)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=143>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
