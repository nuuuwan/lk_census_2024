# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--12_18:42:36-green)

## Original Source Documents

The following original documents have been downloaded from [https://www.statistics.gov.lk](https://www.statistics.gov.lk)

1. [Basic Population by Districts and Divisional Secretary Divisions](Basic-Population.pdf)
2. [Basic Housing Information by Districts and Divisional Secretary Divisions](Basic-Housing.pdf)
3. [Preliminary Report - Census of Population & Housing 2024](Preliminary-Report.pdf)

## Data Tables

The source documents have been parsed to extract the following datasets: 

### 01. [Population by sex, age and district according to DSD](Basic-Population/Population-by-sex-age-and-district-according-to-DSD)

- [📄 JSON](data/Basic-Population/Population-by-sex-age-and-district-according-to-DSD/data.json)
- [📄 TSV Table](data/Basic-Population/Population-by-sex-age-and-district-according-to-DSD/data.tsv)
- [📜 PDF-Table Only](data/Basic-Population/Population-by-sex-age-and-district-according-to-DSD/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Population.pdf)

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

### 02. [Population by ethnicity and district according to DSD](Basic-Population/Population-by-ethnicity-and-district-according-to-DSD)

- [📄 JSON](data/Basic-Population/Population-by-ethnicity-and-district-according-to-DSD/data.json)
- [📄 TSV Table](data/Basic-Population/Population-by-ethnicity-and-district-according-to-DSD/data.tsv)
- [📜 PDF-Table Only](data/Basic-Population/Population-by-ethnicity-and-district-according-to-DSD/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Population.pdf)

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

### 03. [Population by religion and district according to DSD](Basic-Population/Population-by-religion-and-district-according-to-DSD)

- [📄 JSON](data/Basic-Population/Population-by-religion-and-district-according-to-DSD/data.json)
- [📄 TSV Table](data/Basic-Population/Population-by-religion-and-district-according-to-DSD/data.tsv)
- [📜 PDF-Table Only](data/Basic-Population/Population-by-religion-and-district-according-to-DSD/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Population.pdf)

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

### 04. [Number of housing units by housing unit structure at district level and DSDs](Basic-Housing/Number-of-housing-units-by-housing-unit-structure-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-housing-units-by-housing-unit-structure-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-housing-units-by-housing-unit-structure-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-housing-units-by-housing-unit-structure-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6030541,
    "single_house_single_storeyed": 4958008,
    "single_house_two_storeyed": 751375,
    "single_house_more_than_two_storeyed": 59484,
    "attached_house_1st_floor": 164419,
    "attached_house_2nd_floor": 50030,
    "attached_house_3rd_or_4th_floor": 25373,
    "attached_house_5th_to_10th_floor": 12854,
    "attached_house_11th_to_19th_floor": 6031,
    "attached_house_from_20th_floor_or_more": 1756,
    "other": 1211
}
```

### 05. [Number of housing units by main material used for walls construction at district level and DSDs](Basic-Housing/Number-of-housing-units-by-main-material-used-for-walls-construction-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-walls-construction-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-walls-construction-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-walls-construction-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

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

### 06. [Number of housing units by main material used for roof construction at district level and DSDs](Basic-Housing/Number-of-housing-units-by-main-material-used-for-roof-construction-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-roof-construction-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-roof-construction-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-housing-units-by-main-material-used-for-roof-construction-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

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
    "metal_sheets": 150713,
    "kadjan_or_palmyrah_or_straw": 101842,
    "other": 8655,
    "not_relevant": 1211
}
```

### 07. [Number of households by main material used for floor construction at district level and DSDs](Basic-Housing/Number-of-households-by-main-material-used-for-floor-construction-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-households-by-main-material-used-for-floor-construction-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-households-by-main-material-used-for-floor-construction-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-households-by-main-material-used-for-floor-construction-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

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

### 08. [Number of households by main source of drinking water at district level and DSDs](Basic-Housing/Number-of-households-by-main-source-of-drinking-water-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-households-by-main-source-of-drinking-water-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-households-by-main-source-of-drinking-water-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-households-by-main-source-of-drinking-water-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

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

### 09. [Number of households by source of lighting at district level and DSDs](Basic-Housing/Number-of-households-by-source-of-lighting-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-households-by-source-of-lighting-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-households-by-source-of-lighting-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-households-by-source-of-lighting-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "electricity-from_national_grid": 5952365,
    "electricity-from_rural_hydro_power_project": 35220,
    "other-kerosene_lamp": 95150,
    "other-solar_power_grid_connected": 8093,
    "other-solar_power_standalone": 5817,
    "other-bio_gas": 244,
    "other-generator": 1230,
    "other-other": 13196
}
```

### 10. [Number of households using toilet facilities at district level and DSDs](Basic-Housing/Number-of-households-using-toilet-facilities-at-district-level-and-DSDs)

- [📄 JSON](data/Basic-Housing/Number-of-households-using-toilet-facilities-at-district-level-and-DSDs/data.json)
- [📄 TSV Table](data/Basic-Housing/Number-of-households-using-toilet-facilities-at-district-level-and-DSDs/data.tsv)
- [📜 PDF-Table Only](data/Basic-Housing/Number-of-households-using-toilet-facilities-at-district-level-and-DSDs/table.pdf)
- [📜 Original Source PDF](original_docs/Basic-Housing.pdf)

#### Example Data

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_name_in_data": "Sri Lanka",
    "region_ent_type": "country",
    "total": 6111315,
    "within_the_unit-exclusively_for_the_household": 3798777,
    "within_the_unit-sharing_with_another_household": 157346,
    "outside_the_unit-exclusively_for_the_household": 1832587,
    "outside_the_unit-sharing_with_another_household": 197678,
    "other-no_toilet_but_sharing_with_another_household": 101924,
    "other-common_or_public_toilet": 9677,
    "other-not_using_a_toilet": 13326
}
```

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
