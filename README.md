# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_16:04:04-green)

## XLSX Data Tables (5)

The following datasets have been extracted from the XLSX source documents:

### 01. [Population-AgeGroup](data/Population-AgeGroup)

- [📄 JSON](data/Population-AgeGroup/data.json)
- [📄 TSV Table](data/Population-AgeGroup/data.tsv)
- [📊 Source XLSX](original_docs/GNLevel-GN_Level_Population_by_Five_Year_Age_Group.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "00_04": 104125,
    "05_09": 131919,
    "10_14": 156681,
    "15_19": 179866,
    "20_24": 200897,
    "25_29": 167913,
    "30_34": 158469,
    "35_39": 156173,
    "40_44": 174122,
    "45_49": 173231,
    "50_54": 163804,
    "55_59": 150861,
    "60_64": 136267,
    "65_69": 111267,
    "70_74": 90239,
    "75_79": 63864,
    "80_84": 34078,
    "85_89": 15003,
    "90_94": 5407,
    "95_and_above": 1229
}
```

**14,909** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), District (25), Dsd (340), Gnd (14,003)

#### Validation Errors

⚠️ **44** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 02. [Housing-Structure](data/Housing-Structure)

- [📄 JSON](data/Housing-Structure/data.json)
- [📄 TSV Table](data/Housing-Structure/data.tsv)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "single_house_single_storeyed": 355982,
    "single_house_two_storeyed": 185828,
    "single_house_more_than_two_storeyed": 24207,
    "attached_house_1st_floor": 27406,
    "attached_house_2nd_floor": 24275,
    "attached_house_from_3_to_4_floors": 16529,
    "attached_house_from_5_to_10_floors": 11907,
    "attached_house_from_11_to_19_floors": 5994,
    "attached_house_from_20_floors_or_more": 1756,
    "other": 167
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **15** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 03. [Housing-Walls](data/Housing-Walls)

- [📄 JSON](data/Housing-Walls/data.json)
- [📄 TSV Table](data/Housing-Walls/data.tsv)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "bricks": 166151,
    "cement_block": 462409,
    "granite_cube_stones": 2691,
    "cabook": 14988,
    "pressed_soil_bricks": 1597,
    "warichchi_mud": 675,
    "cadjan_palmyrah": 57,
    "planks_metal_sheets_asbestos": 5109,
    "zink_aluminium_sheets": 151,
    "other": 56,
    "not_relevant": 167
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **22** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 04. [Housing-Floor](data/Housing-Floor)

- [📄 JSON](data/Housing-Floor/data.json)
- [📄 TSV Table](data/Housing-Floor/data.tsv)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "cement": 284355,
    "terrazzo_tile_granite_wood_finished": 343281,
    "concrete": 24441,
    "mud": 839,
    "wood": 743,
    "sand": 155,
    "other": 70,
    "not_relevant": 167
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **16** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 05. [Housing-Roof](data/Housing-Roof)

- [📄 JSON](data/Housing-Roof/data.json)
- [📄 TSV Table](data/Housing-Roof/data.tsv)
- [📊 Source XLSX](original_docs/OHU_GN_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "tile": 40032,
    "asbestos": 475061,
    "concrete": 128212,
    "zink_aluminium_sheet": 4065,
    "metal_sheet": 3273,
    "cadjan_palmyrah_straw": 3109,
    "other": 132,
    "not_relevant": 167
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **16** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
