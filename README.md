# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_16:20:28-green)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 870476,
    "sex-male": 416078,
    "sex-female": 454398,
    "age-under-15": 171285,
    "age-15-to-59": 515832,
    "age-60-to-64": 51878,
    "age-65-and-over": 131481
}
```

**376** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (339)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 870476,
    "sinhalese": 736387,
    "sri_lanka_tamil": 40484,
    "indian_tamil_or_malaiyaga_thamilar": 21244,
    "sri_lanka_moor_or_muslim": 71794,
    "burgher": 179,
    "malay": 117,
    "sri_lanka_chetty": 9,
    "bharatha": 7,
    "veddhas": 5,
    "other": 250
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 870476,
    "buddhist": 728929,
    "hindu": 56199,
    "islam": 72616,
    "roman_catholic": 7292,
    "other_christian": 5387,
    "other": 53
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 242027,
    "single_house_single_storeyed": 201784,
    "single_house_two_storeyed": 30451,
    "single_house_more_than_two_storeyed": 1904,
    "attached_house_1st_floor": 6895,
    "attached_house_2nd_floor": 811,
    "attached_house_3rd_or_4th_floor": 156,
    "attached_house_5th_to_10th_floor": 0,
    "attached_house_11th_to_19th_floor": 0,
    "attached_house_from_20th_floor_or_more": 0,
    "other": 26
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 242027,
    "brick": 105322,
    "cement_block": 116372,
    "granite_or_cube_stones": 8490,
    "cabook": 1469,
    "pressed_soil_bricks": 5516,
    "mud_or_warichchi": 3244,
    "kadjan_or_palmyrah": 18,
    "plank_or_metal_sheet_or_asbestos": 1469,
    "zinc_aluminium_sheets": 37,
    "other": 64,
    "not_relevant": 26
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 242027,
    "tile": 76275,
    "asbestos": 131448,
    "concrete": 14232,
    "zinc_aluminium_sheets": 3432,
    "metal_sheets": 8259,
    "kadjan_or_palmyrah_or_straw": 8302,
    "other": 53,
    "not_relevant": 26
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 242027,
    "cement": 155123,
    "terrazzo_or_tile_or_granite_or_wood_or_titanium": 62656,
    "concrete": 19023,
    "mud": 4985,
    "wood": 79,
    "sand": 71,
    "other": 64,
    "not_relevant": 26
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 244037,
    "firewood": 177937,
    "kerosene": 373,
    "gas": 63345,
    "electricity": 467,
    "saw_dust_or_paddy_husk": 13,
    "bio_gas": 12,
    "other": 87,
    "not_relevant": 1803
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 244037,
    "ground_water-_protected_well": 99985,
    "ground_water-semi_protected_well": 15492,
    "ground_water-unprotected_well": 5364,
    "ground_water-tube_well": 1690,
    "ground_water-spring_or_fountain": 33702,
    "pipe_borne_water-national_water_supply_and_drainage_board": 57229,
    "pipe_borne_water-local_authority": 2253,
    "pipe_borne_water-community_based_organizations": 17589,
    "pipe_borne_water-private_water_supply_project": 7569,
    "other-tank_or_river_or_stream": 2780,
    "other-rain_water": 68,
    "other-bottled_water": 245,
    "other-filter_water": 15,
    "other-bowser": 6,
    "other-other": 50
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 244037,
    "electricity-from_national_grid_or_from_rural_hydro_power_project": 239635,
    "kerosene_lamp": 3651,
    "solar_power_grid_connected": 68,
    "solar_power_standalone": 174,
    "bio_gas": 3,
    "rural_water_supply_project": 28,
    "other": 478
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 244037,
    "within_the_unit-exclusively_for_the_household": 156414,
    "within_the_unit-sharing_with_another_household": 5429,
    "outside_the_unit-exclusively_for_the_household": 73283,
    "outside_the_unit-sharing_with_another_household": 5721,
    "other-no_toilet_but_sharing_with_another_household": 2877,
    "other-common_or_public_toilet": 74,
    "other-not_using_a_toilet": 239
}
```

**377** rows in total, by District (1), Country (1), Province (9), District (26), Dsd (340)

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
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 870476,
    "male": 416078,
    "female": 454398
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **12** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 02. [Population by Age Group](data/GN_population_excel/Population-by-Age-Group)

