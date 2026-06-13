# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_17:34:44-green)

## XLSX Data Tables (12)

The following datasets have been extracted from the XLSX source documents:

### 01. [Population-Gender](data/Population-Gender)

- [📄 JSON](data/Population-Gender/data.json)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "male": 10510620,
        "female": 11267437
    },
    "total_value": 21778057
}
```

### 02. [Population-Ethnicity](data/Population-Ethnicity)

- [📄 JSON](data/Population-Ethnicity/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Ethnic_Group.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "sinhalese": 16140676,
        "sri_lanka_tamil": 2662191,
        "indian_malaiyaga_tamil": 590087,
        "sri_lanka_moor_muslim": 2274107,
        "burgher": 25091,
        "malay": 22838,
        "sri_lanka_chetty": 1753,
        "bharatha": 553,
        "veddha": 1287,
        "other": 59474
    },
    "total_value": 21778057
}
```

### 03. [Population-Religion](data/Population-Religion)

- [📄 JSON](data/Population-Religion/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Religion.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "buddhist": 15196960,
        "hindu": 2715045,
        "islam": 2327340,
        "roman_catholic": 1208849,
        "other_christian": 266380,
        "other": 63483
    },
    "total_value": 21778057
}
```

### 04. [Population-AgeGroup](data/Population-AgeGroup)

- [📄 JSON](data/Population-AgeGroup/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Five_Year_Age_Group.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "00_04": 1214840,
        "05_09": 1556256,
        "10_14": 1734881,
        "15_19": 1794693,
        "20_24": 1608311,
        "25_29": 1372173,
        "30_34": 1413829,
        "35_39": 1452470,
        "40_44": 1602090,
        "45_49": 1490507,
        "50_54": 1341592,
        "55_59": 1275868,
        "60_64": 1183138,
        "65_69": 991646,
        "70_74": 795413,
        "75_79": 522918,
        "80_84": 268388,
        "85_89": 111022,
        "90_94": 39231,
        "95_and_above": 8791
    },
    "total_value": 21778057
}
```

### 05. [Housing-Structure](data/Housing-Structure)

- [📄 JSON](data/Housing-Structure/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "single_house_single_storeyed": 4957093,
        "single_house_two_storeyed": 751296,
        "single_house_more_than_two_storeyed": 59478,
        "attached_house_1st_floor": 164412,
        "attached_house_2nd_floor": 50030,
        "attached_house_from_3_to_4_floors": 25373,
        "attached_house_from_5_to_10_floors": 12853,
        "attached_house_from_11_to_19_floors": 6031,
        "attached_house_from_20_floors_or_more": 1756,
        "other": 1211
    },
    "total_value": 6029533
}
```

### 06. [Housing-Walls](data/Housing-Walls)

- [📄 JSON](data/Housing-Walls/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "bricks": 2799139,
        "cement_block": 2827814,
        "granite_cube_stones": 95716,
        "cabook": 68496,
        "pressed_soil_bricks": 111245,
        "warichchi_mud": 70011,
        "cadjan_palmyrah": 7649,
        "planks_metal_sheets_asbestos": 43243,
        "zink_aluminium_sheets": 3869,
        "other": 1140,
        "not_relevant": 1211
    },
    "total_value": 6029533
}
```

### 07. [Housing-Floor](data/Housing-Floor)

- [📄 JSON](data/Housing-Floor/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "cement": 3709380,
        "terrazzo_tile_granite_wood_finished": 1692537,
        "concrete": 498824,
        "mud": 115259,
        "wood": 2579,
        "sand": 7705,
        "other": 2038,
        "not_relevant": 1211
    },
    "total_value": 6029533
}
```

### 08. [Housing-Roof](data/Housing-Roof)

- [📄 JSON](data/Housing-Roof/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "tile": 2031683,
        "asbestos": 3209441,
        "concrete": 440610,
        "zink_aluminium_sheet": 85411,
        "metal_sheet": 163715,
        "cadjan_palmyrah_straw": 88811,
        "other": 8651,
        "not_relevant": 1211
    },
    "total_value": 6029533
}
```

### 09. [Housing-Water](data/Housing-Water)

- [📄 JSON](data/Housing-Water/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "protected_well": 1624274,
        "semi_protected_well": 267317,
        "unprotected_well": 77801,
        "tube_well": 270311,
        "spring_fountain": 230268,
        "pipe_borne_nwsdb": 2373682,
        "pipe_borne_local_authority": 100763,
        "pipe_borne_community": 419246,
        "pipe_borne_private": 130394,
        "tank_river_stream": 59334,
        "rain_water": 4346,
        "bottled_water": 63748,
        "filter_ro": 456849,
        "bowser": 31208,
        "other": 761
    },
    "total_value": 6110302
}
```

### 10. [Housing-Cooking-Fuel](data/Housing-Cooking-Fuel)

- [📄 JSON](data/Housing-Cooking-Fuel/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "firewood": 3381446,
        "kerosene": 32964,
        "gas": 2587844,
        "electricity": 19536,
        "sawdust_paddy_husk": 1738,
        "bio_gas": 7178,
        "other": 2361,
        "not_relevant": 77235
    },
    "total_value": 6110302
}
```

### 11. [Housing-Lighting](data/Housing-Lighting)

- [📄 JSON](data/Housing-Lighting/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "electricity_grid": 5986600,
        "kerosene_lamp": 95123,
        "solar_grid": 8093,
        "solar_standalone": 5816,
        "bio_gas": 244,
        "generator": 1230,
        "other": 13196
    },
    "total_value": 6110302
}
```

### 12. [Housing-Toilet](data/Housing-Toilet)

- [📄 JSON](data/Housing-Toilet/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "within_unit_exclusive": 3798384,
        "within_unit_shared": 157445,
        "within_premises_exclusive": 1832038,
        "within_premises_shared": 197658,
        "no_toilet_sharing": 101884,
        "common_public": 9567,
        "none": 13326
    },
    "total_value": 6110302
}
```

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
