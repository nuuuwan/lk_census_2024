# Language Literacy Rate by Language and District, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 7.10, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=157",
        "source_description": [
            "Table 7.10, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "LanguageLiteracy": "Language Literacy Rate by Language and District, 2024"
        },
        "when": "2024",
        "where_who_types": [
            "district"
        ]
    },
    "LanguageLiteracy": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "LiteracyAtLeastOneLanguage": 2109420,
                    "LiteracySinhala": 2013148,
                    "LiteracyEnglish": 1587413,
                    "LiteracyTamil": 887839
                },
                "total_value": 2139371,
                "total_description": "Population aged 10 and over",
                "pct_values": {
                    "LiteracyAtLeastOneLanguage": 0.986,
...
```

- Source File: [lanka_data.json (15.0 KB)](../../../../data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "p_literacy_at_least_one_language": 0.986,
            "p_literacy_sinhala": 0.941,
            "p_literacy_tamil": 0.415,
            "p_literacy_english": 0.742
        },
        "total_value": 2139371
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "p_literacy_at_least_one_language": 0.989,
            "p_literacy_sinhala": 0.971,
            "p_literacy_tamil": 0.329,
            "p_literacy_english": 0.672
        },
        "total_value": 2169227
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
...
```

- Source File: [data.json (7.4 KB)](../../../../data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Figure 7.3 : Language Literacy Rate by Age Group and Language, 2024"
    ],
    [
        "As illustrated in Figure 7.3, literacy rates in Tamil and English decline steadily with increasing age. Among"
    ],
    [
        "individuals  aged  60  and  above,  Tamil literacy drops  to 30.8%  and  English literacy to 35.0%, reflecting"
    ],
    [
        "more limited educational opportunities and language exposure in the past."
    ],
    [
        "Language Literacy by District Level"
    ],
    [
        "",
        "Population",
        "",
        "Literacy Rate (%)",
        "",
        ""
    ],
    [
        "District",
        "Aged 10 & over",
        "At least one",
        "Sinhala",
        "Tamil",
...
```
- Source File: [raw_data.json (2.9 KB)](../../../../data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024/original.png)

- Source File: [original.pdf (47.1 KB)](../../../../data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=157>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
