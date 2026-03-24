# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_16:12:32-green)

## Original Source Documents

The following original documents have been downloaded from [https://www.statistics.gov.lk](https://www.statistics.gov.lk)

1. [Population_Preliminary_Report.pdf](Population_Preliminary_Report.pdf)
2. [Housing_Preliminary_Report.pdf](Housing_Preliminary_Report.pdf)
3. [CPH2024_Preliminary_Report.pdf](CPH2024_Preliminary_Report.pdf)

## Data Table (11)

The source documents have been parsed to extract the following datasets: 

### 01. [Population by sex and age](Population-Preliminary-Report/Population-by-sex-and-age)

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

**365** rows in total, by Country (1), District (25), Dsd (339)

### 02. [Population by ethnicity](Population-Preliminary-Report/Population-by-ethnicity)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 03. [Population by religion](Population-Preliminary-Report/Population-by-religion)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 04. [Number of housing units by housing unit structure](Housing-Preliminary-Report/Number-of-housing-units-by-housing-unit-structure)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 05. [Number of housing units by main material used for walls construction](Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-walls-construction)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 06. [Number of housing units by main material used for roof construction](Housing-Preliminary-Report/Number-of-housing-units-by-main-material-used-for-roof-construction)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 07. [Number of households by main material used for floor construction](Housing-Preliminary-Report/Number-of-households-by-main-material-used-for-floor-construction)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 08. [Number of households by main source of energy/fuel used](Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used)

- [📄 JSON](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used/data.json)
- [📄 TSV Table](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used/data.tsv)
- [📜 PDF-Table Only](data/Housing-Preliminary-Report/Number-of-households-by-main-source-of-energyfuel-used/table.pdf)
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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 09. [Number of households by main source of drinking water](Housing-Preliminary-Report/Number-of-households-by-main-source-of-drinking-water)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 10. [Number of households by source of lighting](Housing-Preliminary-Report/Number-of-households-by-source-of-lighting)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

### 11. [Number of households using toilet facilities](Housing-Preliminary-Report/Number-of-households-using-toilet-facilities)

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

**366** rows in total, by Country (1), District (25), Dsd (340)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
