# House-WallType

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27-green)

*House-WallType, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "Country:sri_lanka": {
                "WallType:bricks": {
                    "Count": "Int:2799913"
                },
                "WallType:cement_block": {
                    "Count": "Int:2828027"
                },
                "WallType:granite_cube_stones": {
                    "Count": "Int:95717"
                },
                "WallType:cabook": {
                    "Count": "Int:68497"
                },
                "WallType:pressed_soil_bricks": {
                    "Count": "Int:111245"
                },
                "WallType:warichchi_mud": {
                    "Count": "Int:70011"
                },
                "WallType:cadjan_palmyrah": {
                    "Count": "Int:7650"
                },
                "WallType:planks_metal_sheets_asbestos": {
                    "Count": "Int:43260"
                },
                "WallType:zink_aluminium_sheets": {
                    "Count": "Int:3870"
...
```

- Source File: [House-WallType/lanka_data.json (477.1 KB)](../../data/House-WallType/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "bricks": 2799913,
            "cement_block": 2828027,
            "granite_cube_stones": 95717,
            "cabook": 68497,
            "pressed_soil_bricks": 111245,
            "warichchi_mud": 70011,
            "cadjan_palmyrah": 7650,
            "planks_metal_sheets_asbestos": 43260,
            "zink_aluminium_sheets": 3870,
            "other": 1140,
            "not_relevant": 1211
        },
        "total_value": 6030541
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "bricks": 444198,
            "cement_block": 1147193,
            "granite_cube_stones": 8468,
            "cabook": 48401,
            "pressed_soil_bricks": 15695,
...
```

- Source File: [data/House-WallType/data.json (6.9 MB)](../../data/House-WallType/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | bricks | cement_block | granite_cube_stones | cabook | pressed_soil_bricks | warichchi_mud | cadjan_palmyrah | planks_metal_sheets_asbestos | zink_aluminium_sheets | other | not_relevant |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6030541 | 2799913 | 2828027 | 95717 | 68497 | 111245 | 70011 | 7650 | 43260 | 3870 | 1140 | 1211 |
| LK-1 | Western | province | 1686506 | 444198 | 1147193 | 8468 | 48401 | 15695 | 9478 | 122 | 12045 | 407 | 229 | 270 |
| LK-6 | North Western | province | 738403 | 595052 | 118669 | 725 | 365 | 5526 | 7102 | 3440 | 6863 | 437 | 114 | 110 |
| LK-2 | Central | province | 730925 | 282854 | 363613 | 49021 | 1925 | 21108 | 8484 | 35 | 3318 | 332 | 145 | 90 |
| LK-3 | Southern | province | 722971 | 365930 | 313267 | 4658 | 10786 | 14814 | 9670 | 41 | 3546 | 111 | 106 | 42 |
| LK-12 | Gampaha | district | 683025 | 236563 | 414130 | 1848 | 10253 | 8882 | 6545 | 47 | 4439 | 179 | 81 | 58 |
| EC-02 | Gampaha | ed | 683025 | 236563 | 414130 | 1848 | 10253 | 8882 | 6545 | 47 | 4439 | 179 | 81 | 58 |
| LK-11 | Colombo | district | 654051 | 166151 | 462409 | 2691 | 14988 | 1597 | 675 | 57 | 5109 | 151 | 56 | 167 |
| EC-01 | Colombo | ed | 654051 | 166151 | 462409 | 2691 | 14988 | 1597 | 675 | 57 | 5109 | 151 | 56 | 167 |
| LK-9 | Sabaragamuwa | province | 566880 | 181919 | 329020 | 20115 | 4235 | 12675 | 15673 | 42 | 2909 | 84 | 166 | 42 |
| LK-61 | Kurunegala | district | 506909 | 445527 | 48013 | 506 | 242 | 4455 | 5643 | 163 | 2066 | 167 | 89 | 38 |
| EC-15 | Kurunegala | ed | 506909 | 445527 | 48013 | 506 | 242 | 4455 | 5643 | 163 | 2066 | 167 | 89 | 38 |
| LK-5 | Eastern | province | 489362 | 361634 | 108255 | 482 | 217 | 1475 | 4504 | 2306 | 8428 | 1599 | 44 | 418 |
| LK-7 | North Central | province | 397890 | 335859 | 53722 | 238 | 108 | 1936 | 5107 | 57 | 667 | 123 | 48 | 25 |
| LK-8 | Uva | province | 390145 | 215064 | 114216 | 11494 | 2313 | 36894 | 8617 | 38 | 1089 | 135 | 254 | 31 |
| LK-21 | Kandy | district | 389826 | 154206 | 203208 | 17852 | 689 | 8914 | 3835 | 8 | 955 | 95 | 33 | 31 |
| EC-04 | Kandy | ed | 389826 | 154206 | 203208 | 17852 | 689 | 8914 | 3835 | 8 | 955 | 95 | 33 | 31 |
| LK-13 | Kalutara | district | 349430 | 41484 | 270654 | 3929 | 23160 | 5216 | 2258 | 18 | 2497 | 77 | 92 | 45 |
| EC-03 | Kalutara | ed | 349430 | 41484 | 270654 | 3929 | 23160 | 5216 | 2258 | 18 | 2497 | 77 | 92 | 45 |
| LK-91 | Ratnapura | district | 324853 | 76597 | 212648 | 11625 | 2766 | 7159 | 12429 | 24 | 1440 | 47 | 102 | 16 |

- Source File: [data/House-WallType/data.tsv (864.7 KB)](../../data/House-WallType/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
