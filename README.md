# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_16:23:34-green)

## Original Source Documents

The following original documents have been downloaded from [https://www.statistics.gov.lk](https://www.statistics.gov.lk)

1. [Population_Preliminary_Report.pdf](Population_Preliminary_Report.pdf)
2. [Housing_Preliminary_Report.pdf](Housing_Preliminary_Report.pdf)
3. [CPH2024_Preliminary_Report.pdf](CPH2024_Preliminary_Report.pdf)
4. [GN_population_excel.xlsx](GN_population_excel.xlsx)
5. [GN_housing_excel.xlsx](GN_housing_excel.xlsx)
6. [HH_GND_excel.xlsx](HH_GND_excel.xlsx)

## PDF Data Tables (11)

The following datasets have been extracted from the PDF source documents:

### 01. [Population by sex and age](data/Population-Preliminary-Report/Population-by-sex-and-age)

- [📄 JSON](data/Population-Preliminary-Report/Population-by-sex-and-age/data.json)
- [📄 TSV Table](data/Population-Preliminary-Report/Population-by-sex-and-age/data.tsv)
- [📜 PDF-Table Only](data/Population-Preliminary-Report/Population-by-sex-and-age/table.pdf)
- [📜 Original Source PDF](original_docs/Population_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 21781800,
    "sex-male": 10512344,
    "sex-female": 11269456,
    "age-under-15": 4506839,
    "age-15-to-59": 13353837,
    "age-60-to-64": 1183310,
    "age-65-and-over": 2737814
}
```

**374** rows in total, by Country (1), Province (9), District (25), Dsd (339)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **2** known administrative entities have no corresponding row in data
  - Welivitiya-Divitura (`LK-3130`)
  - Kalmunai (`LK-5224`)

### 02. [Population by ethnicity](data/Population-Preliminary-Report/Population-by-ethnicity)

- [📄 JSON](data/Population-Preliminary-Report/Population-by-ethnicity/data.json)
- [📄 TSV Table](data/Population-Preliminary-Report/Population-by-ethnicity/data.tsv)
- [📜 PDF-Table Only](data/Population-Preliminary-Report/Population-by-ethnicity/table.pdf)
- [📜 Original Source PDF](original_docs/Population_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 21781800,
    "sinhalese": 16144037,
    "sri_lanka_tamil": 2681627,
    "indian_tamil_or_malaiyaga_thamilar": 600360,
    "sri_lanka_moor_or_muslim": 2283246,
    "burgher": 31721,
    "malay": 26650,
    "sri_lanka_chetty": 2443,
    "bharatha": 1183,
    "veddhas": 1373,
    "other": 9160
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

⚠️ **2** rows where 'total' field doesn't equal sum of other fields
  - Northern (`LK-4`) — total: 1,150,148, sum of fields: 1,150,150
  - Kilinochchi (`LK-45`) — total: 136,710, sum of fields: 136,712

### 03. [Population by religion](data/Population-Preliminary-Report/Population-by-religion)

- [📄 JSON](data/Population-Preliminary-Report/Population-by-religion/data.json)
- [📄 TSV Table](data/Population-Preliminary-Report/Population-by-religion/data.tsv)
- [📜 PDF-Table Only](data/Population-Preliminary-Report/Population-by-religion/table.pdf)
- [📜 Original Source PDF](original_docs/Population_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 21781800,
    "buddhist": 15199093,
    "hindu": 2734839,
    "islam": 2337379,
    "roman_catholic": 1224348,
    "other_christian": 282185,
    "other": 3956
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 04. [Number of housing units by housing unit structure](data/Housing-Preliminary-Report/Number-of-housing-units-by-housing-unit-structure)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-housing-units-by-housing-unit-structure/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-housing-units-by-housing-unit-structure/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-housing-units-by-housing-unit-structure/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6030541,
    "single_house_single_storeyed": 4958009,
    "single_house_two_storeyed": 751375,
    "single_house_more_than_two_storeyed": 59484,
    "attached_house_1st_floor": 164419,
    "attached_house_2nd_floor": 50030,
    "attached_house_3rd_or_4th_floor": 25373,
    "attached_house_5th_to_10th_floor": 12853,
    "attached_house_11th_to_19th_floor": 6031,
    "attached_house_from_20th_floor_or_more": 1756,
    "other": 1211
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 05. [Number of housing units by main material used for walls construction](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-walls-construction)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-walls-construction/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-walls-construction/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-walls-construction/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6030541,
    "brick": 2799913,
    "cement_block": 2828027,
    "granite_or_cube_stones": 95717,
    "cabook": 68497,
    "pressed_soil_bricks": 111245,
    "mud_or_warichchi": 70011,
    "kadjan_or_palmyrah": 7650,
    "plank_or_metal_sheet_or_asbestos": 43260,
    "zinc_aluminium_sheets": 3870,
    "other": 1140,
    "not_relevant": 1211
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 06. [Number of housing units by main material used for roof construction](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-roof-construction)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-roof-construction/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-roof-construction/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-roof-construction/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6030541,
    "tile": 2032441,
    "asbestos": 3209496,
    "concrete": 440761,
    "zinc_aluminium_sheets": 85422,
    "metal_sheets": 163735,
    "kadjan_or_palmyrah_or_straw": 88820,
    "other": 8655,
    "not_relevant": 1211
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 07. [Number of households by main material used for floor construction](data/Housing-Preliminary-Report/Number-of-households-by-main-material-used-for-floor-construction)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-by-main-material-used-for-floor-construction/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-by-main-material-used-for-floor-construction/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-by-main-material-used-for-floor-construction/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6030541,
    "cement": 3710163,
    "terrazzo_or_tile_or_granite_or_wood_or_titanium": 1692659,
    "concrete": 498925,
    "mud": 115259,
    "wood": 2579,
    "sand": 7707,
    "other": 2038,
    "not_relevant": 1211
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 08. [Number of households by main source of energy/fuel used for cooking](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used-for-cooking)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "firewood": 3381781,
    "kerosene": 32974,
    "gas": 2588502,
    "electricity": 19540,
    "saw_dust_or_paddy_husk": 1739,
    "bio_gas": 7179,
    "other": 2361,
    "not_relevant": 77239
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 09. [Number of households by main source of drinking water](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-drinking-water)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-drinking-water/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-drinking-water/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-drinking-water/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "ground_water-_protected_well": 1624506,
    "ground_water-semi_protected_well": 267327,
    "ground_water-unprotected_well": 77806,
    "ground_water-tube_well": 270401,
    "ground_water-spring_or_fountain": 230268,
    "pipe_borne_water-national_water_supply_and_drainage_board": 2374349,
    "pipe_borne_water-local_authority": 100764,
    "pipe_borne_water-community_based_organizations": 419247,
    "pipe_borne_water-private_water_supply_project": 130394,
    "other-tank_or_river_or_stream": 59336,
    "other-rain_water": 4346,
    "other-bottled_water": 63753,
    "other-filter_water": 456849,
    "other-bowser": 31208,
    "other-other": 761
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 10. [Number of households by source of lighting](data/Housing-Preliminary-Report/Number-of-households-by-source-of-lighting)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-by-source-of-lighting/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-by-source-of-lighting/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-by-source-of-lighting/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "electricity-from_national_grid_or_from_rural_hydro_power_project": 5987585,
    "kerosene_lamp": 95150,
    "solar_power_grid_connected": 8093,
    "solar_power_standalone": 5817,
    "bio_gas": 244,
    "rural_water_supply_project": 1230,
    "other": 13196
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

### 11. [Number of households using toilet facilities](data/Housing-Preliminary-Report/Number-of-households-using-toilet-facilities)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-using-toilet-facilities/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-using-toilet-facilities/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-using-toilet-facilities/table.pdf)
- [📜 Original Source PDF](original_docs/Housing_Preliminary_Report.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "within_the_unit-exclusively_for_the_household": 3798777,
    "within_the_unit-sharing_with_another_household": 157456,
    "outside_the_unit-exclusively_for_the_household": 1832587,
    "outside_the_unit-sharing_with_another_household": 197678,
    "other-no_toilet_but_sharing_with_another_household": 101924,
    "other-common_or_public_toilet": 9567,
    "other-not_using_a_toilet": 13326
}
```

**375** rows in total, by Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

## XLSX Data Tables (8)

The following datasets have been extracted from the XLSX source documents:

### 01. [Population by Sex](data/GN_population_excel/Population-by-Sex)

- [📄 JSON](data/GN_population_excel/Population-by-Sex/data.json)
- [📄 TSV Table](data/GN_population_excel/Population-by-Sex/data.tsv)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "total": 21781800,
    "male": 10512344,
    "female": 11269456
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "total": 21781800,
    "age_0_14": 4506839,
    "age_15_59": 13353837,
    "age_60_64": 1183310,
    "age_65_and_above": 2737814
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "occupied_housing_units": 6030541
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "n_households": 6111315
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "protected_well": 1624506,
    "semi_protected_well": 267327,
    "unprotected_well": 77806,
    "tube_well": 270401,
    "spring_fountain": 230268,
    "pipe_borne_nwsdb": 2374349,
    "pipe_borne_local_authority": 100764,
    "pipe_borne_community": 419247,
    "pipe_borne_private": 130394,
    "tank_river_stream": 59336,
    "rain_water": 4346,
    "bottled_water": 63753,
    "filter_ro": 456849,
    "bowser": 31208,
    "other": 761
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "firewood": 3381781,
    "kerosene": 32974,
    "gas": 2588502,
    "electricity": 19540,
    "sawdust_paddy_husk": 1739,
    "bio_gas": 7179,
    "other": 2361,
    "not_relevant": 77239
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "electricity_grid": 5987585,
    "kerosene_lamp": 95150,
    "solar_grid": 8093,
    "solar_standalone": 5817,
    "bio_gas": 244,
    "generator": 1230,
    "other": 13196
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

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
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "COUNTRY",
    "within_unit_exclusive": 3798777,
    "within_unit_shared": 157456,
    "within_premises_exclusive": 1832587,
    "within_premises_shared": 197678,
    "no_toilet_sharing": 101924,
    "common_public": 9567,
    "none": 13326
}
```

**14,383** rows in total, by Country (1), Province (9), District (25), Dsd (340), Gnd (14,008)

#### Validation Errors

⚠️ **4** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - Kokuthoduvai South (`LK-4415095`)
  - Ellainagar (`LK-5115005`)
  - Eravur 04 (`LK-5115010`)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
