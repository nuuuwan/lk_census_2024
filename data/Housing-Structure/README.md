# Housing-Structure

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14-green)

*Housing-Structure, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "single_house_single_storeyed": 4958009,
            "single_house_two_storeyed": 751375,
            "single_house_more_than_two_storeyed": 59484,
            "attached_house_1st_floor": 164419,
            "attached_house_2nd_floor": 50030,
            "attached_house_from_3_to_4_floors": 25373,
            "attached_house_from_5_to_10_floors": 12853,
            "attached_house_from_11_to_19_floors": 6031,
            "attached_house_from_20_floors_or_more": 1756,
            "other": 1211
        },
        "total_value": 6030541
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "single_house_single_storeyed": 1177294,
            "single_house_two_storeyed": 360332,
            "single_house_more_than_two_storeyed": 32722,
            "attached_house_1st_floor": 44627,
            "attached_house_2nd_floor": 32464,
            "attached_house_from_3_to_4_floors": 18775,
...
```

- Source File: [data.json (8.9 MB)](../../data/Housing-Structure/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | single_house_single_storeyed | single_house_two_storeyed | single_house_more_than_two_storeyed | attached_house_1st_floor | attached_house_2nd_floor | attached_house_from_3_to_4_floors | attached_house_from_5_to_10_floors | attached_house_from_11_to_19_floors | attached_house_from_20_floors_or_more | other |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6030541 | 4958009 | 751375 | 59484 | 164419 | 50030 | 25373 | 12853 | 6031 | 1756 | 1211 |
| LK-1 | Western | province | 1686506 | 1177294 | 360332 | 32722 | 44627 | 32464 | 18775 | 12272 | 5994 | 1756 | 270 |
| LK-6 | North Western | province | 738403 | 681543 | 52350 | 1295 | 2143 | 785 | 139 | 38 | 0 | 0 | 110 |
| LK-2 | Central | province | 730925 | 539831 | 95235 | 11754 | 70508 | 9149 | 3866 | 469 | 23 | 0 | 90 |
| LK-3 | Southern | province | 722971 | 615514 | 91046 | 5317 | 6959 | 3271 | 748 | 60 | 14 | 0 | 42 |
| LK-12 | Gampaha | district | 683025 | 534645 | 123034 | 6482 | 10860 | 5848 | 1802 | 296 | 0 | 0 | 58 |
| EC-02 | Gampaha | ed | 683025 | 534645 | 123034 | 6482 | 10860 | 5848 | 1802 | 296 | 0 | 0 | 58 |
| LK-11 | Colombo | district | 654051 | 355982 | 185828 | 24207 | 27406 | 24275 | 16529 | 11907 | 5994 | 1756 | 167 |
| EC-01 | Colombo | ed | 654051 | 355982 | 185828 | 24207 | 27406 | 24275 | 16529 | 11907 | 5994 | 1756 | 167 |
| LK-9 | Sabaragamuwa | province | 566880 | 487757 | 56665 | 3513 | 17071 | 1485 | 347 | 0 | 0 | 0 | 42 |
| LK-61 | Kurunegala | district | 506909 | 463412 | 40530 | 1033 | 1274 | 512 | 96 | 14 | 0 | 0 | 38 |
| EC-15 | Kurunegala | ed | 506909 | 463412 | 40530 | 1033 | 1274 | 512 | 96 | 14 | 0 | 0 | 38 |
| LK-5 | Eastern | province | 489362 | 452172 | 32702 | 1365 | 1432 | 774 | 491 | 8 | 0 | 0 | 418 |
| LK-7 | North Central | province | 397890 | 373745 | 22469 | 559 | 581 | 393 | 117 | 1 | 0 | 0 | 25 |
| LK-8 | Uva | province | 390145 | 337782 | 27180 | 2355 | 20632 | 1384 | 781 | 0 | 0 | 0 | 31 |
| LK-21 | Kandy | district | 389826 | 291819 | 68443 | 8761 | 14534 | 4520 | 1237 | 458 | 23 | 0 | 31 |
| EC-04 | Kandy | ed | 389826 | 291819 | 68443 | 8761 | 14534 | 4520 | 1237 | 458 | 23 | 0 | 31 |
| LK-13 | Kalutara | district | 349430 | 286667 | 51470 | 2033 | 6361 | 2341 | 444 | 69 | 0 | 0 | 45 |
| EC-03 | Kalutara | ed | 349430 | 286667 | 51470 | 2033 | 6361 | 2341 | 444 | 69 | 0 | 0 | 45 |
| LK-91 | Ratnapura | district | 324853 | 285973 | 26214 | 1609 | 10176 | 674 | 191 | 0 | 0 | 0 | 16 |

- Source File: [data.tsv (846.3 kB)](../../data/Housing-Structure/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
