# House-RoofType

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20-green)

*House-RoofType, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "Province:LK-1": {
                "RoofType:tile": {
                    "Count": "Int:363704"
                },
                "RoofType:asbestos": {
                    "Count": "Int:1098621"
                },
                "RoofType:concrete": {
                    "Count": "Int:190819"
                },
                "RoofType:zink_aluminium_sheet": {
                    "Count": "Int:10224"
                },
                "RoofType:metal_sheet": {
                    "Count": "Int:12480"
                },
                "RoofType:cadjan_palmyrah_straw": {
                    "Count": "Int:10085"
                },
                "RoofType:other": {
                    "Count": "Int:303"
                },
                "RoofType:not_relevant": {
                    "Count": "Int:270"
                }
            },
            "Province:LK-6": {
...
```

- Source File: [House-RoofType/lanka_data.json (5.6 KB)](../../data/House-RoofType/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "tile": 2032441,
            "asbestos": 3209496,
            "concrete": 440761,
            "zink_aluminium_sheet": 85422,
            "metal_sheet": 163735,
            "cadjan_palmyrah_straw": 88820,
            "other": 8655,
            "not_relevant": 1211
        },
        "total_value": 6030541
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "tile": 363704,
            "asbestos": 1098621,
            "concrete": 190819,
            "zink_aluminium_sheet": 10224,
            "metal_sheet": 12480,
            "cadjan_palmyrah_straw": 10085,
            "other": 303,
            "not_relevant": 270
...
```

- Source File: [data/House-RoofType/data.json (5.4 MB)](../../data/House-RoofType/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | tile | asbestos | concrete | zink_aluminium_sheet | metal_sheet | cadjan_palmyrah_straw | other | not_relevant |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6030541 | 2032441 | 3209496 | 440761 | 85422 | 163735 | 88820 | 8655 | 1211 |
| LK-1 | Western | province | 1686506 | 363704 | 1098621 | 190819 | 10224 | 12480 | 10085 | 303 | 270 |
| LK-6 | North Western | province | 738403 | 487945 | 192946 | 18700 | 9457 | 14211 | 12523 | 2511 | 110 |
| LK-2 | Central | province | 730925 | 66210 | 471886 | 83423 | 34464 | 53758 | 20521 | 573 | 90 |
| LK-3 | Southern | province | 722971 | 311194 | 365468 | 31230 | 2162 | 7330 | 5322 | 223 | 42 |
| LK-12 | Gampaha | district | 683025 | 245645 | 380955 | 43598 | 4169 | 5122 | 3374 | 104 | 58 |
| EC-02 | Gampaha | ed | 683025 | 245645 | 380955 | 43598 | 4169 | 5122 | 3374 | 104 | 58 |
| LK-11 | Colombo | district | 654051 | 40032 | 475061 | 128212 | 4065 | 3273 | 3109 | 132 | 167 |
| EC-01 | Colombo | ed | 654051 | 40032 | 475061 | 128212 | 4065 | 3273 | 3109 | 132 | 167 |
| LK-9 | Sabaragamuwa | province | 566880 | 149072 | 344798 | 26348 | 5632 | 21011 | 19831 | 146 | 42 |
| LK-61 | Kurunegala | district | 506909 | 306636 | 161307 | 14905 | 6032 | 10010 | 7506 | 475 | 38 |
| EC-15 | Kurunegala | ed | 506909 | 306636 | 161307 | 14905 | 6032 | 10010 | 7506 | 475 | 38 |
| LK-5 | Eastern | province | 489362 | 285586 | 121898 | 54518 | 7358 | 7875 | 8896 | 2813 | 418 |
| LK-7 | North Central | province | 397890 | 96127 | 280591 | 9748 | 2902 | 4495 | 3826 | 176 | 25 |
| LK-8 | Uva | province | 390145 | 90405 | 232820 | 18874 | 7033 | 36734 | 4085 | 163 | 31 |
| LK-21 | Kandy | district | 389826 | 29503 | 262248 | 58516 | 10412 | 16281 | 12775 | 60 | 31 |
| EC-04 | Kandy | ed | 389826 | 29503 | 262248 | 58516 | 10412 | 16281 | 12775 | 60 | 31 |
| LK-13 | Kalutara | district | 349430 | 78027 | 242605 | 19009 | 1990 | 4085 | 3602 | 67 | 45 |
| EC-03 | Kalutara | ed | 349430 | 78027 | 242605 | 19009 | 1990 | 4085 | 3602 | 67 | 45 |
| LK-91 | Ratnapura | district | 324853 | 72797 | 213350 | 12116 | 2200 | 12752 | 11529 | 93 | 16 |

- Source File: [data/House-RoofType/data.tsv (786.2 KB)](../../data/House-RoofType/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
