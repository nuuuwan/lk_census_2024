# Population Aged 3 Years and Over by Sex and Educational Activity During the Census Reference Period,

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 7.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=149",
        "source_description": [
            "Table 7.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "EducationBySex": "Population Aged 3 Years and Over by Sex and Educational Activity During the Census Reference Period,"
        },
        "when": "2024",
        "where_who_types": [
            "educational_activity"
        ]
    },
    "EducationBySex": {
        "2024": {
            "Preschool education": {
                "educational_activity": "Preschool education",
                "values": {
                    "Male": 243648,
                    "Female": 238458
                },
                "total_value": 482106,
                "pct_values": {
                    "Male": 0.5054,
                    "Female": 0.4946
                }
            },
            "School education": {
                "educational_activity": "School education",
...
```

- Source File: [lanka_data.json (2.3 KB)](../../../../data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "educational_activity": "Preschool education",
        "values": {
            "male": 243648,
            "female": 238458
        },
        "total_value": 482106
    },
    {
        "educational_activity": "School education",
        "values": {
            "male": 2157831,
            "female": 2193394
        },
        "total_value": 4351225
    },
    {
        "educational_activity": "Degree/Postgraduate education",
        "values": {
            "male": 120745,
            "female": 200244
        },
        "total_value": 320989
    },
    {
        "educational_activity": "Vocational training/Technical education",
        "values": {
            "male": 70149,
            "female": 52308
...
```

- Source File: [data.json (958.0 B)](../../../../data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "7. Education and Literacy"
    ],
    [
        "The  data  on  education  and  literacy  collected  during  a  population  census  is  vital  for  a country's  human"
    ],
    [
        "resource development and the formulation of future policies. In the Census of Population and Housing -"
    ],
    [
        "2024, information was collected for all persons aged three years and over on the educational activities in"
    ],
    [
        "which they were engaged during the census reference period (defined as the 30 days preceding the date"
    ],
    [
        "of enumeration) as well as on the highest level of educational attainment obtained at the time of the census."
    ],
    [
        "Based on these data, the government and relevant authorities are empowered to facilitate evidence-based"
    ],
    [
        "decision-making  in  education,  including  the  allocation  of  resources  and  the  mitigation  of  educational"
    ],
    [
        "disparities, as well as the formulation of new educational policies. Furthermore, information was collected"
    ],
    [
        "on  literacy  in  the  main  languages  used  in  Sri  Lanka  \u201cSinhala,\u201d  \u201cTamil,\u201d  and  \u201cEnglish\u201d  as  well  as  on"
...
```
- Source File: [raw_data.json (2.3 KB)](../../../../data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,/original.png)

- Source File: [original.pdf (63.3 KB)](../../../../data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=149>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
