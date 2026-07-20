# Population-Gender

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20-green)

*Population-Gender, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "male": 10512344,
            "female": 11269456
        },
        "total_value": 21781800
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "male": 2961374,
            "female": 3155967
        },
        "total_value": 6117341
    },
    {
        "region_id": "LK-2",
        "region_name": "Central",
        "region_ent_type": "province",
        "values": {
            "male": 1298405,
            "female": 1415640
        },
        "total_value": 2714045
...
```

- Source File: [Population-Gender/data.json (3.2 MB)](../../data/Population-Gender/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | male | female |
| :-- | :-- | :-- | --: | :-- | :-- |
| LK | Sri Lanka | country | 21781800 | 10512344 | 11269456 |
| LK-1 | Western | province | 6117341 | 2961374 | 3155967 |
| LK-2 | Central | province | 2714045 | 1298405 | 1415640 |
| LK-3 | Southern | province | 2606679 | 1258830 | 1347849 |
| LK-6 | North Western | province | 2586972 | 1243316 | 1343656 |
| LK-12 | Gampaha | district | 2436142 | 1175469 | 1260673 |
| EC-02 | Gampaha | ed | 2436142 | 1175469 | 1260673 |
| LK-11 | Colombo | district | 2375415 | 1154799 | 1220616 |
| EC-01 | Colombo | ed | 2375415 | 1154799 | 1220616 |
| LK-9 | Sabaragamuwa | province | 2015899 | 978537 | 1037362 |
| LK-5 | Eastern | province | 1783214 | 850607 | 932607 |
| LK-61 | Kurunegala | district | 1768156 | 849072 | 919084 |
| EC-15 | Kurunegala | ed | 1768156 | 849072 | 919084 |
| LK-21 | Kandy | district | 1461895 | 696713 | 765182 |
| EC-04 | Kandy | ed | 1461895 | 696713 | 765182 |
| LK-7 | North Central | province | 1407610 | 686257 | 721353 |
| LK-8 | Uva | province | 1399892 | 683745 | 716147 |
| LK-13 | Kalutara | district | 1305784 | 631106 | 674678 |
| EC-03 | Kalutara | ed | 1305784 | 631106 | 674678 |
| LK-4 | Northern | province | 1150148 | 551273 | 598875 |

- Source File: [Population-Gender/data.tsv (614.7 KB)](../../data/Population-Gender/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GN_population_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
