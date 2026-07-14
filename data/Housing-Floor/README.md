# Housing-Floor

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Housing-Floor, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "cement": 3710163,
            "terrazzo_tile_granite_wood_finished": 1692659,
            "concrete": 498925,
            "mud": 115259,
            "wood": 2579,
            "sand": 7707,
            "other": 2038,
            "not_relevant": 1211
        },
        "total_value": 6030541
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "cement": 836713,
            "terrazzo_tile_granite_wood_finished": 754097,
            "concrete": 87793,
            "mud": 5688,
            "wood": 1159,
            "sand": 578,
            "other": 208,
            "not_relevant": 270
...
```

- Source File: [data.json (5.5 MB)](../../data/Housing-Floor/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | cement | terrazzo_tile_granite_wood_finished | concrete | mud | wood | sand | other | not_relevant |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6030541 | 3710163 | 1692659 | 498925 | 115259 | 2579 | 7707 | 2038 | 1211 |
| LK-1 | Western | province | 1686506 | 836713 | 754097 | 87793 | 5688 | 1159 | 578 | 208 | 270 |
| LK-6 | North Western | province | 738403 | 466494 | 173106 | 85119 | 11929 | 304 | 1117 | 224 | 110 |
| LK-2 | Central | province | 730925 | 486204 | 160536 | 58877 | 24089 | 361 | 385 | 383 | 90 |
| LK-3 | Southern | province | 722971 | 408910 | 236461 | 66411 | 10752 | 190 | 109 | 96 | 42 |
| LK-12 | Gampaha | district | 683025 | 356781 | 281209 | 41726 | 2515 | 307 | 318 | 111 | 58 |
| EC-02 | Gampaha | ed | 683025 | 356781 | 281209 | 41726 | 2515 | 307 | 318 | 111 | 58 |
| LK-11 | Colombo | district | 654051 | 284355 | 343281 | 24441 | 839 | 743 | 155 | 70 | 167 |
| EC-01 | Colombo | ed | 654051 | 284355 | 343281 | 24441 | 839 | 743 | 155 | 70 | 167 |
| LK-9 | Sabaragamuwa | province | 566880 | 369945 | 132390 | 47738 | 16283 | 180 | 176 | 126 | 42 |
| LK-61 | Kurunegala | district | 506909 | 313606 | 122146 | 60973 | 9610 | 105 | 331 | 100 | 38 |
| EC-15 | Kurunegala | ed | 506909 | 313606 | 122146 | 60973 | 9610 | 105 | 331 | 100 | 38 |
| LK-5 | Eastern | province | 489362 | 392963 | 54405 | 30161 | 7006 | 93 | 3989 | 327 | 418 |
| LK-7 | North Central | province | 397890 | 249106 | 69140 | 68233 | 11145 | 46 | 138 | 57 | 25 |
| LK-8 | Uva | province | 390145 | 249488 | 68548 | 47422 | 24260 | 132 | 176 | 88 | 31 |
| LK-21 | Kandy | district | 389826 | 237497 | 113150 | 29352 | 9450 | 183 | 106 | 57 | 31 |
| EC-04 | Kandy | ed | 389826 | 237497 | 113150 | 29352 | 9450 | 183 | 106 | 57 | 31 |
| LK-13 | Kalutara | district | 349430 | 195577 | 129607 | 21626 | 2334 | 109 | 105 | 27 | 45 |
| EC-03 | Kalutara | ed | 349430 | 195577 | 129607 | 21626 | 2334 | 109 | 105 | 27 | 45 |
| LK-91 | Ratnapura | district | 324853 | 214822 | 69734 | 28715 | 11298 | 101 | 105 | 62 | 16 |

- Source File: [data.tsv (802.5 kB)](../../data/Housing-Floor/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
