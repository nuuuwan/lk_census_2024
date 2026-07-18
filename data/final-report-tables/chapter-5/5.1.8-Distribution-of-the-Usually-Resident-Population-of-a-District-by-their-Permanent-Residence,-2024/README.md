# Distribution of the Usually Resident Population of a District by their Permanent Residence, 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18-green)

*Table 5.1.8, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "District:LK-11": {
                "ResidentRelativeToDistrict:InDistrict": {
                    "Count": "Int:2244323"
                },
                "ResidentRelativeToDistrict:InOtherDistrict": {
                    "Count": "Int:130546"
                }
            },
            "District:LK-12": {
                "ResidentRelativeToDistrict:InDistrict": {
                    "Count": "Int:2340241"
                },
                "ResidentRelativeToDistrict:InOtherDistrict": {
                    "Count": "Int:95672"
                }
            },
            "District:LK-13": {
                "ResidentRelativeToDistrict:InDistrict": {
                    "Count": "Int:1287854"
                },
                "ResidentRelativeToDistrict:InOtherDistrict": {
                    "Count": "Int:17854"
                }
            },
            "District:LK-21": {
                "ResidentRelativeToDistrict:InDistrict": {
                    "Count": "Int:1434821"
...
```

- Source File: [lanka_data.json (5.6 KB)](../../../../data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "in_district": 2244323,
            "in_other_district": 130546
        },
        "total_value": 2374869
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "in_district": 2340241,
            "in_other_district": 95672
        },
        "total_value": 2435913
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
            "in_district": 1287854,
            "in_other_district": 17854
        },
        "total_value": 1305708
...
```

- Source File: [data.json (5.2 KB)](../../../../data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Census of Population and Housing  - 2024"
    ],
    [
        "Permanent Residence"
    ],
    [
        "According to Table 5.1.8, 97.9 percent (454,034) of the total population in Sri Lanka reside in the same"
    ],
    [
        "district as  their permanent  residence. Among  the  usually resident  population,  the  highest  percentage  of"
    ],
    [
        "those holding permanent residence in a different district is reported in the Colombo District (5.5%). This"
    ],
    [
        "figure stands at 3.9 percent in the Gampaha District, while Kilinochchi and Vavuniya districts reported 3.4"
    ],
    [
        "percent and 2.1 percent respectively. In all other districts, this percentage remains below 2 percent."
    ],
    [
        "Usual residence",
        "Population*",
        "permanent residence district",
        "",
        "",
        "residence in another district"
    ],
...
```
- Source File: [raw_data.json (3.3 KB)](../../../../data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024/original.png)

- Source File: [original.pdf (47.4 KB)](../../../../data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=94>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
