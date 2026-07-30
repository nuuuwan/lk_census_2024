# House-Lighting

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*House-Lighting, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "House": {
        "Time:2024": {
            "Country:sri_lanka": {
                "Lighting:electricity_grid": {
                    "Count": "Int:5987585"
                },
                "Lighting:kerosene": {
                    "Count": "Int:95150"
                },
                "Lighting:solar_grid": {
                    "Count": "Int:8093"
                },
                "Lighting:solar_standalone": {
                    "Count": "Int:5817"
                },
                "Lighting:bio_gas": {
                    "Count": "Int:244"
                },
                "Lighting:generator": {
                    "Count": "Int:1230"
                },
                "Lighting:other": {
                    "Count": "Int:13196"
                }
            },
            "Province:western": {
                "Lighting:electricity_grid": {
                    "Count": "Int:1682433"
                },
...
```

- Source File: [House-Lighting/lanka_data.json (294.3 KB)](../../data/House-Lighting/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK",
        "region_name": "Sri Lanka",
        "region_ent_type": "country",
        "values": {
            "electricity_grid": 5987585,
            "kerosene_lamp": 95150,
            "solar_grid": 8093,
            "solar_standalone": 5817,
            "bio_gas": 244,
            "generator": 1230,
            "other": 13196
        },
        "total_value": 6111315
    },
    {
        "region_id": "LK-1",
        "region_name": "Western",
        "region_ent_type": "province",
        "values": {
            "electricity_grid": 1682433,
            "kerosene_lamp": 10565,
            "solar_grid": 5206,
            "solar_standalone": 1514,
            "bio_gas": 121,
            "generator": 288,
            "other": 3293
        },
        "total_value": 1703420
...
```

- Source File: [data/House-Lighting/data.json (5.0 MB)](../../data/House-Lighting/data.json)

## Structured TSV Data (similar to original layout) - First 20 rows

| region_id | region_name | region_ent_type | total_value | electricity_grid | kerosene_lamp | solar_grid | solar_standalone | bio_gas | generator | other |
| :-- | :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK | Sri Lanka | country | 6111315 | 5987585 | 95150 | 8093 | 5817 | 244 | 1230 | 13196 |
| LK-1 | Western | province | 1703420 | 1682433 | 10565 | 5206 | 1514 | 121 | 288 | 3293 |
| LK-2 | Central | province | 749019 | 736755 | 9880 | 360 | 495 | 27 | 127 | 1375 |
| LK-6 | North Western | province | 745193 | 729060 | 13132 | 553 | 1252 | 28 | 164 | 1004 |
| LK-3 | Southern | province | 728288 | 717303 | 7272 | 705 | 496 | 11 | 76 | 2425 |
| LK-12 | Gampaha | district | 688635 | 680337 | 4340 | 1724 | 479 | 50 | 70 | 1635 |
| EC-02 | Gampaha | ed | 688635 | 680337 | 4340 | 1724 | 479 | 50 | 70 | 1635 |
| LK-11 | Colombo | district | 661822 | 653295 | 3366 | 2900 | 831 | 58 | 192 | 1180 |
| EC-01 | Colombo | ed | 661822 | 653295 | 3366 | 2900 | 831 | 58 | 192 | 1180 |
| LK-9 | Sabaragamuwa | province | 571682 | 558898 | 10307 | 203 | 542 | 8 | 193 | 1531 |
| LK-61 | Kurunegala | district | 511166 | 501299 | 8332 | 313 | 509 | 4 | 37 | 672 |
| EC-15 | Kurunegala | ed | 511166 | 501299 | 8332 | 313 | 509 | 4 | 37 | 672 |
| LK-5 | Eastern | province | 499217 | 479020 | 18042 | 393 | 213 | 17 | 102 | 1430 |
| LK-7 | North Central | province | 402469 | 392571 | 8494 | 206 | 440 | 12 | 31 | 715 |
| LK-8 | Uva | province | 400025 | 389582 | 8556 | 183 | 571 | 8 | 93 | 1032 |
| LK-21 | Kandy | district | 397626 | 392207 | 4108 | 243 | 235 | 11 | 40 | 782 |
| EC-04 | Kandy | ed | 397626 | 392207 | 4108 | 243 | 235 | 11 | 40 | 782 |
| LK-13 | Kalutara | district | 352963 | 348801 | 2859 | 582 | 204 | 13 | 26 | 478 |
| EC-03 | Kalutara | ed | 352963 | 348801 | 2859 | 582 | 204 | 13 | 26 | 478 |
| LK-91 | Ratnapura | district | 327645 | 319263 | 6656 | 135 | 368 | 5 | 165 | 1053 |

- Source File: [data/House-Lighting/data.tsv (722.8 KB)](../../data/House-Lighting/data.tsv)

## Source

- <https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
