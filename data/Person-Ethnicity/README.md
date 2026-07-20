# Person-Ethnicity

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20-green)

*Person-Ethnicity, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "sinhalese": 16140688,
            "sri_lanka_tamil": 2665574,
            "indian_malaiyaga_tamil": 590087,
            "sri_lanka_moor_muslim": 2274372,
            "burgher": 25159,
            "malay": 22838,
            "sri_lanka_chetty": 1753,
            "bharatha": 553,
            "veddha": 1287,
            "other": 59489
        },
        "total_value": 21781800
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "sinhalese": 5115543,
            "sri_lanka_tamil": 379680,
            "indian_malaiyaga_tamil": 26271,
            "sri_lanka_moor_muslim": 542333,
            "burgher": 15725,
            "malay": 16126,
...
```

- Source File: [Person-Ethnicity/data.json (6.1 MB)](../../data/Person-Ethnicity/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | sinhalese | sri_lanka_tamil | indian_malaiyaga_tamil | sri_lanka_moor_muslim | burgher | malay | sri_lanka_chetty | bharatha | veddha | other |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 21781800 | 16140688 | 2665574 | 590087 | 2274372 | 25159 | 22838 | 1753 | 553 | 1287 | 59489 |
| LK-1 | Western | province | 6117341 | 5115543 | 379680 | 26271 | 542333 | 15725 | 16126 | 1753 | 553 | 0 | 19357 |
| LK-2 | Central | province | 2714045 | 1783899 | 222924 | 406956 | 289281 | 2395 | 952 | 0 | 0 | 0 | 7638 |
| LK-3 | Southern | province | 2606679 | 2470423 | 27994 | 10187 | 88145 | 127 | 3882 | 0 | 0 | 0 | 5921 |
| LK-6 | North Western | province | 2586972 | 2193622 | 67272 | 1689 | 314035 | 1519 | 931 | 0 | 0 | 0 | 7904 |
| LK-12 | Gampaha | district | 2436142 | 2188512 | 96007 | 5392 | 121910 | 5607 | 8476 | 1704 | 205 | 0 | 8329 |
| EC-02 | Gampaha | ed | 2436142 | 2188512 | 96007 | 5392 | 121910 | 5607 | 8476 | 1704 | 205 | 0 | 8329 |
| LK-11 | Colombo | district | 2375415 | 1807945 | 243613 | 14412 | 284667 | 9885 | 7456 | 49 | 338 | 0 | 7050 |
| EC-01 | Colombo | ed | 2375415 | 1807945 | 243613 | 14412 | 284667 | 9885 | 7456 | 49 | 338 | 0 | 7050 |
| LK-9 | Sabaragamuwa | province | 2015899 | 1739900 | 130472 | 44395 | 96930 | 260 | 25 | 0 | 0 | 0 | 3917 |
| LK-5 | Eastern | province | 1783214 | 390538 | 677890 | 1221 | 703155 | 4503 | 367 | 0 | 0 | 898 | 4642 |
| LK-61 | Kurunegala | district | 1768156 | 1601886 | 19475 | 1028 | 139988 | 40 | 497 | 0 | 0 | 0 | 5242 |
| EC-15 | Kurunegala | ed | 1768156 | 1601886 | 19475 | 1028 | 139988 | 40 | 497 | 0 | 0 | 0 | 5242 |
| LK-21 | Kandy | district | 1461895 | 1077219 | 121452 | 37373 | 219175 | 1124 | 637 | 0 | 0 | 0 | 4915 |
| EC-04 | Kandy | ed | 1461895 | 1077219 | 121452 | 37373 | 219175 | 1124 | 637 | 0 | 0 | 0 | 4915 |
| LK-7 | North Central | province | 1407610 | 1272757 | 11147 | 173 | 119657 | 57 | 56 | 0 | 0 | 221 | 3542 |
| LK-8 | Uva | province | 1399892 | 1139983 | 95535 | 96469 | 63685 | 548 | 499 | 0 | 0 | 168 | 3005 |
| LK-13 | Kalutara | district | 1305784 | 1119086 | 40060 | 6467 | 135756 | 233 | 194 | 0 | 10 | 0 | 3978 |
| EC-03 | Kalutara | ed | 1305784 | 1119086 | 40060 | 6467 | 135756 | 233 | 194 | 0 | 10 | 0 | 3978 |
| LK-4 | Northern | province | 1150148 | 34023 | 1052660 | 2726 | 57151 | 25 | 0 | 0 | 0 | 0 | 3563 |

- Source File: [data/Person-Ethnicity/data.tsv (843.1 KB)](../../data/Person-Ethnicity/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Ethnic_Group>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
