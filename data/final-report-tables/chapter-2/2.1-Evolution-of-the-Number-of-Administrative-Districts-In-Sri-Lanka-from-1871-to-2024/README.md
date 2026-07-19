# Evolution of the Number of Administrative Districts In Sri Lanka from 1871 to 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19-green)

*Table 2.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "District": {
        "District:LK-11": {
            "Time:1871": {
                "IsExisting": "Bool:True"
            },
            "Time:1881": {
                "IsExisting": "Bool:True"
            },
            "Time:1891": {
                "IsExisting": "Bool:True"
            },
            "Time:1901": {
                "IsExisting": "Bool:True"
            },
            "Time:1911": {
                "IsExisting": "Bool:True"
            },
            "Time:1921": {
                "IsExisting": "Bool:True"
            },
            "Time:1931": {
                "IsExisting": "Bool:True"
            },
            "Time:1946": {
                "IsExisting": "Bool:True"
            },
            "Time:1953": {
                "IsExisting": "Bool:True"
            },
...
```

- Source File: [lanka_data.json (26.2 KB)](../../../../data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "is_in_1871": true,
            "is_in_1881": true,
            "is_in_1891": true,
            "is_in_1901": true,
            "is_in_1911": true,
            "is_in_1921": true,
            "is_in_1931": true,
            "is_in_1946": true,
            "is_in_1953": true,
            "is_in_1963": true,
            "is_in_1971": true,
            "is_in_1981": true,
            "is_in_2001": true,
            "is_in_2012": true,
            "is_in_2024": true
        }
    },
    {
        "region_id": "LK-12-Negombo",
        "region_name": "Negombo",
        "region_ent_type": "district",
        "values": {
            "is_in_1871": false,
            "is_in_1881": true,
...
```

- Source File: [data.json (13.6 KB)](../../../../data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing - 2024"
    ],
    [
        "2.2.2 Division by district"
    ],
    [
        "The 5 provinces established in 1833 by the Colebrooke Reform consisted of 23 districts. The boundaries"
    ],
    [
        "of these districts have been subject to changes from time to time and due to these changes, the number of"
    ],
    [
        "districts has changed in subsequent censuses. This is shown in the table 2.1 below."
    ],
    [
        "Although the division of administrative districts changed from 1871 to 1981, in 2001 the country's territory"
    ],
    [
        "was divided into 25 administrative districts, which remains the same today."
    ],
    [
        "District",
        "1871",
        "1881",
        "1891",
        "1901",
        "1911",
        "1921",
...
```
- Source File: [raw_data.json (6.7 KB)](../../../../data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024/original.png)

- Source File: [original.pdf (107.0 KB)](../../../../data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=60>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