- [📄 JSON](data/GN_population_excel/Population-by-Age-Group/data.json)
- [📄 TSV Table](data/GN_population_excel/Population-by-Age-Group/data.tsv)
- [📊 Source XLSX](original_docs/GN_population_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "total": 870476,
    "age_0_14": 171285,
    "age_15_59": 515832,
    "age_60_64": 51878,
    "age_65_and_above": 131481
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **20** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 03. [Occupied Housing Units](data/GN_housing_excel/Occupied-Housing-Units)

- [📄 JSON](data/GN_housing_excel/Occupied-Housing-Units/data.json)
- [📄 TSV Table](data/GN_housing_excel/Occupied-Housing-Units/data.tsv)
- [📊 Source XLSX](original_docs/GN_housing_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "occupied_housing_units": 242027
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **4** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-9 (`LK-9`)
  - LK-9230 (`LK-9230`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 04. [Number of Households](data/HH_GND_excel/Number-of-Households)

- [📄 JSON](data/HH_GND_excel/Number-of-Households/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-Households/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "n_households": 244037
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **4** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-9 (`LK-9`)
  - LK-9230 (`LK-9230`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 05. [Number of households by main source of drinking water](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-main-source-of-drinking-water/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "protected_well": 99985,
    "semi_protected_well": 15492,
    "unprotected_well": 5364,
    "tube_well": 1690,
    "spring_fountain": 33702,
    "pipe_borne_nwsdb": 57229,
    "pipe_borne_local_authority": 2253,
    "pipe_borne_community": 17589,
    "pipe_borne_private": 7569,
    "tank_river_stream": 2780,
    "rain_water": 68,
    "bottled_water": 245,
    "filter_ro": 15,
    "bowser": 6,
    "other": 50
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **57** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 06. [Number of households by main source of energy/fuel used for cooking](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-main-source-of-energyfuel-used-for-cooking/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "firewood": 177937,
    "kerosene": 373,
    "gas": 63345,
    "electricity": 467,
    "sawdust_paddy_husk": 13,
    "bio_gas": 12,
    "other": 87,
    "not_relevant": 1803
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **31** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 07. [Number of households by source of lighting](data/HH_GND_excel/Number-of-households-by-source-of-lighting)

- [📄 JSON](data/HH_GND_excel/Number-of-households-by-source-of-lighting/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-by-source-of-lighting/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "electricity_grid": 239635,
    "kerosene_lamp": 3651,
    "solar_grid": 68,
    "solar_standalone": 174,
    "bio_gas": 3,
    "generator": 28,
    "other": 478
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **25** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

### 08. [Number of households using toilet facilities](data/HH_GND_excel/Number-of-households-using-toilet-facilities)

- [📄 JSON](data/HH_GND_excel/Number-of-households-using-toilet-facilities/data.json)
- [📄 TSV Table](data/HH_GND_excel/Number-of-households-using-toilet-facilities/data.tsv)
- [📊 Source XLSX](original_docs/HH_GND_excel.xlsx)

#### Example Data

```json
{
    "region_id": "EC-22",
    "region_name": "Kegalle",
    "region_name_in_data": null,
    "region_ent_type": "DISTRICT",
    "within_unit_exclusive": 156414,
    "within_unit_shared": 5429,
    "within_premises_exclusive": 73283,
    "within_premises_shared": 5721,
    "no_toilet_sharing": 2877,
    "common_public": 74,
    "none": 239
}
```

**14,462** rows in total, by District (27), Gnd (14,085), Country (1), Province (9), Dsd (340)

#### Validation Errors

⚠️ **28** aggregated values don't match sum of children
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)
  - LK-2 (`LK-2`)

⚠️ **39** GNDs in the reference gazetteer missing from this dataset (boundary differences)
  - Medapihilla (`LK-2209125`)
  - Kadawatha (`LK-2209130`)
  - Galporugolla (`LK-2209135`)

⚠️ **6** GND IDs in this dataset not found in the reference gazetteer (boundary differences)
  - EC-22I (`EC-22I`)
  - LG-92033 (`LG-92033`)
  - Kokuthoduvai South (`LK-4415095`)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
