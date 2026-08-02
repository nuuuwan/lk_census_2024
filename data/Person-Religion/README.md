# Person-Religion

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*Person-Religion, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:2024": {
            "Country:sri_lanka": {
                "Religion:buddhist": {
                    "Count": "Int:15196960"
                },
                "Religion:hindu": {
                    "Count": "Int:2718154"
                },
                "Religion:islam": {
                    "Count": "Int:2327605"
                },
                "Religion:roman_catholic": {
                    "Count": "Int:1209072"
                },
                "Religion:other_christian": {
                    "Count": "Int:266515"
                },
                "Religion:other": {
                    "Count": "Int:63494"
                }
            },
            "Province:western": {
                "Religion:buddhist": {
                    "Count": "Int:4507601"
                },
                "Religion:hindu": {
                    "Count": "Int:305971"
                },
...
```

- Source File: [lanka_data.json (254.5 KB)](../../data/Person-Religion/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "buddhist": 15196960,
            "hindu": 2718154,
            "islam": 2327605,
            "roman_catholic": 1209072,
            "other_christian": 266515,
            "other": 63494
        },
        "total_value": 21781800
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "buddhist": 4507601,
            "hindu": 305971,
            "islam": 568301,
            "roman_catholic": 616413,
            "other_christian": 104869,
            "other": 14186
        },
        "total_value": 6117341
    },
    {
...
```

- Source File: [data/Person-Religion/data.json (4.5 MB)](../../data/Person-Religion/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | buddhist | hindu | islam | roman_catholic | other_christian | other |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 21781800 | 15196960 | 2718154 | 2327605 | 1209072 | 266515 | 63494 |
| LK-1 | Western | province | 6117341 | 4507601 | 305971 | 568301 | 616413 | 104869 | 14186 |
| LK-2 | Central | province | 2714045 | 1760853 | 565722 | 296754 | 55680 | 26421 | 8615 |
| LK-3 | Southern | province | 2606679 | 2463066 | 28775 | 92985 | 5093 | 7568 | 9192 |
| LK-6 | North Western | province | 2586972 | 1918652 | 43060 | 318870 | 278850 | 17211 | 10329 |
| LK-12 | Gampaha | district | 2436142 | 1744475 | 67337 | 132985 | 441173 | 43053 | 7119 |
| EC-02 | Gampaha | ed | 2436142 | 1744475 | 67337 | 132985 | 441173 | 43053 | 7119 |
| LK-11 | Colombo | district | 2375415 | 1682524 | 197524 | 297852 | 139690 | 55217 | 2608 |
| EC-01 | Colombo | ed | 2375415 | 1682524 | 197524 | 297852 | 139690 | 55217 | 2608 |
| LK-9 | Sabaragamuwa | province | 2015899 | 1728595 | 158799 | 98549 | 14257 | 10416 | 5283 |
| LK-5 | Eastern | province | 1783214 | 388164 | 596842 | 706572 | 46596 | 41109 | 3931 |
| LK-61 | Kurunegala | district | 1768156 | 1557548 | 15155 | 142329 | 38045 | 7359 | 7720 |
| EC-15 | Kurunegala | ed | 1768156 | 1557548 | 15155 | 142329 | 38045 | 7359 | 7720 |
| LK-21 | Kandy | district | 1461895 | 1063437 | 143193 | 223243 | 17093 | 9656 | 5273 |
| EC-04 | Kandy | ed | 1461895 | 1063437 | 143193 | 223243 | 17093 | 9656 | 5273 |
| LK-7 | North Central | province | 1407610 | 1262247 | 9588 | 120511 | 6869 | 3663 | 4732 |
| LK-8 | Uva | province | 1399892 | 1135408 | 180305 | 65203 | 9852 | 5431 | 3693 |
| LK-13 | Kalutara | district | 1305784 | 1080602 | 41110 | 137464 | 35550 | 6599 | 4459 |
| EC-03 | Kalutara | ed | 1305784 | 1080602 | 41110 | 137464 | 35550 | 6599 | 4459 |
| LK-4 | Northern | province | 1150148 | 32374 | 829092 | 59860 | 175462 | 49827 | 3533 |

- Source File: [data/Person-Religion/data.tsv (736.0 KB)](../../data/Person-Religion/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Religion>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
