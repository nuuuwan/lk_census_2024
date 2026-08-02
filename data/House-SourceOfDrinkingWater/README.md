# House-SourceOfDrinkingWater

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02-green)

*House-SourceOfDrinkingWater, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "Country:sri_lanka": {
                "SourceOfDrinkingWater:protected_well": {
                    "Count": "Int:1624506"
                },
                "SourceOfDrinkingWater:semi_protected_well": {
                    "Count": "Int:267327"
                },
                "SourceOfDrinkingWater:unprotected_well": {
                    "Count": "Int:77806"
                },
                "SourceOfDrinkingWater:tube_well": {
                    "Count": "Int:270401"
                },
                "SourceOfDrinkingWater:spring_or_fountain": {
                    "Count": "Int:230268"
                },
                "SourceOfDrinkingWater:pipe_borne_nwsdb": {
                    "Count": "Int:2374349"
                },
                "SourceOfDrinkingWater:pipe_borne_local": {
                    "Count": "Int:100764"
                },
                "SourceOfDrinkingWater:pipe_borne_comm": {
                    "Count": "Int:419247"
                },
                "SourceOfDrinkingWater:pipe_borne_private": {
                    "Count": "Int:130394"
...
```

- Source File: [lanka_data.json (744.8 KB)](../../data/House-SourceOfDrinkingWater/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "protected_well": 1624506,
            "semi_protected_well": 267327,
            "unprotected_well": 77806,
            "tube_well": 270401,
            "spring_fountain": 230268,
            "pipe_borne_nwsdb": 2374349,
            "pipe_borne_local_authority": 100764,
            "pipe_borne_community": 419247,
            "pipe_borne_private": 130394,
            "tank_river_stream": 59336,
            "rain_water": 4346,
            "bottled_water": 63753,
            "filter_ro": 456849,
            "bowser": 31208,
            "other": 761
        },
        "total_value": 6111315
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "protected_well": 547468,
...
```

- Source File: [data.json (8.5 MB)](../../data/House-SourceOfDrinkingWater/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | protected_well | semi_protected_well | unprotected_well | tube_well | spring_fountain | pipe_borne_nwsdb | pipe_borne_local_authority | pipe_borne_community | pipe_borne_private | tank_river_stream | rain_water | bottled_water | filter_ro | bowser | other |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6111315 | 1624506 | 267327 | 77806 | 270401 | 230268 | 2374349 | 100764 | 419247 | 130394 | 59336 | 4346 | 63753 | 456849 | 31208 | 761 |
| LK-1 | Western | province | 1703420 | 547468 | 47227 | 9979 | 45657 | 5123 | 983503 | 9099 | 39974 | 9811 | 1849 | 114 | 3140 | 128 | 95 | 253 |
| LK-2 | Central | province | 749019 | 91497 | 21372 | 9024 | 16174 | 96127 | 299310 | 44481 | 92552 | 39614 | 24126 | 382 | 1576 | 11453 | 1199 | 132 |
| LK-6 | North Western | province | 745193 | 281852 | 58067 | 12442 | 53483 | 4291 | 63057 | 5932 | 37229 | 11245 | 954 | 1816 | 38618 | 157245 | 18926 | 36 |
| LK-3 | Southern | province | 728288 | 239865 | 47351 | 15823 | 6870 | 12729 | 315660 | 6322 | 48336 | 15673 | 6369 | 134 | 4677 | 7877 | 545 | 57 |
| LK-12 | Gampaha | district | 688635 | 318367 | 26537 | 4401 | 35031 | 755 | 281959 | 3870 | 13137 | 2066 | 67 | 56 | 2229 | 70 | 49 | 41 |
| EC-02 | Gampaha | ed | 688635 | 318367 | 26537 | 4401 | 35031 | 755 | 281959 | 3870 | 13137 | 2066 | 67 | 56 | 2229 | 70 | 49 | 41 |
| LK-11 | Colombo | district | 661822 | 78469 | 3522 | 568 | 3649 | 1344 | 558425 | 3720 | 9703 | 1278 | 124 | 24 | 720 | 55 | 22 | 199 |
| EC-01 | Colombo | ed | 661822 | 78469 | 3522 | 568 | 3649 | 1344 | 558425 | 3720 | 9703 | 1278 | 124 | 24 | 720 | 55 | 22 | 199 |
| LK-9 | Sabaragamuwa | province | 571682 | 181561 | 30748 | 10767 | 6083 | 65092 | 125630 | 8699 | 92907 | 34084 | 14417 | 144 | 969 | 463 | 33 | 85 |
| LK-61 | Kurunegala | district | 511166 | 239671 | 51665 | 11319 | 13182 | 4192 | 37062 | 4432 | 23132 | 3945 | 817 | 992 | 21353 | 98172 | 1229 | 3 |
| EC-15 | Kurunegala | ed | 511166 | 239671 | 51665 | 11319 | 13182 | 4192 | 37062 | 4432 | 23132 | 3945 | 817 | 992 | 21353 | 98172 | 1229 | 3 |
| LK-5 | Eastern | province | 499217 | 83224 | 14057 | 4964 | 50650 | 734 | 319708 | 2697 | 9774 | 771 | 585 | 80 | 736 | 9859 | 1278 | 100 |
| LK-7 | North Central | province | 402469 | 27167 | 3488 | 1125 | 3067 | 5351 | 91184 | 7187 | 24505 | 3245 | 532 | 745 | 7785 | 226167 | 906 | 15 |
| LK-8 | Uva | province | 400025 | 68602 | 14099 | 5774 | 6877 | 40628 | 140265 | 10265 | 70074 | 14065 | 9990 | 492 | 865 | 17645 | 364 | 20 |
| LK-21 | Kandy | district | 397626 | 48571 | 12629 | 4082 | 4492 | 31494 | 214501 | 30434 | 32975 | 10688 | 5875 | 180 | 256 | 1135 | 278 | 36 |
| EC-04 | Kandy | ed | 397626 | 48571 | 12629 | 4082 | 4492 | 31494 | 214501 | 30434 | 32975 | 10688 | 5875 | 180 | 256 | 1135 | 278 | 36 |
| LK-13 | Kalutara | district | 352963 | 150632 | 17168 | 5010 | 6977 | 3024 | 143119 | 1509 | 17134 | 6467 | 1658 | 34 | 191 | 3 | 24 | 13 |
| EC-03 | Kalutara | ed | 352963 | 150632 | 17168 | 5010 | 6977 | 3024 | 143119 | 1509 | 17134 | 6467 | 1658 | 34 | 191 | 3 | 24 | 13 |
| LK-91 | Ratnapura | district | 327645 | 81576 | 15256 | 5403 | 4393 | 31390 | 68401 | 6446 | 75318 | 26515 | 11637 | 76 | 724 | 448 | 27 | 35 |

- Source File: [data.tsv (996.7 KB)](../../data/House-SourceOfDrinkingWater/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
