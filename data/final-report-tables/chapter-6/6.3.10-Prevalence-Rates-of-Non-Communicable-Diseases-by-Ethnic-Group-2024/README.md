# Prevalence Rates of Non-Communicable Diseases by Ethnic Group, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*Table 6.3.10, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Ethnicity:sinhala": {
                "NonCommunicableDisease:diabetes": {
                    "Count": "Int:1388253"
                },
                "NonCommunicableDisease:high_cholesterol": {
                    "Count": "Int:1404396"
                },
                "NonCommunicableDisease:high_blood_pressure": {
                    "Count": "Int:1694960"
                },
                "NonCommunicableDisease:heart_disease": {
                    "Count": "Int:419704"
                },
                "NonCommunicableDisease:kidney_disease": {
                    "Count": "Int:129140"
                },
                "NonCommunicableDisease:thalassemia": {
                    "Count": "Int:16142"
                },
                "NonCommunicableDisease:cancer": {
                    "Count": "Int:64570"
                },
                "NonCommunicableDisease:stroke_or_paralysis": {
                    "Count": "Int:96855"
                },
                "NonCommunicableDisease:asthma": {
                    "Count": "Int:274422"
...
```

- Source File: [lanka_data.json (8.2 KB)](../../../../data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "ethnicity": "Sri Lanka*",
        "values": {
            "diabetes": 1851256,
            "high_cholesterol": 1785918,
            "high_blood_pressure": 2199728,
            "heart_disease": 544487,
            "kidney_disease": 174236,
            "thalassemia": 21779,
            "cancer": 87118,
            "stroke": 130677,
            "asthma": 392031,
            "epilepsy": 65338
        },
        "total_value": 21779483
    },
    {
        "ethnicity": "Sinhala",
        "values": {
            "diabetes": 1388253,
            "high_cholesterol": 1404396,
            "high_blood_pressure": 1694960,
            "heart_disease": 419704,
            "kidney_disease": 129140,
            "thalassemia": 16142,
            "cancer": 64570,
            "stroke": 96855,
            "asthma": 274422,
            "epilepsy": 48427
...
```

- Source File: [data.json (3.4 KB)](../../../../data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Ethnic group",
        "Total Population",
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
        "Sri Lanka*",
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
- Source File: [raw_data.json (1.9 KB)](../../../../data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group-2024/original.png)

- Source File: [original.pdf (42.4 KB)](../../../../data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=146>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
