# Housing-Toilet

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20-green)

*Housing-Toilet, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "within_unit_exclusive": 3798777,
            "within_unit_shared": 157456,
            "within_premises_exclusive": 1832587,
            "within_premises_shared": 197678,
            "no_toilet_sharing": 101924,
            "common_public": 9567,
            "none": 13326
        },
        "total_value": 6111315
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "within_unit_exclusive": 1402581,
            "within_unit_shared": 39527,
            "within_premises_exclusive": 206499,
            "within_premises_shared": 37544,
            "no_toilet_sharing": 11147,
            "common_public": 5440,
            "none": 682
        },
        "total_value": 1703420
...
```

- Source File: [data/Housing-Toilet/data.json (5.6 MB)](../../data/Housing-Toilet/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | within_unit_exclusive | within_unit_shared | within_premises_exclusive | within_premises_shared | no_toilet_sharing | common_public | none |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6111315 | 3798777 | 157456 | 1832587 | 197678 | 101924 | 9567 | 13326 |
| LK-1 | Western | province | 1703420 | 1402581 | 39527 | 206499 | 37544 | 11147 | 5440 | 682 |
| LK-2 | Central | province | 749019 | 458565 | 26474 | 219652 | 28760 | 12295 | 1882 | 1391 |
| LK-6 | North Western | province | 745193 | 407961 | 17499 | 277976 | 27876 | 11301 | 624 | 1956 |
| LK-3 | Southern | province | 728288 | 415171 | 13432 | 265541 | 21117 | 12060 | 375 | 592 |
| LK-12 | Gampaha | district | 688635 | 535542 | 18369 | 104375 | 24006 | 5395 | 699 | 249 |
| EC-02 | Gampaha | ed | 688635 | 535542 | 18369 | 104375 | 24006 | 5395 | 699 | 249 |
| LK-11 | Colombo | district | 661822 | 599062 | 13455 | 35126 | 7064 | 2390 | 4518 | 207 |
| EC-01 | Colombo | ed | 661822 | 599062 | 13455 | 35126 | 7064 | 2390 | 4518 | 207 |
| LK-9 | Sabaragamuwa | province | 571682 | 324428 | 14234 | 202930 | 18605 | 10520 | 394 | 571 |
| LK-61 | Kurunegala | district | 511166 | 273343 | 11009 | 198128 | 20141 | 7344 | 269 | 932 |
| EC-15 | Kurunegala | ed | 511166 | 273343 | 11009 | 198128 | 20141 | 7344 | 269 | 932 |
| LK-5 | Eastern | province | 499217 | 286398 | 14745 | 156914 | 16916 | 19498 | 258 | 4488 |
| LK-7 | North Central | province | 402469 | 193979 | 10318 | 170120 | 18899 | 7869 | 135 | 1149 |
| LK-8 | Uva | province | 400025 | 177500 | 14094 | 177759 | 20475 | 9071 | 245 | 881 |
| LK-21 | Kandy | district | 397626 | 273024 | 11299 | 96783 | 10586 | 4687 | 964 | 283 |
| EC-04 | Kandy | ed | 397626 | 273024 | 11299 | 96783 | 10586 | 4687 | 964 | 283 |
| LK-13 | Kalutara | district | 352963 | 267977 | 7703 | 66998 | 6474 | 3362 | 223 | 226 |
| EC-03 | Kalutara | ed | 352963 | 267977 | 7703 | 66998 | 6474 | 3362 | 223 | 226 |
| LK-91 | Ratnapura | district | 327645 | 168014 | 8805 | 129647 | 12884 | 7643 | 320 | 332 |

- Source File: [data/Housing-Toilet/data.tsv (754.4 KB)](../../data/Housing-Toilet/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
