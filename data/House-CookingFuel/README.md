# House-CookingFuel

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01-green)

*House-CookingFuel, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "Country:sri_lanka": {
                "CookingFuel:fire_wood": {
                    "Count": "Int:3381781"
                },
                "CookingFuel:kerosene": {
                    "Count": "Int:32974"
                },
                "CookingFuel:gas": {
                    "Count": "Int:2588502"
                },
                "CookingFuel:electricity": {
                    "Count": "Int:19540"
                },
                "CookingFuel:sawdust_paddy_husk": {
                    "Count": "Int:1739"
                },
                "CookingFuel:bio_gas": {
                    "Count": "Int:7179"
                },
                "CookingFuel:other": {
                    "Count": "Int:2361"
                },
                "CookingFuel:not_relevant": {
                    "Count": "Int:77239"
                }
            },
            "Province:western": {
...
```

- Source File: [lanka_data.json (343.6 KB)](../../data/House-CookingFuel/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "firewood": 3381781,
            "kerosene": 32974,
            "gas": 2588502,
            "electricity": 19540,
            "sawdust_paddy_husk": 1739,
            "bio_gas": 7179,
            "other": 2361,
            "not_relevant": 77239
        },
        "total_value": 6111315
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "firewood": 433777,
            "kerosene": 15637,
            "gas": 1203412,
            "electricity": 10508,
            "sawdust_paddy_husk": 303,
            "bio_gas": 356,
            "other": 1152,
            "not_relevant": 38275
...
```

- Source File: [House-CookingFuel/data.json (5.1 MB)](../../data/House-CookingFuel/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | firewood | kerosene | gas | electricity | sawdust_paddy_husk | bio_gas | other | not_relevant |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6111315 | 3381781 | 32974 | 2588502 | 19540 | 1739 | 7179 | 2361 | 77239 |
| LK-1 | Western | province | 1703420 | 433777 | 15637 | 1203412 | 10508 | 303 | 356 | 1152 | 38275 |
| LK-2 | Central | province | 749019 | 489749 | 2717 | 249179 | 2191 | 84 | 559 | 175 | 4365 |
| LK-6 | North Western | province | 745193 | 534964 | 2782 | 195933 | 1394 | 35 | 570 | 272 | 9243 |
| LK-3 | Southern | province | 728288 | 438164 | 1173 | 277959 | 1226 | 89 | 82 | 304 | 9291 |
| LK-12 | Gampaha | district | 688635 | 218798 | 5137 | 439916 | 3068 | 126 | 131 | 633 | 20826 |
| EC-02 | Gampaha | ed | 688635 | 218798 | 5137 | 439916 | 3068 | 126 | 131 | 633 | 20826 |
| LK-11 | Colombo | district | 661822 | 65584 | 9106 | 566183 | 6425 | 134 | 157 | 380 | 13853 |
| EC-01 | Colombo | ed | 661822 | 65584 | 9106 | 566183 | 6425 | 134 | 157 | 380 | 13853 |
| LK-9 | Sabaragamuwa | province | 571682 | 433669 | 1060 | 131384 | 960 | 32 | 23 | 154 | 4400 |
| LK-61 | Kurunegala | district | 511166 | 394682 | 677 | 108665 | 1015 | 13 | 45 | 158 | 5911 |
| EC-15 | Kurunegala | ed | 511166 | 394682 | 677 | 108665 | 1015 | 13 | 45 | 158 | 5911 |
| LK-5 | Eastern | province | 499217 | 232633 | 5032 | 251630 | 1291 | 1007 | 3557 | 111 | 3956 |
| LK-7 | North Central | province | 402469 | 304792 | 737 | 92753 | 560 | 12 | 186 | 103 | 3326 |
| LK-8 | Uva | province | 400025 | 327040 | 957 | 68808 | 988 | 82 | 32 | 50 | 2068 |
| LK-21 | Kandy | district | 397626 | 231787 | 1321 | 160277 | 1447 | 51 | 24 | 110 | 2609 |
| EC-04 | Kandy | ed | 397626 | 231787 | 1321 | 160277 | 1447 | 51 | 24 | 110 | 2609 |
| LK-13 | Kalutara | district | 352963 | 149395 | 1394 | 197313 | 1015 | 43 | 68 | 139 | 3596 |
| EC-03 | Kalutara | ed | 352963 | 149395 | 1394 | 197313 | 1015 | 43 | 68 | 139 | 3596 |
| LK-91 | Ratnapura | district | 327645 | 255732 | 687 | 68039 | 493 | 19 | 11 | 67 | 2597 |

- Source File: [House-CookingFuel/data.tsv (770.5 KB)](../../data/House-CookingFuel/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
