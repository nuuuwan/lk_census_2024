# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_15:09:48-green)

## XLSX Data Tables (15)

The following datasets have been extracted from the XLSX source documents:

### 01. [Population by Sex](data/GN_population_excel/Population-by-Sex)

- [📄 JSON](data/GN_population_excel/Population-by-Sex/data.json)
- [📄 TSV Table](data/GN_population_excel/Population-by-Sex/data.tsv)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "total": 2375415,
    "male": 1154799,
    "female": 1220616
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **6** aggregated values don't match sum of children
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

### 02. [Population by Age Group](data/GN_population_excel/Population-by-Age-Group)

- [📄 JSON](data/GN_population_excel/Population-by-Age-Group/data.json)
- [📄 TSV Table](data/GN_population_excel/Population-by-Age-Group/data.tsv)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "total": 2375415,
    "age_0_14": 392725,
    "age_15_59": 1525336,
    "age_60_64": 136267,
    "age_65_and_above": 321087
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **10** aggregated values don't match sum of children
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

### 03. [Occupied Housing Units](data/GN_housing_excel/Occupied-Housing-Units)

- [📄 JSON](data/GN_housing_excel/Occupied-Housing-Units/data.json)
- [📄 TSV Table](data/GN_housing_excel/Occupied-Housing-Units/data.tsv)
- [📊 Source XLSX](original_docs/GN_housing_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "occupied_housing_units": 654051
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **2** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 04. [Number of Households](data/HH_GND_excel/Number-of-Households)

- [📄 JSON](data/HH_GND_excel/Number-of-Households/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-Households/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "n_households": 661822
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **2** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

### 05. [Number of households by main source of drinking water](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "protected_well": 78469,
    "semi_protected_well": 3522,
    "unprotected_well": 568,
    "tube_well": 3649,
    "spring_fountain": 1344,
    "pipe_borne_nwsdb": 558425,
    "pipe_borne_local_authority": 3720,
    "pipe_borne_community": 9703,
    "pipe_borne_private": 1278,
    "tank_river_stream": 124,
    "rain_water": 24,
    "bottled_water": 720,
    "filter_ro": 55,
    "bowser": 22,
    "other": 199
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **30** aggregated values don't match sum of children
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

### 06. [Number of households by main source of energy/fuel used for cooking](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "firewood": 65584,
    "kerosene": 9106,
    "gas": 566183,
    "electricity": 6425,
    "sawdust_paddy_husk": 134,
    "bio_gas": 157,
    "other": 380,
    "not_relevant": 13853
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

### 07. [Number of households by source of lighting](data/HH_GND_excel/Number-of-households-by-source-of-lighting)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-source-of-lighting/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-source-of-lighting/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "electricity_grid": 653295,
    "kerosene_lamp": 3366,
    "solar_grid": 2900,
    "solar_standalone": 831,
    "bio_gas": 58,
    "generator": 192,
    "other": 1180
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **14** aggregated values don't match sum of children
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

### 08. [Number of households using toilet facilities](data/HH_GND_excel/Number-of-households-using-toilet-facilities)

- [📄 JSON](data/HH_GND_excel/Number-of-households-using-toilet-facilities/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-using-toilet-facilities/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "within_unit_exclusive": 599062,
    "within_unit_shared": 13455,
    "within_premises_exclusive": 35126,
    "within_premises_shared": 7064,
    "no_toilet_sharing": 2390,
    "common_public": 4518,
    "none": 207
}
```

**14,923** rows in total, by Ed (22), Pd (160), Lg (358), Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **14** aggregated values don't match sum of children
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

### 09. [Population by Ethnic Group](data/GN_Level_Population_by_Ethnic_Group/Population-by-Ethnic-Group)

- [📄 JSON](data/GN_Level_Population_by_Ethnic_Group/Population-by-Ethnic-Group/data.json)
- [📄 TSV Table](data/GN_Level_Population_by_Ethnic_Group/Population-by-Ethnic-Group/data.tsv)
- [📊 Source XLSX](original_docs/GN_Level_Population_by_Ethnic_Group.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "sinhalese": 1807945,
    "sri_lanka_tamil": 243613,
    "indian_malaiyaga_tamil": 14412,
    "sri_lanka_moor_muslim": 284667,
    "burgher": 9885,
    "malay": 7456,
    "sri_lanka_chetty": 49,
    "bharatha": 338,
    "veddha": 0
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

### 10. [Population by Religion Group](data/GN_Level_Population_by_Religion/Population-by-Religion-Group)

- [📄 JSON](data/GN_Level_Population_by_Religion/Population-by-Religion-Group/data.json)
- [📄 TSV Table](data/GN_Level_Population_by_Religion/Population-by-Religion-Group/data.tsv)
- [📊 Source XLSX](original_docs/GN_Level_Population_by_Religion.xlsx)

#### Example Data

```json
{
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "ED",
    "buddhist": 1682524,
    "hindu": 197524,
    "islam": 297852,
    "roman_catholic": 139690,
    "other_christian": 55217,
    "other": 2608
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

### 11. [Population by 5 year Age groups](data/GN_Level_Population_by_Five_Year_Age_Group/Population-by-5-year-Age-groups)

- [📄 JSON](data/GN_Level_Population_by_Five_Year_Age_Group/Population-by-5-year-Age-groups/data.json)
- [📄 TSV Table](data/GN_Level_Population_by_Five_Year_Age_Group/Population-by-5-year-Age-groups/data.tsv)
- [📊 Source XLSX](original_docs/GN_Level_Population_by_Five_Year_Age_Group.xlsx)

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

### 12. [Type of Housing unit Structure](data/OHU_GN_excel/Type-of-Housing-unit-Structure)

- [📄 JSON](data/OHU_GN_excel/Type-of-Housing-unit-Structure/data.json)
- [📄 TSV Table](data/OHU_GN_excel/Type-of-Housing-unit-Structure/data.tsv)
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

### 13. [Principal material of construction of the Walls](data/OHU_GN_excel/Principal-material-of-construction-of-the-Walls)

- [📄 JSON](data/OHU_GN_excel/Principal-material-of-construction-of-the-Walls/data.json)
- [📄 TSV Table](data/OHU_GN_excel/Principal-material-of-construction-of-the-Walls/data.tsv)
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

### 14. [Principal material of construction of the Floor](data/OHU_GN_excel/Principal-material-of-construction-of-the-Floor)

- [📄 JSON](data/OHU_GN_excel/Principal-material-of-construction-of-the-Floor/data.json)
- [📄 TSV Table](data/OHU_GN_excel/Principal-material-of-construction-of-the-Floor/data.tsv)
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

### 15. [Principal material of construction of the Roof](data/OHU_GN_excel/Principal-material-of-construction-of-the-Roof)

- [📄 JSON](data/OHU_GN_excel/Principal-material-of-construction-of-the-Roof/data.json)
- [📄 TSV Table](data/OHU_GN_excel/Principal-material-of-construction-of-the-Roof/data.tsv)
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
