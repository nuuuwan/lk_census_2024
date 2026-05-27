# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_16:31:08-green)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 2375415,
    "sex-male": 1154799,
    "sex-female": 1220616,
    "age-under-15": 392721,
    "age-15-to-59": 1525340,
    "age-60-to-64": 136268,
    "age-65-and-over": 321086
}
```

**396** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (339)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 2375415,
    "sinhalese": 1807945,
    "sri_lanka_tamil": 243856,
    "indian_tamil_or_malaiyaga_thamilar": 15427,
    "sri_lanka_moor_or_muslim": 285346,
    "burgher": 10643,
    "malay": 8249,
    "sri_lanka_chetty": 239,
    "bharatha": 560,
    "veddhas": 14,
    "other": 3136
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

#### Validation Errors

⚠️ **1** rows in data couldn't be matched to a known administrative entity
  - Kalmunai Tamil Division (`LK-52XX`)

⚠️ **1** known administrative entities have no corresponding row in data
  - Kalmunai (`LK-5224`)

⚠️ **3** rows where 'total' field doesn't equal sum of other fields
  - Jaffna (`EC-10`) — total: 731,461, sum of fields: 731,463
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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 2375415,
    "buddhist": 1682524,
    "hindu": 197759,
    "islam": 298422,
    "roman_catholic": 139882,
    "other_christian": 55624,
    "other": 1204
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 654051,
    "single_house_single_storeyed": 355982,
    "single_house_two_storeyed": 185828,
    "single_house_more_than_two_storeyed": 24207,
    "attached_house_1st_floor": 27406,
    "attached_house_2nd_floor": 24275,
    "attached_house_3rd_or_4th_floor": 16529,
    "attached_house_5th_to_10th_floor": 11907,
    "attached_house_11th_to_19th_floor": 5994,
    "attached_house_from_20th_floor_or_more": 1756,
    "other": 167
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 654051,
    "brick": 166151,
    "cement_block": 462409,
    "granite_or_cube_stones": 2691,
    "cabook": 14988,
    "pressed_soil_bricks": 1597,
    "mud_or_warichchi": 675,
    "kadjan_or_palmyrah": 57,
    "plank_or_metal_sheet_or_asbestos": 5109,
    "zinc_aluminium_sheets": 151,
    "other": 56,
    "not_relevant": 167
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 654051,
    "tile": 40032,
    "asbestos": 475061,
    "concrete": 128212,
    "zinc_aluminium_sheets": 4065,
    "metal_sheets": 3273,
    "kadjan_or_palmyrah_or_straw": 3109,
    "other": 132,
    "not_relevant": 167
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 654051,
    "cement": 284355,
    "terrazzo_or_tile_or_granite_or_wood_or_titanium": 343281,
    "concrete": 24441,
    "mud": 839,
    "wood": 743,
    "sand": 155,
    "other": 70,
    "not_relevant": 167
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 661822,
    "firewood": 65584,
    "kerosene": 9106,
    "gas": 566183,
    "electricity": 6425,
    "saw_dust_or_paddy_husk": 134,
    "bio_gas": 157,
    "other": 380,
    "not_relevant": 13853
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 661822,
    "ground_water-_protected_well": 78469,
    "ground_water-semi_protected_well": 3522,
    "ground_water-unprotected_well": 568,
    "ground_water-tube_well": 3649,
    "ground_water-spring_or_fountain": 1344,
    "pipe_borne_water-national_water_supply_and_drainage_board": 558425,
    "pipe_borne_water-local_authority": 3720,
    "pipe_borne_water-community_based_organizations": 9703,
    "pipe_borne_water-private_water_supply_project": 1278,
    "other-tank_or_river_or_stream": 124,
    "other-rain_water": 24,
    "other-bottled_water": 720,
    "other-filter_water": 55,
    "other-bowser": 22,
    "other-other": 199
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 661822,
    "electricity-from_national_grid_or_from_rural_hydro_power_project": 653295,
    "kerosene_lamp": 3366,
    "solar_power_grid_connected": 2900,
    "solar_power_standalone": 831,
    "bio_gas": 58,
    "rural_water_supply_project": 192,
    "other": 1180
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 661822,
    "within_the_unit-exclusively_for_the_household": 599062,
    "within_the_unit-sharing_with_another_household": 13455,
    "outside_the_unit-exclusively_for_the_household": 35126,
    "outside_the_unit-sharing_with_another_household": 7064,
    "other-no_toilet_but_sharing_with_another_household": 2390,
    "other-common_or_public_toilet": 4518,
    "other-not_using_a_toilet": 207
}
```

**397** rows in total, by District (22), Country (1), Province (9), District (25), Dsd (340)

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
    "region_id": "EC-01",
    "region_name": "Colombo",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 2375415,
    "male": 1154799,
    "female": 1220616
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **6** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
    "total": 2375415,
    "age_0_14": 392725,
    "age_15_59": 1525336,
    "age_60_64": 136267,
    "age_65_and_above": 321087
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **10** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
    "occupied_housing_units": 654051
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **2** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
    "n_households": 661822
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **2** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
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

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **30** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
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

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **16** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
    "electricity_grid": 653295,
    "kerosene_lamp": 3366,
    "solar_grid": 2900,
    "solar_standalone": 831,
    "bio_gas": 58,
    "generator": 192,
    "other": 1180
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **14** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

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
    "region_ent_type": "DISTRICT",
    "within_unit_exclusive": 599062,
    "within_unit_shared": 13455,
    "within_premises_exclusive": 35126,
    "within_premises_shared": 7064,
    "no_toilet_sharing": 2390,
    "common_public": 4518,
    "none": 207
}
```

**14,923** rows in total, by District (47), Gnd (14,526), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **14** aggregated values don't match sum of children
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)
  - LK-1 (`LK-1`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **522** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-01A (`EC-01A`)
  - EC-01B (`EC-01B`)
  - EC-01C (`EC-01C`)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
