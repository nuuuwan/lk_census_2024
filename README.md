# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_16:48:00-green)

## XLSX Data Tables (12)

The following datasets have been extracted from the XLSX source documents:

### 01. [Population-Gender](data/Population-Gender)

- [📄 JSON](data/Population-Gender/data.json)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 7640,
    "values": {
        "male": 3864,
        "female": 3776
    },
    "total_value": 7640
}
```

### 02. [Population-Ethnicity](data/Population-Ethnicity)

- [📄 JSON](data/Population-Ethnicity/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Ethnic_Group.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-1103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 7640,
    "values": {
        "sinhalese": 3234,
        "sri_lanka_tamil": 2485,
        "indian_malaiyaga_tamil": 32,
        "sri_lanka_moor_muslim": 1865,
        "burgher": 16,
        "malay": 0,
        "sri_lanka_chetty": 0,
        "bharatha": 0,
        "veddha": 0,
        "other": 8
    },
    "total_value": 7640
}
```

### 03. [Population-Religion](data/Population-Religion)

- [📄 JSON](data/Population-Religion/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Religion.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-1103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 7640,
    "values": {
        "buddhist": 2597,
        "hindu": 1531,
        "islam": 1919,
        "roman_catholic": 1026,
        "other_christian": 567,
        "other": 0
    },
    "total_value": 7640
}
```

### 04. [Population-AgeGroup](data/Population-AgeGroup)

- [📄 JSON](data/Population-AgeGroup/data.json)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Five_Year_Age_Group.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-1103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 7640,
    "values": {
        "00_04": 464,
        "05_09": 581,
        "10_14": 650,
        "15_19": 731,
        "20_24": 689,
        "25_29": 577,
        "30_34": 502,
        "35_39": 462,
        "40_44": 563,
        "45_49": 537,
        "50_54": 424,
        "55_59": 406,
        "60_64": 393,
        "65_69": 307,
        "70_74": 185,
        "75_79": 107,
        "80_84": 40,
        "85_89": 16,
        "90_94": 4,
        "95_and_above": 2
    },
    "total_value": 7640
}
```

### 05. [Housing-Structure](data/Housing-Structure)

- [📄 JSON](data/Housing-Structure/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1834,
    "values": {
        "single_house_single_storeyed": 1405,
        "single_house_two_storeyed": 169,
        "single_house_more_than_two_storeyed": 3,
        "attached_house_1st_floor": 156,
        "attached_house_2nd_floor": 101,
        "attached_house_from_3_to_4_floors": 0,
        "attached_house_from_5_to_10_floors": 0,
        "attached_house_from_11_to_19_floors": 0,
        "attached_house_from_20_floors_or_more": 0,
        "other": 0
    },
    "total_value": 1834
}
```

### 06. [Housing-Walls](data/Housing-Walls)

- [📄 JSON](data/Housing-Walls/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1834,
    "values": {
        "bricks": 232,
        "cement_block": 1517,
        "granite_cube_stones": 1,
        "cabook": 1,
        "pressed_soil_bricks": 0,
        "warichchi_mud": 0,
        "cadjan_palmyrah": 0,
        "planks_metal_sheets_asbestos": 83,
        "zink_aluminium_sheets": 0,
        "other": 0,
        "not_relevant": 0
    },
    "total_value": 1834
}
```

### 07. [Housing-Floor](data/Housing-Floor)

- [📄 JSON](data/Housing-Floor/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1834,
    "values": {
        "cement": 1577,
        "terrazzo_tile_granite_wood_finished": 231,
        "concrete": 14,
        "mud": 0,
        "wood": 12,
        "sand": 0,
        "other": 0,
        "not_relevant": 0
    },
    "total_value": 1834
}
```

### 08. [Housing-Roof](data/Housing-Roof)

- [📄 JSON](data/Housing-Roof/data.json)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1834,
    "values": {
        "tile": 1,
        "asbestos": 1580,
        "concrete": 120,
        "zink_aluminium_sheet": 32,
        "metal_sheet": 94,
        "cadjan_palmyrah_straw": 7,
        "other": 0,
        "not_relevant": 0
    },
    "total_value": 1834
}
```

### 09. [Housing-Water](data/Housing-Water)

- [📄 JSON](data/Housing-Water/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1859,
    "values": {
        "protected_well": 4,
        "semi_protected_well": 3,
        "unprotected_well": 0,
        "tube_well": 1,
        "spring_fountain": 0,
        "pipe_borne_nwsdb": 1846,
        "pipe_borne_local_authority": 5,
        "pipe_borne_community": 0,
        "pipe_borne_private": 0,
        "tank_river_stream": 0,
        "rain_water": 0,
        "bottled_water": 0,
        "filter_ro": 0,
        "bowser": 0,
        "other": 0
    },
    "total_value": 1859
}
```

### 10. [Housing-Cooking-Fuel](data/Housing-Cooking-Fuel)

- [📄 JSON](data/Housing-Cooking-Fuel/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1859,
    "values": {
        "firewood": 91,
        "kerosene": 248,
        "gas": 1436,
        "electricity": 4,
        "sawdust_paddy_husk": 0,
        "bio_gas": 0,
        "other": 0,
        "not_relevant": 80
    },
    "total_value": 1859
}
```

### 11. [Housing-Lighting](data/Housing-Lighting)

- [📄 JSON](data/Housing-Lighting/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1859,
    "values": {
        "electricity_grid": 1817,
        "kerosene_lamp": 24,
        "solar_grid": 0,
        "solar_standalone": 0,
        "bio_gas": 0,
        "generator": 0,
        "other": 18
    },
    "total_value": 1859
}
```

### 12. [Housing-Toilet](data/Housing-Toilet)

- [📄 JSON](data/Housing-Toilet/data.json)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "gnd_id": "LK-11103005",
    "gnd_name_from_source": "Sammanthranapura",
    "total_value_from_source": 1859,
    "values": {
        "within_unit_exclusive": 1645,
        "within_unit_shared": 40,
        "within_premises_exclusive": 5,
        "within_premises_shared": 10,
        "no_toilet_sharing": 31,
        "common_public": 127,
        "none": 1
    },
    "total_value": 1859
}
```

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
