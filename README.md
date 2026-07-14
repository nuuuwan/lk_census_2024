# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_12:04:23-green)

**154** Datasets on Population, Housing and more, by Country, Province, District, Divisional Secretariat Division (DSD), Grama Niladhari Division (GND), Electoral District (ED), Polling Division (PD), and Local Government Authority (LG) levels.

## 01. [Population-Gender](data/Population-Gender)

### Data by Country & Province

| region_id | region_name | total_value | male | female |
| --: | --: | --: | --: | --:|
| LK | Sri Lanka | 21,781,800 | 10,512,344 | 11,269,456 |
| LK-1 | Western | 6,117,341 | 2,961,374 | 3,155,967 |
| LK-2 | Central | 2,714,045 | 1,298,405 | 1,415,640 |
| LK-3 | Southern | 2,606,679 | 1,258,830 | 1,347,849 |
| LK-4 | Northern | 1,150,148 | 551,273 | 598,875 |
| LK-5 | Eastern | 1,783,214 | 850,607 | 932,607 |
| LK-6 | North Western | 2,586,972 | 1,243,316 | 1,343,656 |
| LK-7 | North Central | 1,407,610 | 686,257 | 721,353 |
| LK-8 | Uva | 1,399,892 | 683,745 | 716,147 |
| LK-9 | Sabaragamuwa | 2,015,899 | 978,537 | 1,037,362 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "male": 10512344,
        "female": 11269456
    },
    "total_value": 21781800
}
```

### Data Files

- [📄 data/Population-Gender/data.json (3.3 MB)](data/Population-Gender/data.json)
- [📕 data/Population-Gender/data.tsv (629.5 kB)](data/Population-Gender/data.tsv)
- [📊 original_docs/GN_population_excel.xlsx (1.5 MB)](original_docs/GN_population_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GN_population_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GN_population_excel)


## 02. [Population-Ethnicity](data/Population-Ethnicity)

### Data by Country & Province

| region_id | region_name | total_value | sinhalese | sri_lanka_tamil | indian_malaiyaga_tamil | sri_lanka_moor_muslim | burgher | malay | sri_lanka_chetty | bharatha | veddha | other |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 21,781,800 | 16,140,688 | 2,665,574 | 590,087 | 2,274,372 | 25,159 | 22,838 | 1,753 | 553 | 1,287 | 59,489 |
| LK-1 | Western | 6,117,341 | 5,115,543 | 379,680 | 26,271 | 542,333 | 15,725 | 16,126 | 1,753 | 553 | 0 | 19,357 |
| LK-2 | Central | 2,714,045 | 1,783,899 | 222,924 | 406,956 | 289,281 | 2,395 | 952 | 0 | 0 | 0 | 7,638 |
| LK-3 | Southern | 2,606,679 | 2,470,423 | 27,994 | 10,187 | 88,145 | 127 | 3,882 | 0 | 0 | 0 | 5,921 |
| LK-4 | Northern | 1,150,148 | 34,023 | 1,052,660 | 2,726 | 57,151 | 25 | 0 | 0 | 0 | 0 | 3,563 |
| LK-5 | Eastern | 1,783,214 | 390,538 | 677,890 | 1,221 | 703,155 | 4,503 | 367 | 0 | 0 | 898 | 4,642 |
| LK-6 | North Western | 2,586,972 | 2,193,622 | 67,272 | 1,689 | 314,035 | 1,519 | 931 | 0 | 0 | 0 | 7,904 |
| LK-7 | North Central | 1,407,610 | 1,272,757 | 11,147 | 173 | 119,657 | 57 | 56 | 0 | 0 | 221 | 3,542 |
| LK-8 | Uva | 1,399,892 | 1,139,983 | 95,535 | 96,469 | 63,685 | 548 | 499 | 0 | 0 | 168 | 3,005 |
| LK-9 | Sabaragamuwa | 2,015,899 | 1,739,900 | 130,472 | 44,395 | 96,930 | 260 | 25 | 0 | 0 | 0 | 3,917 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "sinhalese": 16140688,
        "sri_lanka_tamil": 2665574,
        "indian_malaiyaga_tamil": 590087,
        "sri_lanka_moor_muslim": 2274372,
        "burgher": 25159,
        "malay": 22838,
        "sri_lanka_chetty": 1753,
        "bharatha": 553,
        "veddha": 1287,
        "other": 59489
    },
    "total_value": 21781800
}
```

### Data Files

- [📄 data/Population-Ethnicity/data.json (6.4 MB)](data/Population-Ethnicity/data.json)
- [📕 data/Population-Ethnicity/data.tsv (863.4 kB)](data/Population-Ethnicity/data.tsv)
- [📊 original_docs/GNLevel-GN_Level_Population_by_Ethnic_Group.xlsx (6.8 MB)](original_docs/GNLevel-GN_Level_Population_by_Ethnic_Group.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Ethnic_Group](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Ethnic_Group)


## 03. [Population-Religion](data/Population-Religion)

### Data by Country & Province

| region_id | region_name | total_value | buddhist | hindu | islam | roman_catholic | other_christian | other |
| --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 21,781,800 | 15,196,960 | 2,718,154 | 2,327,605 | 1,209,072 | 266,515 | 63,494 |
| LK-1 | Western | 6,117,341 | 4,507,601 | 305,971 | 568,301 | 616,413 | 104,869 | 14,186 |
| LK-2 | Central | 2,714,045 | 1,760,853 | 565,722 | 296,754 | 55,680 | 26,421 | 8,615 |
| LK-3 | Southern | 2,606,679 | 2,463,066 | 28,775 | 92,985 | 5,093 | 7,568 | 9,192 |
| LK-4 | Northern | 1,150,148 | 32,374 | 829,092 | 59,860 | 175,462 | 49,827 | 3,533 |
| LK-5 | Eastern | 1,783,214 | 388,164 | 596,842 | 706,572 | 46,596 | 41,109 | 3,931 |
| LK-6 | North Western | 2,586,972 | 1,918,652 | 43,060 | 318,870 | 278,850 | 17,211 | 10,329 |
| LK-7 | North Central | 1,407,610 | 1,262,247 | 9,588 | 120,511 | 6,869 | 3,663 | 4,732 |
| LK-8 | Uva | 1,399,892 | 1,135,408 | 180,305 | 65,203 | 9,852 | 5,431 | 3,693 |
| LK-9 | Sabaragamuwa | 2,015,899 | 1,728,595 | 158,799 | 98,549 | 14,257 | 10,416 | 5,283 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "buddhist": 15196960,
        "hindu": 2718154,
        "islam": 2327605,
        "roman_catholic": 1209072,
        "other_christian": 266515,
        "other": 63494
    },
    "total_value": 21781800
}
```

### Data Files

- [📄 data/Population-Religion/data.json (4.7 MB)](data/Population-Religion/data.json)
- [📕 data/Population-Religion/data.tsv (753.6 kB)](data/Population-Religion/data.tsv)
- [📊 original_docs/GNLevel-GN_Level_Population_by_Religion.xlsx (1.0 MB)](original_docs/GNLevel-GN_Level_Population_by_Religion.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Religion](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Religion)


## 04. [Population-AgeGroup](data/Population-AgeGroup)

### Data by Country & Province

| region_id | region_name | total_value | 00_04 | 05_09 | 10_14 | 15_19 | 20_24 | 25_29 | 30_34 | 35_39 | 40_44 | 45_49 | 50_54 | 55_59 | 60_64 | 65_69 | 70_74 | 75_79 | 80_84 | 85_89 | 90_94 | 95_and_above |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 21,781,800 | 1,215,120 | 1,556,523 | 1,735,196 | 1,795,038 | 1,608,606 | 1,372,458 | 1,414,060 | 1,452,703 | 1,602,344 | 1,490,765 | 1,341,807 | 1,276,056 | 1,183,310 | 991,814 | 795,539 | 522,990 | 268,415 | 111,029 | 39,235 | 8,792 |
| LK-1 | Western | 6,117,341 | 287,116 | 369,976 | 428,367 | 475,748 | 486,242 | 411,892 | 396,532 | 403,369 | 458,173 | 445,763 | 412,374 | 380,280 | 343,391 | 285,239 | 231,712 | 162,489 | 85,998 | 36,613 | 13,076 | 2,991 |
| LK-2 | Central | 2,714,045 | 154,205 | 204,497 | 235,152 | 229,457 | 192,660 | 154,026 | 162,232 | 173,222 | 192,876 | 179,495 | 161,999 | 163,045 | 155,726 | 130,207 | 102,224 | 68,790 | 34,734 | 13,854 | 4,609 | 1,035 |
| LK-3 | Southern | 2,606,679 | 142,793 | 190,768 | 209,476 | 215,333 | 178,596 | 152,631 | 164,052 | 174,519 | 187,572 | 170,305 | 158,824 | 151,599 | 143,734 | 127,415 | 103,385 | 70,188 | 38,224 | 18,201 | 7,295 | 1,769 |
| LK-4 | Northern | 1,150,148 | 73,293 | 79,675 | 90,800 | 96,680 | 98,803 | 88,553 | 83,444 | 77,294 | 81,599 | 73,899 | 60,386 | 54,470 | 54,236 | 47,215 | 41,357 | 27,932 | 13,342 | 5,195 | 1,675 | 300 |
| LK-5 | Eastern | 1,783,214 | 137,014 | 157,548 | 157,400 | 169,326 | 146,886 | 126,629 | 127,105 | 116,811 | 124,535 | 110,400 | 95,671 | 89,532 | 79,012 | 59,664 | 43,627 | 24,716 | 11,701 | 4,151 | 1,227 | 259 |
| LK-6 | North Western | 2,586,972 | 148,254 | 191,642 | 210,926 | 214,171 | 176,527 | 152,409 | 161,533 | 173,373 | 192,544 | 179,687 | 158,485 | 153,502 | 144,739 | 122,896 | 99,957 | 60,025 | 30,313 | 11,271 | 3,866 | 852 |
| LK-7 | North Central | 1,407,610 | 83,713 | 112,655 | 125,152 | 117,867 | 97,492 | 82,682 | 93,829 | 97,166 | 108,645 | 101,145 | 88,419 | 79,891 | 72,924 | 58,945 | 44,684 | 24,831 | 11,129 | 4,626 | 1,503 | 312 |
| LK-8 | Uva | 1,399,892 | 83,349 | 109,270 | 119,643 | 114,780 | 96,666 | 86,593 | 96,137 | 99,529 | 102,117 | 92,838 | 82,728 | 81,850 | 76,369 | 61,507 | 45,617 | 28,239 | 14,326 | 5,882 | 2,014 | 438 |
| LK-9 | Sabaragamuwa | 2,015,899 | 105,383 | 140,492 | 158,280 | 161,676 | 134,734 | 117,043 | 129,196 | 137,420 | 154,283 | 137,233 | 122,921 | 121,887 | 113,179 | 98,726 | 82,976 | 55,780 | 28,648 | 11,236 | 3,970 | 836 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "00_04": 1215120,
        "05_09": 1556523,
        "10_14": 1735196,
        "15_19": 1795038,
        "20_24": 1608606,
        "25_29": 1372458,
        "30_34": 1414060,
        "35_39": 1452703,
        "40_44": 1602344,
        "45_49": 1490765,
        "50_54": 1341807,
        "55_59": 1276056,
        "60_64": 1183310,
        "65_69": 991814,
        "70_74": 795539,
        "75_79": 522990,
        "80_84": 268415,
        "85_89": 111029,
        "90_94": 39235,
        "95_and_above": 8792
    },
    "total_value": 21781800
}
```

### Data Files

- [📄 data/Population-AgeGroup/data.json (8.5 MB)](data/Population-AgeGroup/data.json)
- [📕 data/Population-AgeGroup/data.tsv (1.5 MB)](data/Population-AgeGroup/data.tsv)
- [📊 original_docs/GNLevel-GN_Level_Population_by_Five_Year_Age_Group.xlsx (2.1 MB)](original_docs/GNLevel-GN_Level_Population_by_Five_Year_Age_Group.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Five_Year_Age_Group](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/GNLevel/GN_Level_Population_by_Five_Year_Age_Group)


## 05. [Housing-Structure](data/Housing-Structure)

### Data by Country & Province

| region_id | region_name | total_value | single_house_single_storeyed | single_house_two_storeyed | single_house_more_than_two_storeyed | attached_house_1st_floor | attached_house_2nd_floor | attached_house_from_3_to_4_floors | attached_house_from_5_to_10_floors | attached_house_from_11_to_19_floors | attached_house_from_20_floors_or_more | other |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,030,541 | 4,958,009 | 751,375 | 59,484 | 164,419 | 50,030 | 25,373 | 12,853 | 6,031 | 1,756 | 1,211 |
| LK-1 | Western | 1,686,506 | 1,177,294 | 360,332 | 32,722 | 44,627 | 32,464 | 18,775 | 12,272 | 5,994 | 1,756 | 270 |
| LK-2 | Central | 730,925 | 539,831 | 95,235 | 11,754 | 70,508 | 9,149 | 3,866 | 469 | 23 | 0 | 90 |
| LK-3 | Southern | 722,971 | 615,514 | 91,046 | 5,317 | 6,959 | 3,271 | 748 | 60 | 14 | 0 | 42 |
| LK-4 | Northern | 307,459 | 292,371 | 13,396 | 604 | 466 | 325 | 109 | 5 | 0 | 0 | 183 |
| LK-5 | Eastern | 489,362 | 452,172 | 32,702 | 1,365 | 1,432 | 774 | 491 | 8 | 0 | 0 | 418 |
| LK-6 | North Western | 738,403 | 681,543 | 52,350 | 1,295 | 2,143 | 785 | 139 | 38 | 0 | 0 | 110 |
| LK-7 | North Central | 397,890 | 373,745 | 22,469 | 559 | 581 | 393 | 117 | 1 | 0 | 0 | 25 |
| LK-8 | Uva | 390,145 | 337,782 | 27,180 | 2,355 | 20,632 | 1,384 | 781 | 0 | 0 | 0 | 31 |
| LK-9 | Sabaragamuwa | 566,880 | 487,757 | 56,665 | 3,513 | 17,071 | 1,485 | 347 | 0 | 0 | 0 | 42 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "single_house_single_storeyed": 4958009,
        "single_house_two_storeyed": 751375,
        "single_house_more_than_two_storeyed": 59484,
        "attached_house_1st_floor": 164419,
        "attached_house_2nd_floor": 50030,
        "attached_house_from_3_to_4_floors": 25373,
        "attached_house_from_5_to_10_floors": 12853,
        "attached_house_from_11_to_19_floors": 6031,
        "attached_house_from_20_floors_or_more": 1756,
        "other": 1211
    },
    "total_value": 6030541
}
```

### Data Files

- [📄 data/Housing-Structure/data.json (8.9 MB)](data/Housing-Structure/data.json)
- [📕 data/Housing-Structure/data.tsv (846.3 kB)](data/Housing-Structure/data.tsv)
- [📊 original_docs/OHU_GN_excel.xlsx (3.4 MB)](original_docs/OHU_GN_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel)


## 06. [Housing-Walls](data/Housing-Walls)

### Data by Country & Province

| region_id | region_name | total_value | bricks | cement_block | granite_cube_stones | cabook | pressed_soil_bricks | warichchi_mud | cadjan_palmyrah | planks_metal_sheets_asbestos | zink_aluminium_sheets | other | not_relevant |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,030,541 | 2,799,913 | 2,828,027 | 95,717 | 68,497 | 111,245 | 70,011 | 7,650 | 43,260 | 3,870 | 1,140 | 1,211 |
| LK-1 | Western | 1,686,506 | 444,198 | 1,147,193 | 8,468 | 48,401 | 15,695 | 9,478 | 122 | 12,045 | 407 | 229 | 270 |
| LK-2 | Central | 730,925 | 282,854 | 363,613 | 49,021 | 1,925 | 21,108 | 8,484 | 35 | 3,318 | 332 | 145 | 90 |
| LK-3 | Southern | 722,971 | 365,930 | 313,267 | 4,658 | 10,786 | 14,814 | 9,670 | 41 | 3,546 | 111 | 106 | 42 |
| LK-4 | Northern | 307,459 | 17,403 | 280,072 | 516 | 147 | 1,122 | 1,376 | 1,569 | 4,395 | 642 | 34 | 183 |
| LK-5 | Eastern | 489,362 | 361,634 | 108,255 | 482 | 217 | 1,475 | 4,504 | 2,306 | 8,428 | 1,599 | 44 | 418 |
| LK-6 | North Western | 738,403 | 595,052 | 118,669 | 725 | 365 | 5,526 | 7,102 | 3,440 | 6,863 | 437 | 114 | 110 |
| LK-7 | North Central | 397,890 | 335,859 | 53,722 | 238 | 108 | 1,936 | 5,107 | 57 | 667 | 123 | 48 | 25 |
| LK-8 | Uva | 390,145 | 215,064 | 114,216 | 11,494 | 2,313 | 36,894 | 8,617 | 38 | 1,089 | 135 | 254 | 31 |
| LK-9 | Sabaragamuwa | 566,880 | 181,919 | 329,020 | 20,115 | 4,235 | 12,675 | 15,673 | 42 | 2,909 | 84 | 166 | 42 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "bricks": 2799913,
        "cement_block": 2828027,
        "granite_cube_stones": 95717,
        "cabook": 68497,
        "pressed_soil_bricks": 111245,
        "warichchi_mud": 70011,
        "cadjan_palmyrah": 7650,
        "planks_metal_sheets_asbestos": 43260,
        "zink_aluminium_sheets": 3870,
        "other": 1140,
        "not_relevant": 1211
    },
    "total_value": 6030541
}
```

### Data Files

- [📄 data/Housing-Walls/data.json (7.2 MB)](data/Housing-Walls/data.json)
- [📕 data/Housing-Walls/data.tsv (885.4 kB)](data/Housing-Walls/data.tsv)
- [📊 original_docs/OHU_GN_excel.xlsx (3.4 MB)](original_docs/OHU_GN_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel)


## 07. [Housing-Floor](data/Housing-Floor)

### Data by Country & Province

| region_id | region_name | total_value | cement | terrazzo_tile_granite_wood_finished | concrete | mud | wood | sand | other | not_relevant |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,030,541 | 3,710,163 | 1,692,659 | 498,925 | 115,259 | 2,579 | 7,707 | 2,038 | 1,211 |
| LK-1 | Western | 1,686,506 | 836,713 | 754,097 | 87,793 | 5,688 | 1,159 | 578 | 208 | 270 |
| LK-2 | Central | 730,925 | 486,204 | 160,536 | 58,877 | 24,089 | 361 | 385 | 383 | 90 |
| LK-3 | Southern | 722,971 | 408,910 | 236,461 | 66,411 | 10,752 | 190 | 109 | 96 | 42 |
| LK-4 | Northern | 307,459 | 250,340 | 43,976 | 7,171 | 4,107 | 114 | 1,039 | 529 | 183 |
| LK-5 | Eastern | 489,362 | 392,963 | 54,405 | 30,161 | 7,006 | 93 | 3,989 | 327 | 418 |
| LK-6 | North Western | 738,403 | 466,494 | 173,106 | 85,119 | 11,929 | 304 | 1,117 | 224 | 110 |
| LK-7 | North Central | 397,890 | 249,106 | 69,140 | 68,233 | 11,145 | 46 | 138 | 57 | 25 |
| LK-8 | Uva | 390,145 | 249,488 | 68,548 | 47,422 | 24,260 | 132 | 176 | 88 | 31 |
| LK-9 | Sabaragamuwa | 566,880 | 369,945 | 132,390 | 47,738 | 16,283 | 180 | 176 | 126 | 42 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "cement": 3710163,
        "terrazzo_tile_granite_wood_finished": 1692659,
        "concrete": 498925,
        "mud": 115259,
        "wood": 2579,
        "sand": 7707,
        "other": 2038,
        "not_relevant": 1211
    },
    "total_value": 6030541
}
```

### Data Files

- [📄 data/Housing-Floor/data.json (5.5 MB)](data/Housing-Floor/data.json)
- [📕 data/Housing-Floor/data.tsv (802.5 kB)](data/Housing-Floor/data.tsv)
- [📊 original_docs/OHU_GN_excel.xlsx (3.4 MB)](original_docs/OHU_GN_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel)


## 08. [Housing-Roof](data/Housing-Roof)

### Data by Country & Province

| region_id | region_name | total_value | tile | asbestos | concrete | zink_aluminium_sheet | metal_sheet | cadjan_palmyrah_straw | other | not_relevant |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,030,541 | 2,032,441 | 3,209,496 | 440,761 | 85,422 | 163,735 | 88,820 | 8,655 | 1,211 |
| LK-1 | Western | 1,686,506 | 363,704 | 1,098,621 | 190,819 | 10,224 | 12,480 | 10,085 | 303 | 270 |
| LK-2 | Central | 730,925 | 66,210 | 471,886 | 83,423 | 34,464 | 53,758 | 20,521 | 573 | 90 |
| LK-3 | Southern | 722,971 | 311,194 | 365,468 | 31,230 | 2,162 | 7,330 | 5,322 | 223 | 42 |
| LK-4 | Northern | 307,459 | 182,198 | 100,468 | 7,101 | 6,190 | 5,841 | 3,731 | 1,747 | 183 |
| LK-5 | Eastern | 489,362 | 285,586 | 121,898 | 54,518 | 7,358 | 7,875 | 8,896 | 2,813 | 418 |
| LK-6 | North Western | 738,403 | 487,945 | 192,946 | 18,700 | 9,457 | 14,211 | 12,523 | 2,511 | 110 |
| LK-7 | North Central | 397,890 | 96,127 | 280,591 | 9,748 | 2,902 | 4,495 | 3,826 | 176 | 25 |
| LK-8 | Uva | 390,145 | 90,405 | 232,820 | 18,874 | 7,033 | 36,734 | 4,085 | 163 | 31 |
| LK-9 | Sabaragamuwa | 566,880 | 149,072 | 344,798 | 26,348 | 5,632 | 21,011 | 19,831 | 146 | 42 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "tile": 2032441,
        "asbestos": 3209496,
        "concrete": 440761,
        "zink_aluminium_sheet": 85422,
        "metal_sheet": 163735,
        "cadjan_palmyrah_straw": 88820,
        "other": 8655,
        "not_relevant": 1211
    },
    "total_value": 6030541
}
```

### Data Files

- [📄 data/Housing-Roof/data.json (5.7 MB)](data/Housing-Roof/data.json)
- [📕 data/Housing-Roof/data.tsv (805.1 kB)](data/Housing-Roof/data.tsv)
- [📊 original_docs/OHU_GN_excel.xlsx (3.4 MB)](original_docs/OHU_GN_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/OHU_GN_excel)


## 09. [Housing-Water](data/Housing-Water)

### Data by Country & Province

| region_id | region_name | total_value | protected_well | semi_protected_well | unprotected_well | tube_well | spring_fountain | pipe_borne_nwsdb | pipe_borne_local_authority | pipe_borne_community | pipe_borne_private | tank_river_stream | rain_water | bottled_water | filter_ro | bowser | other |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,111,315 | 1,624,506 | 267,327 | 77,806 | 270,401 | 230,268 | 2,374,349 | 100,764 | 419,247 | 130,394 | 59,336 | 4,346 | 63,753 | 456,849 | 31,208 | 761 |
| LK-1 | Western | 1,703,420 | 547,468 | 47,227 | 9,979 | 45,657 | 5,123 | 983,503 | 9,099 | 39,974 | 9,811 | 1,849 | 114 | 3,140 | 128 | 95 | 253 |
| LK-2 | Central | 749,019 | 91,497 | 21,372 | 9,024 | 16,174 | 96,127 | 299,310 | 44,481 | 92,552 | 39,614 | 24,126 | 382 | 1,576 | 11,453 | 1,199 | 132 |
| LK-3 | Southern | 728,288 | 239,865 | 47,351 | 15,823 | 6,870 | 12,729 | 315,660 | 6,322 | 48,336 | 15,673 | 6,369 | 134 | 4,677 | 7,877 | 545 | 57 |
| LK-4 | Northern | 312,002 | 103,270 | 30,918 | 7,908 | 81,540 | 193 | 36,032 | 6,082 | 3,896 | 1,886 | 514 | 439 | 5,387 | 26,012 | 7,862 | 63 |
| LK-5 | Eastern | 499,217 | 83,224 | 14,057 | 4,964 | 50,650 | 734 | 319,708 | 2,697 | 9,774 | 771 | 585 | 80 | 736 | 9,859 | 1,278 | 100 |
| LK-6 | North Western | 745,193 | 281,852 | 58,067 | 12,442 | 53,483 | 4,291 | 63,057 | 5,932 | 37,229 | 11,245 | 954 | 1,816 | 38,618 | 157,245 | 18,926 | 36 |
| LK-7 | North Central | 402,469 | 27,167 | 3,488 | 1,125 | 3,067 | 5,351 | 91,184 | 7,187 | 24,505 | 3,245 | 532 | 745 | 7,785 | 226,167 | 906 | 15 |
| LK-8 | Uva | 400,025 | 68,602 | 14,099 | 5,774 | 6,877 | 40,628 | 140,265 | 10,265 | 70,074 | 14,065 | 9,990 | 492 | 865 | 17,645 | 364 | 20 |
| LK-9 | Sabaragamuwa | 571,682 | 181,561 | 30,748 | 10,767 | 6,083 | 65,092 | 125,630 | 8,699 | 92,907 | 34,084 | 14,417 | 144 | 969 | 463 | 33 | 85 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
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
    },
    "total_value": 6111315
}
```

### Data Files

- [📄 data/Housing-Water/data.json (8.9 MB)](data/Housing-Water/data.json)
- [📕 data/Housing-Water/data.tsv (1.0 MB)](data/Housing-Water/data.tsv)
- [📊 original_docs/HH_GND_excel.xlsx (3.7 MB)](original_docs/HH_GND_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel)


## 10. [Housing-Cooking-Fuel](data/Housing-Cooking-Fuel)

### Data by Country & Province

| region_id | region_name | total_value | firewood | kerosene | gas | electricity | sawdust_paddy_husk | bio_gas | other | not_relevant |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,111,315 | 3,381,781 | 32,974 | 2,588,502 | 19,540 | 1,739 | 7,179 | 2,361 | 77,239 |
| LK-1 | Western | 1,703,420 | 433,777 | 15,637 | 1,203,412 | 10,508 | 303 | 356 | 1,152 | 38,275 |
| LK-2 | Central | 749,019 | 489,749 | 2,717 | 249,179 | 2,191 | 84 | 559 | 175 | 4,365 |
| LK-3 | Southern | 728,288 | 438,164 | 1,173 | 277,959 | 1,226 | 89 | 82 | 304 | 9,291 |
| LK-4 | Northern | 312,002 | 186,993 | 2,879 | 117,444 | 422 | 95 | 1,814 | 40 | 2,315 |
| LK-5 | Eastern | 499,217 | 232,633 | 5,032 | 251,630 | 1,291 | 1,007 | 3,557 | 111 | 3,956 |
| LK-6 | North Western | 745,193 | 534,964 | 2,782 | 195,933 | 1,394 | 35 | 570 | 272 | 9,243 |
| LK-7 | North Central | 402,469 | 304,792 | 737 | 92,753 | 560 | 12 | 186 | 103 | 3,326 |
| LK-8 | Uva | 400,025 | 327,040 | 957 | 68,808 | 988 | 82 | 32 | 50 | 2,068 |
| LK-9 | Sabaragamuwa | 571,682 | 433,669 | 1,060 | 131,384 | 960 | 32 | 23 | 154 | 4,400 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "firewood": 3381781,
        "kerosene": 32974,
        "gas": 2588502,
        "electricity": 19540,
        "sawdust_paddy_husk": 1739,
        "bio_gas": 7179,
        "other": 2361,
        "not_relevant": 77239
    },
    "total_value": 6111315
}
```

### Data Files

- [📄 data/Housing-Cooking-Fuel/data.json (5.4 MB)](data/Housing-Cooking-Fuel/data.json)
- [📕 data/Housing-Cooking-Fuel/data.tsv (789.0 kB)](data/Housing-Cooking-Fuel/data.tsv)
- [📊 original_docs/HH_GND_excel.xlsx (3.7 MB)](original_docs/HH_GND_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel)


## 11. [Housing-Lighting](data/Housing-Lighting)

### Data by Country & Province

| region_id | region_name | total_value | electricity_grid | kerosene_lamp | solar_grid | solar_standalone | bio_gas | generator | other |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,111,315 | 5,987,585 | 95,150 | 8,093 | 5,817 | 244 | 1,230 | 13,196 |
| LK-1 | Western | 1,703,420 | 1,682,433 | 10,565 | 5,206 | 1,514 | 121 | 288 | 3,293 |
| LK-2 | Central | 749,019 | 736,755 | 9,880 | 360 | 495 | 27 | 127 | 1,375 |
| LK-3 | Southern | 728,288 | 717,303 | 7,272 | 705 | 496 | 11 | 76 | 2,425 |
| LK-4 | Northern | 312,002 | 301,963 | 8,902 | 284 | 294 | 12 | 156 | 391 |
| LK-5 | Eastern | 499,217 | 479,020 | 18,042 | 393 | 213 | 17 | 102 | 1,430 |
| LK-6 | North Western | 745,193 | 729,060 | 13,132 | 553 | 1,252 | 28 | 164 | 1,004 |
| LK-7 | North Central | 402,469 | 392,571 | 8,494 | 206 | 440 | 12 | 31 | 715 |
| LK-8 | Uva | 400,025 | 389,582 | 8,556 | 183 | 571 | 8 | 93 | 1,032 |
| LK-9 | Sabaragamuwa | 571,682 | 558,898 | 10,307 | 203 | 542 | 8 | 193 | 1,531 |

### Example Data Row (JSON)

```json
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
}
```

### Data Files

- [📄 data/Housing-Lighting/data.json (5.2 MB)](data/Housing-Lighting/data.json)
- [📕 data/Housing-Lighting/data.tsv (740.1 kB)](data/Housing-Lighting/data.tsv)
- [📊 original_docs/HH_GND_excel.xlsx (3.7 MB)](original_docs/HH_GND_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel)


## 12. [Housing-Toilet](data/Housing-Toilet)

### Data by Country & Province

| region_id | region_name | total_value | within_unit_exclusive | within_unit_shared | within_premises_exclusive | within_premises_shared | no_toilet_sharing | common_public | none |
| --: | --: | --: | --: | --: | --: | --: | --: | --: | --:|
| LK | Sri Lanka | 6,111,315 | 3,798,777 | 157,456 | 1,832,587 | 197,678 | 101,924 | 9,567 | 13,326 |
| LK-1 | Western | 1,703,420 | 1,402,581 | 39,527 | 206,499 | 37,544 | 11,147 | 5,440 | 682 |
| LK-2 | Central | 749,019 | 458,565 | 26,474 | 219,652 | 28,760 | 12,295 | 1,882 | 1,391 |
| LK-3 | Southern | 728,288 | 415,171 | 13,432 | 265,541 | 21,117 | 12,060 | 375 | 592 |
| LK-4 | Northern | 312,002 | 132,194 | 7,133 | 155,196 | 7,486 | 8,163 | 214 | 1,616 |
| LK-5 | Eastern | 499,217 | 286,398 | 14,745 | 156,914 | 16,916 | 19,498 | 258 | 4,488 |
| LK-6 | North Western | 745,193 | 407,961 | 17,499 | 277,976 | 27,876 | 11,301 | 624 | 1,956 |
| LK-7 | North Central | 402,469 | 193,979 | 10,318 | 170,120 | 18,899 | 7,869 | 135 | 1,149 |
| LK-8 | Uva | 400,025 | 177,500 | 14,094 | 177,759 | 20,475 | 9,071 | 245 | 881 |
| LK-9 | Sabaragamuwa | 571,682 | 324,428 | 14,234 | 202,930 | 18,605 | 10,520 | 394 | 571 |

### Example Data Row (JSON)

```json
{
    "region_id": "LK",
    "region_name": "Sri Lanka",
    "region_ent_type": "country",
    "values": {
        "within_unit_exclusive": 3798777,
        "within_unit_shared": 157456,
        "within_premises_exclusive": 1832587,
        "within_premises_shared": 197678,
        "no_toilet_sharing": 101924,
        "common_public": 9567,
        "none": 13326
    },
    "total_value": 6111315
}
```

### Data Files

- [📄 data/Housing-Toilet/data.json (5.9 MB)](data/Housing-Toilet/data.json)
- [📕 data/Housing-Toilet/data.tsv (772.5 kB)](data/Housing-Toilet/data.tsv)
- [📊 original_docs/HH_GND_excel.xlsx (3.7 MB)](original_docs/HH_GND_excel.xlsx)

### Source

- 🌐: [https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel](https://www.statistics.gov.lk/Population/StaticalInformation/CPH2024/HH_GND_excel)


## `Final Report Build Status`

| status | status_label | n |
| :-- | :-- | --: |
| 2 | 🔴 Raw data is difficult to parse | 21 |
| 4 | 🟡 Lanka data is missing | 113 |
| 5 | ✅ All Stages Complete | 8 |

## 13. [Officers who have  Assigned for Census of Population and Housing 2024 Activities](data/final-report-tables/chapter-1/1.1.1-Officers-who-have--Assigned-for-Census-of-Population-and-Housing-2024-Activities)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 1618 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=23",
        "source_description": [
            "Table 1.1.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "CensusOfficers": "Officers who have Assigned for Census of Population and Housing 2024 Activities"
        },
        "when": "2024",
        "where_types": [
            "ed",
            "district",
            "country",
            "province"
        ]
    },
    "CensusOfficers": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "EnumeratorsWhoUsedSmartPhonesByoad": 1986,
                    "EnumeratorsWhoUsedTabletComputersCapi": 1104,
                    "TechnicalStaffCircleOfficers": 98,
                    "OtherNonTechnicalStaff": 70,
                    "TechnicalStaffAreaSupervisors": 53,
                    "TechnicalStaffZonalSupervisorsAndDistrictStatisticalBranchHead": 18,
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=23> (Table 1.1.1)

## 14. [The Questions and Topics Included in the Censuses of Sri Lanka 1871 - 2024](data/final-report-tables/chapter-1/1.1.2-The-Questions-and-Topics-Included-in-the-Censuses-of-Sri-Lanka-1871---2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Topic | Is Census 1871 | Is Census 1881 | Is Census 1891 | Is Census 1901 | Is Census 1911 | Is Census 1921 | Is Census 1931 | Is Census 1946 | Is Census 1953 | Is Census 1963 | Is Census 1971 | Is Census 1981 | Is Census 2001 | Is Census 2012 | Is Census 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| schedule | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False |
| Demographic and Personal Information | False | False | False | False | False | False | False | False | False | False | False | False | False | False | False |
| Name | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| Relationship to head of the household | True | True | True | False | False | False | False | True | True | True | True | True | True | True | True |
| Sex | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| Date of birth | False | False | False | False | False | False | False | False | False | True | True | True | True | True | True |
| Age | True | True | True | True | True | True | True | True | True | True | True | True | False | False | False |
| Marital Status | True | False | False | True | True | True | True | True | False | True | True | True | True | True | True |
| Ethnic group | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| Religion | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |

### Example Data Row (JSON)

```json
{
    "Topic": "schedule",
    "Is Census 1871": false,
    "Is Census 1881": false,
    "Is Census 1891": false,
    "Is Census 1901": false,
    "Is Census 1911": false,
    "Is Census 1921": false,
    "Is Census 1931": false,
    "Is Census 1946": false,
    "Is Census 1953": false,
    "Is Census 1963": false,
    "Is Census 1971": false,
    "Is Census 1981": false,
    "Is Census 2001": false,
    "Is Census 2012": false,
    "Is Census 2024": false
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=31> (Table 1.1.2)

## 15. [Evolution of the Number of Administrative Districts In Sri Lanka from 1871 to 2024](data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 27 rows)

| Region Id | Region Name | Region Ent Type | Is In 1871 | Is In 1881 | Is In 1891 | Is In 1901 | Is In 1911 | Is In 1921 | Is In 1931 | Is In 1946 | Is In 1953 | Is In 1963 | Is In 1971 | Is In 1981 | Is In 2001 | Is In 2012 | Is In 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-12-Negombo | Negombo | district | False | True | True | False | False | False | False | False | False | False | False | False | False | False | False |
| LK-12 | Gampaha | district | False | False | False | False | False | False | False | False | False | False | False | True | True | True | True |
| LK-13 | Kalutara | district | False | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-21 | Kandy | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-22 | Matale | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-23 | Nuwara Eliya | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-81 | Badulla | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-31 | Galle | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |
| LK-32 | Matara | district | True | True | True | True | True | True | True | True | True | True | True | True | True | True | True |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Is In 1871": true,
    "Is In 1881": true,
    "Is In 1891": true,
    "Is In 1901": true,
    "Is In 1911": true,
    "Is In 1921": true,
    "Is In 1931": true,
    "Is In 1946": true,
    "Is In 1953": true,
    "Is In 1963": true,
    "Is In 1971": true,
    "Is In 1981": true,
    "Is In 2001": true,
    "Is In 2012": true,
    "Is In 2024": true
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=60> (Table 2.1)

## 16. [Administrative Structure by District, 1981](data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 1142 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=62",
        "source_description": [
            "Table 2.2, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "AdministrativeStructure": "Administrative Structure by District, 1981"
        },
        "when": "1981",
        "where_types": [
            "province",
            "country",
            "district",
            "ed"
        ]
    },
    "AdministrativeStructure": {
        "1981": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "GramaSevakaDivisions": 121,
                    "AssistantGovernmentAgendDivisions": 8,
                    "TownCouncils": 6,
                    "UrbanCouncils": 4,
                    "MunicipalCouncils": 2
                },
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=62> (Table 2.2)

## 17. [Administrative Structure by District, 2012](data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 1162 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=63",
        "source_description": [
            "Table 2.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "AdministrativeStructure": "Administrative Structure by District, 2012"
        },
        "when": "2012",
        "where_types": [
            "ed",
            "province",
            "country",
            "district"
        ]
    },
    "AdministrativeStructure": {
        "2012": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "GramaSevakaDivisions": 557,
                    "AssistantGovernmentAgendDivisions": 13,
                    "MunicipalCouncils": 5,
                    "UrbanCouncils": 5,
                    "TownCouncils": 3
                },
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=63> (Table 2.3)

## 18. [Administrative Structure by District, 2024](data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District,-2024)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 1162 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=64",
        "source_description": [
            "Table 2.4, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "AdministrativeStructure": "Administrative Structure by District, 2024"
        },
        "when": "2024",
        "where_types": [
            "province",
            "district",
            "country",
            "ed"
        ]
    },
    "AdministrativeStructure": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "GramaSevakaDivisions": 557,
                    "AssistantGovernmentAgendDivisions": 13,
                    "MunicipalCouncils": 5,
                    "UrbanCouncils": 5,
                    "TownCouncils": 3
                },
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=64> (Table 2.4)

## 19. [Total Population, Intercensal Increase and Average Annual Growth Rate by Census Year, 1871 - 2024](data/final-report-tables/chapter-3/3.1-Total-Population,-Intercensal-Increase-and-Average-Annual-Growth-Rate-by-Census-Year,-1871---2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 16 rows)

| Census Data | Total Population | Total Value |
| :-- | :-- | :-- |
| 27 March 1871 | 2400380 | 2400380 |
| 17 February 1881 | 2759738 | 2759738 |
| 26 February 1891 | 3007789 | 3007789 |
| 01 March 1901 | 3565954 | 3565954 |
| 10 March 1911 | 4106350 | 4106350 |
| 18 March 1921 | 4498605 | 4498605 |
| 26 February 1931 | 5306871 | 5306871 |
| 19 March 1946 | 6657339 | 6657339 |
| 20 March 1953 | 8097895 | 8097895 |
| 08 July 1963 | 10582064 | 10582064 |

### Example Data Row (JSON)

```json
{
    "Census Data": "27 March 1871",
    "Total Population": 2400380,
    "Total Value": 2400380
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=67> (Table 3.1)

## 20. [Distribution of Population by Province and District, 2024](data/final-report-tables/chapter-3/3.2-Distribution-of-Population-by-Province-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Population |
| :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2375415 |
| LK-12 | Gampaha | district | 2436142 |
| LK-13 | Kalutara | district | 1305784 |
| LK-21 | Kandy | district | 1461895 |
| LK-22 | Matale | district | 526870 |
| LK-23 | Nuwara Eliya | district | 725280 |
| LK-31 | Galle | district | 1097372 |
| LK-32 | Matara | district | 837889 |
| LK-33 | Hambantota | district | 671418 |
| LK-41 | Jaffna | district | 594751 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population": 2375415
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=68> (Table 3.2)

## 21. [Population and Average Annual Growth Rate by District, Census Years 1981- 2024](data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District,-Census-Years-1981--2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Population 1981 | Population 2001 | Population 2012 | Population 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 1675847 | 2239696 | 2324349 | 2375415 |
| LK-12 | Gampaha | district | 1367813 | 2060470 | 2304833 | 2436142 |
| LK-13 | Kalutara | district | 823964 | 1065635 | 1221948 | 1305784 |
| LK-21 | Kandy | district | 1032335 | 1276202 | 1375382 | 1461895 |
| LK-22 | Matale | district | 352860 | 439031 | 484531 | 526870 |
| LK-23 | Nuwara Eliya | district | 583716 | 702689 | 711644 | 725280 |
| LK-31 | Galle | district | 805403 | 989769 | 1063334 | 1097372 |
| LK-32 | Matara | district | 642235 | 760990 | 814048 | 837889 |
| LK-33 | Hambantota | district | 421277 | 525913 | 599903 | 671418 |
| LK-41 | Jaffna | district | 734474 | 0 | 583882 | 594751 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population 1981": 1675847,
    "Population 2001": 2239696,
    "Population 2012": 2324349,
    "Population 2024": 2375415
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=69> (Table 3.3)

## 22. [Population Density by District, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-3/3.4-Population-Density-by-District,-1981,-2001,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 27 rows)

| Region Id | Region Name | Region Ent Type | Population Density 1981 | Population Density 2001 | Population Density 2012 | Population Density 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2605 | 3330 | 3438 | 3551 |
| LK-12 | Gampaha | district | 994 | 1539 | 1719 | 1776 |
| LK-13 | Kalutara | district | 516 | 677 | 775 | 805 |
| LK-21 | Kandy | district | 554 | 667 | 717 | 780 |
| LK-31 | Galle | district | 487 | 613 | 658 | 695 |
| LK-32 | Matara | district | 516 | 600 | 641 | 648 |
| LK-41 | Jaffna | district | 401 | 0 | 629 | 631 |
| LK-92 | Kegalle | district | 412 | 466 | 499 | 530 |
| LK-23 | Nuwara Eliya | district | 354 | 412 | 417 | 427 |
| LK-61 | Kurunegala | district | 254 | 316 | 350 | 380 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population Density 1981": 2605,
    "Population Density 2001": 3330,
    "Population Density 2012": 3438,
    "Population Density 2024": 3551
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=70> (Table 3.4)

## 23. [Distribution of Population by Sector, 2012 and 2024](data/final-report-tables/chapter-3/3.5-Distribution-of-Population-by-Sector,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Population 2012 | Population 2024 |
| :-- | :-- | :-- |
|  | 2012 | 2024 |
| Sri Lanka | 20359439 | 21781800 |
| Urban* | 3704470 | 3819203 |
| Rural | 15753322 | 17096918 |
| Estate Rural** | 901647 | 865679 |

### Example Data Row (JSON)

```json
{
    "Sector": "",
    "Population 2012": 2012,
    "Population 2024": 2024
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=71> (Table 3.5)

## 24. [Population Distribution by District and Sector, 2024](data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Population Urban | Population Estate Urban | Population Rural | Population Estate Rural | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 1773222 | 3874 | 593669 | 4650 | 2375415 |
| LK-12 | Gampaha | district | 350441 | 0 | 2085307 | 394 | 2436142 |
| LK-13 | Kalutara | district | 149939 | 864 | 1120942 | 34039 | 1305784 |
| LK-21 | Kandy | district | 171416 | 241 | 1208607 | 81631 | 1461895 |
| LK-22 | Matale | district | 62848 | 0 | 447122 | 16900 | 526870 |
| LK-23 | Nuwara Eliya | district | 36649 | 5666 | 308357 | 374608 | 725280 |
| LK-31 | Galle | district | 135514 | 0 | 944811 | 17047 | 1097372 |
| LK-32 | Matara | district | 98886 | 0 | 721903 | 17100 | 837889 |
| LK-33 | Hambantota | district | 33918 | 0 | 637442 | 58 | 671418 |
| LK-41 | Jaffna | district | 113821 | 0 | 480930 | 0 | 594751 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population Urban": 1773222,
    "Population Estate Urban": 3874,
    "Population Rural": 593669,
    "Population Estate Rural": 4650,
    "Total Value": 2375415
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=72> (Table 3.6)

## 25. [Lifetime Migrants by District of Dirth and District of Usual Residence,](data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence,)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 419 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=82",
        "source_description": [
            "Table 5.1.1, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "MigrantsLifetime": "Lifetime Migrants by District of Dirth and District of Usual Residence,"
        },
        "when": "2024",
        "where_types": [
            "district"
        ]
    },
    "MigrantsLifetime": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "PopulationLocal": 1876288,
                    "PopulationMigrant": 491236,
                    "PopulationForeign": 7345
                },
                "total_value": 2374869,
                "pct_values": {
                    "PopulationLocal": 0.7901,
                    "PopulationMigrant": 0.2068,
                    "PopulationForeign": 0.0031
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=82> (Table 5.1.1)

## 26. [In, Out and Net Lifetime Migrants by District, 2024](data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | In Migrants | Out Migrants |
| :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 491236 | 299712 |
| LK-12 | Gampaha | district | 490861 | 133333 |
| LK-13 | Kalutara | district | 180877 | 118645 |
| LK-21 | Kandy | district | 157921 | 282795 |
| LK-22 | Matale | district | 78262 | 100663 |
| LK-23 | Nuwara Eliya | district | 52570 | 163618 |
| LK-31 | Galle | district | 88038 | 180517 |
| LK-32 | Matara | district | 82457 | 201297 |
| LK-33 | Hambantota | district | 64982 | 103658 |
| LK-41 | Jaffna | district | 26104 | 79449 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "In Migrants": 491236,
    "Out Migrants": 299712
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=84> (Table 5.1.2)

## 27. [Largest Migration Flows of Lifetime Migrants by District of Usual Residence, 2024](data/final-report-tables/chapter-5/5.1.3-Largest-Migration-Flows-of-Lifetime-Migrants-by-District-of-Usual-Residence,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Lifetime In Migrants | 1St Largest Stream Migration District Name | P 1St Largest Stream Migration District | 2Nd Largest Stream Migration District Name | P 2Nd Largest Stream Migration District | 3Rd Largest Stream Migration District Name | P 3Rd Largest Stream Migration District |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 491236 | Matara | 0.109 | Galle | 0.102 | Kandy | 0.099 |
| LK-12 | Gampaha | district | 490861 | Colombo | 0.234 | Kurunegala | 0.097 | Kandy | 0.084 |
| LK-13 | Kalutara | district | 180877 | Colombo | 0.336 | Galle | 0.149 | Ratnapura | 0.094 |
| LK-21 | Kandy | district | 157921 | Nuwara Eliya | 0.172 | Matale | 0.115 | Kegalle | 0.094 |
| LK-22 | Matale | district | 78262 | Kandy | 0.334 | Kurunegala | 0.121 | Anuradhapura | 0.103 |
| LK-23 | Nuwara Eliya | district | 52570 | Kandy | 0.361 | Badulla | 0.175 | Kegalle | 0.065 |
| LK-31 | Galle | district | 88038 | Matara | 0.292 | Kalutara | 0.13 | Colombo | 0.122 |
| LK-32 | Matara | district | 82457 | Hambantota | 0.252 | Galle | 0.234 | Colombo | 0.102 |
| LK-33 | Hambantota | district | 64982 | Matara | 0.383 | Ratnapura | 0.12 | Galle | 0.098 |
| LK-41 | Jaffna | district | 26104 | Kilinochchi | 0.22 | Mullaitivu | 0.17 | Vavuniya | 0.086 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Lifetime In Migrants": 491236,
    "1St Largest Stream Migration District Name": "Matara",
    "P 1St Largest Stream Migration District": 0.109,
    "2Nd Largest Stream Migration District Name": "Galle",
    "P 2Nd Largest Stream Migration District": 0.102,
    "3Rd Largest Stream Migration District Name": "Kandy",
    "P 3Rd Largest Stream Migration District": 0.099
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=86> (Table 5.1.3)

## 28. [Largest Migration Flows of Lifetime Migrants who have Migrated Out of their District of Birth, 2024](data/final-report-tables/chapter-5/5.1.4-Largest-Migration-Flows-of-Lifetime-Migrants-who-have-Migrated-Out-of-their-District-of-Birth,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Lifetime In Migrants | 1St Largest Stream Migration District Name | P 1St Largest Stream Migration District | 2Nd Largest Stream Migration District Name | P 2Nd Largest Stream Migration District | 3Rd Largest Stream Migration District Name | P 3Rd Largest Stream Migration District |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 299712 | Gampaha | 0.383 | Kalutara | 0.203 | Kurunegala | 0.049 |
| LK-12 | Gampaha | district | 133333 | Colombo | 0.257 | Kurunegala | 0.181 | Puttalam | 0.112 |
| LK-13 | Kalutara | district | 118645 | Colombo | 0.359 | Gampaha | 0.159 | Galle | 0.096 |
| LK-21 | Kandy | district | 282795 | Colombo | 0.172 | Gampaha | 0.146 | Matale | 0.093 |
| LK-22 | Matale | district | 100663 | Kandy | 0.181 | Anuradhapura | 0.157 | Gampaha | 0.125 |
| LK-23 | Nuwara Eliya | district | 163618 | Colombo | 0.214 | Gampaha | 0.173 | Kandy | 0.166 |
| LK-31 | Galle | district | 180517 | Colombo | 0.278 | Gampaha | 0.156 | Kalutara | 0.15 |
| LK-32 | Matara | district | 201297 | Colombo | 0.266 | Gampaha | 0.145 | Galle | 0.128 |
| LK-33 | Hambantota | district | 103658 | Matara | 0.201 | Colombo | 0.179 | Moneragala | 0.14 |
| LK-41 | Jaffna | district | 79449 | Colombo | 0.205 | Kilinochchi | 0.203 | Vavuniya | 0.2 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Lifetime In Migrants": 299712,
    "1St Largest Stream Migration District Name": "Gampaha",
    "P 1St Largest Stream Migration District": 0.383,
    "2Nd Largest Stream Migration District Name": "Kalutara",
    "P 2Nd Largest Stream Migration District": 0.203,
    "3Rd Largest Stream Migration District Name": "Kurunegala",
    "P 3Rd Largest Stream Migration District": 0.049
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=87> (Table 5.1.4)

## 29. [In-migration, Out-migration, and Net Migration by District,](data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | In Migrants | Out Migrants |
| :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 519379 | 384245 |
| LK-12 | Gampaha | district | 524737 | 155712 |
| LK-13 | Kalutara | district | 192833 | 126566 |
| LK-21 | Kandy | district | 172489 | 287823 |
| LK-22 | Matale | district | 82805 | 105145 |
| LK-23 | Nuwara Eliya | district | 60934 | 169381 |
| LK-31 | Galle | district | 95154 | 183490 |
| LK-32 | Matara | district | 95958 | 202894 |
| LK-33 | Hambantota | district | 69567 | 107848 |
| LK-41 | Jaffna | district | 29253 | 76684 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "In Migrants": 519379,
    "Out Migrants": 384245
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=89> (Table 5.1.5)

## 30. [In-migrants by District of Usual Residence and Duration of Residence, 2024](data/final-report-tables/chapter-5/5.1.6-In-migrants-by-District-of-Usual-Residence-and-Duration-of-Residence,-2024)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 934 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=90",
        "source_description": [
            "Table 5.1.6, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "MigrantsResidenceDuration": "In-migrants by District of Usual Residence and Duration of Residence, 2024"
        },
        "when": "2024",
        "where_types": [
            "province",
            "district",
            "country",
            "ed"
        ]
    },
    "MigrantsResidenceDuration": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "10OrMoreYears": 305038,
                    "0004Years": 149236,
                    "0409Years": 65105
                },
                "total_value": 519379,
                "pct_values": {
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=90> (Table 5.1.6)

## 31. [Reasons for Migration from District of Previous Residence to District of Usual Residence, 2024](data/final-report-tables/chapter-5/5.1.7-Reasons-for-Migration-from-District-of-Previous-Residence-to-District-of-Usual-Residence,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Total Value | P Marriage | P Employment Searching For Job | P Education | P Accompanied A Family Member | P Returning For Permanent Residence | P Development Projects | P Resettled After Displacement | P A Disaster A Displaced Happened In The Prior Place | P Other |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 519379.999 | 0.255 | 0.378 | 0.118 | 0.174 | 0.054 | 0.001 | 0.001 | 0.004 | 0.014 |
| LK-12 | Gampaha | district | 524737.9990000001 | 0.349 | 0.261 | 0.043 | 0.19 | 0.128 | 0.002 | 0.002 | 0.006 | 0.018 |
| LK-13 | Kalutara | district | 192834.0 | 0.43 | 0.113 | 0.034 | 0.173 | 0.197 | 0.001 | 0.005 | 0.011 | 0.036 |
| LK-21 | Kandy | district | 172489.999 | 0.505 | 0.097 | 0.107 | 0.157 | 0.104 | 0.001 | 0.002 | 0.005 | 0.021 |
| LK-22 | Matale | district | 82805.99900000001 | 0.573 | 0.086 | 0.031 | 0.162 | 0.11 | 0.005 | 0.005 | 0.009 | 0.018 |
| LK-23 | Nuwara Eliya | district | 60935.0 | 0.596 | 0.102 | 0.035 | 0.167 | 0.056 | 0.005 | 0.013 | 0.014 | 0.012 |
| LK-31 | Galle | district | 95154.999 | 0.572 | 0.103 | 0.058 | 0.138 | 0.088 | 0.0 | 0.002 | 0.005 | 0.033 |
| LK-32 | Matara | district | 95959.0 | 0.548 | 0.069 | 0.089 | 0.123 | 0.141 | 0.0 | 0.002 | 0.006 | 0.022 |
| LK-33 | Hambantota | district | 69568.00099999999 | 0.616 | 0.074 | 0.023 | 0.126 | 0.099 | 0.009 | 0.003 | 0.008 | 0.043 |
| LK-41 | Jaffna | district | 29253.999 | 0.119 | 0.107 | 0.201 | 0.129 | 0.214 | 0.0 | 0.21 | 0.006 | 0.013 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total Value": 519379.999,
    "P Marriage": 0.255,
    "P Employment Searching For Job": 0.378,
    "P Education": 0.118,
    "P Accompanied A Family Member": 0.174,
    "P Returning For Permanent Residence": 0.054,
    "P Development Projects": 0.001,
    "P Resettled After Displacement": 0.001,
    "P A Disaster A Displaced Happened In The Prior Place": 0.004,
    "P Other": 0.014
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=91> (Table 5.1.7)

## 32. [Distribution of the Usually Resident Population of a District by their Permanent Residence, 2024](data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 369 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=94",
        "source_description": [
            "Table 5.1.8, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "ResidenceDistrictOrOtherDistrict": "Distribution of the Usually Resident Population of a District by their Permanent Residence, 2024"
        },
        "when": "2024",
        "where_types": [
            "district"
        ]
    },
    "ResidenceDistrictOrOtherDistrict": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "InDistrict": 2244323,
                    "InOtherDistrict": 130546
                },
                "total_value": 2374869,
                "pct_values": {
                    "InDistrict": 0.945,
                    "InOtherDistrict": 0.055
                }
            },
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=94> (Table 5.1.8)

## 33. [Population Temporarily Living Abroad by District and Sex, 2024](data/final-report-tables/chapter-5/5.2.1-Population-Temporarily-Living-Abroad-by-District-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Male | Female | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 43531 | 27908 | 71439 |
| LK-12 | Gampaha | district | 54734 | 31343 | 86077 |
| LK-13 | Kalutara | district | 25238 | 16114 | 41352 |
| LK-21 | Kandy | district | 35518 | 21712 | 57230 |
| LK-22 | Matale | district | 10682 | 9382 | 20064 |
| LK-23 | Nuwara Eliya | district | 6158 | 10755 | 16913 |
| LK-31 | Galle | district | 25283 | 15061 | 40344 |
| LK-32 | Matara | district | 14822 | 6498 | 21320 |
| LK-33 | Hambantota | district | 9432 | 4799 | 14231 |
| LK-41 | Jaffna | district | 8091 | 1334 | 9425 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Male": 43531,
    "Female": 27908,
    "Total Value": 71439
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=95> (Table 5.2.1)

## 34. [Population Temporarily Living Abroad by Sector, Sex and Age Group, 2024](data/final-report-tables/chapter-5/5.2.2-Population-Temporarily-Living-Abroad-by-Sector,-Sex-and-Age-Group,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Census of Population and Housing  - 2024 | -- | -- | -- | -- | -- |
| Out of the total population temporarily living abroad, 412,735 (61.4%) were males and 259,514 (38.6%) | -- | -- | -- | -- | -- |
| were females. Also, of the total population temporarily living abroad, 12.8 percent were reported from the | -- | -- | -- | -- | -- |
| Gampaha District, 10.6 percent from the Colombo District, and 9.5 percent from the Kurunegala District, | -- | -- | -- | -- | -- |
| while  the  lowest  percentage,  0.2  percent,  was  reported  from  the  Mannar,  Mullaitivu,  and  Kilinochchi | -- | -- | -- | -- | -- |
| Districts. | -- | -- | -- | -- | -- |
| According to Figure 5.2.1, the majority of the population temporarily living abroad, accounting for 66.8 | -- | -- | -- | -- | -- |
| percent (449,369), belonged to the 30–59 years age group. In addition, 2.9 percent (19,383) were persons | -- | -- | -- | -- | -- |
| under 18 years of age, while 2.4 percent (16,124) were aged 60 years and over. | -- | -- | -- | -- | -- |
| Sector by | Total |  | Age Group (Years) |  |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=96> (Table 5.2.2)

## 35. [Population Temporarily Living Abroad by District and Main Reason for Living in Abroad, 2024](data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Employment | Education | Accompanying Family Member In Need | Other | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 51449 | 12339 | 7230 | 421 | 71439 |
| LK-12 | Gampaha | district | 67844 | 10894 | 7028 | 311 | 86077 |
| LK-13 | Kalutara | district | 34819 | 3953 | 2469 | 111 | 41352 |
| LK-21 | Kandy | district | 48904 | 4242 | 3891 | 193 | 57230 |
| LK-22 | Matale | district | 18526 | 755 | 730 | 53 | 20064 |
| LK-23 | Nuwara Eliya | district | 15895 | 402 | 572 | 44 | 16913 |
| LK-31 | Galle | district | 35722 | 2954 | 1555 | 113 | 40344 |
| LK-32 | Matara | district | 18282 | 2145 | 840 | 53 | 21320 |
| LK-33 | Hambantota | district | 12606 | 1184 | 408 | 33 | 14231 |
| LK-41 | Jaffna | district | 7653 | 877 | 589 | 306 | 9425 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Employment": 51449,
    "Education": 12339,
    "Accompanying Family Member In Need": 7230,
    "Other": 421,
    "Total Value": 71439
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=97> (Table 5.2.3)

## 36. [Population Temporarily Living Abroad by Main Reason for Living Abroad and Age Group, 2024](data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age | Employment | Education | Accompanying Family Member In Need | Other | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Total | 577919 | 53621 | 38218 | 2491 | 672249 |
| Less than 18 | 0 | 1486 | 17862 | 35 | 19383 |
| 18 - 29 | 142256 | 38053 | 6348 | 716 | 187373 |
| 30 - 59 | 423249 | 14042 | 10530 | 1548 | 449369 |
| 60 & over | 12414 | 40 | 3478 | 192 | 16124 |

### Example Data Row (JSON)

```json
{
    "Age": "Total",
    "Employment": 577919,
    "Education": 53621,
    "Accompanying Family Member In Need": 38218,
    "Other": 2491,
    "Total Value": 672249
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=98> (Table 5.2.4)

## 37. [Population Temporarily Living Abroad, by Main Reason for Living Abroad, Country of Residence and Sex,](data/final-report-tables/chapter-5/5.2.5-Population-Temporarily-Living-Abroad,-by-Main-Reason-for-Living-Abroad,-Country-of-Residence-and-Sex,)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 | Col 13 | Col 14 | Col 15 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| residence |  |  |  |  | Employment |  |  | Education |  |  | Accompanied a family 
member’s need |  |  | Other |  |
|  | Total | Male | Female | Total | Male | Female | Total | Male | Female | Total | Male | Female | Total | Male | Female |
| Total | 672,249 | 412,735 | 259,514 | 577,919 | 367,680 | 210,239 | 53,621 | 29,735 | 23,886 | 38,218 | 14,422 | 23,796 | 2,491 | 898 | 1,593 |
|  | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Kuwait | 15.2 | 7.1 | 28.3 | 17.4 | 7.8 | 34.3 | 0.6 | 0.5 | 0.8 | 3.7 | 2.8 | 4.2 | 4.5 | 2.0 | 5.8 |
| United Arab Emirates | 14.8 | 16.8 | 11.6 | 16.2 | 18.3 | 12.7 | 2.5 | 2.6 | 2.5 | 11.2 | 10.9 | 11.5 | 6.9 | 7.5 | 6.6 |
| Saudi Arabia | 11.6 | 9.1 | 15.5 | 13.0 | 10.0 | 18.4 | 0.7 | 0.9 | 0.5 | 5.6 | 5.0 | 6.0 | 3.6 | 2.9 | 4.0 |
| Qatar | 10.5 | 15.3 | 2.9 | 11.8 | 16.8 | 2.8 | 0.7 | 1.0 | 0.4 | 6.7 | 7.4 | 6.2 | 2.7 | 3.2 | 2.4 |
| Italy | 6.0 | 6.4 | 5.5 | 5.8 | 6.3 | 4.8 | 2.6 | 2.5 | 2.7 | 14.5 | 15.8 | 13.7 | 6.5 | 6.8 | 6.3 |
| Japan | 5.4 | 6.3 | 3.9 | 3.8 | 5.0 | 1.9 | 21.3 | 23.5 | 18.6 | 6.0 | 5.2 | 6.6 | 4.8 | 4.6 | 4.9 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=99> (Table 5.2.5)

## 38. [Total Population, Sex ratio and the Percentage of Male and Female, 1946-2024](data/final-report-tables/chapter-6/6.1.1-Total-Population,-Sex-ratio-and-the-Percentage-of-Male-and-Female,-1946-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Census Year | Population | Sex Ratio | P Male | P Female |
| :-- | :-- | :-- | :-- | :-- |
| 1946 | 6657339 | 113.0 | 0.531 | 0.469 |
| 1953 | 8097895 | 115.5 | 0.527 | 0.473 |
| 1963 | 10582064 | 108.2 | 0.52 | 0.48 |
| 1971 | 12689897 | 106.1 | 0.515 | 0.485 |
| 1981 | 14846750 | 104.0 | 0.51 | 0.49 |
| 2001* | 16929689 | 99.1 | 0.498 | 0.502 |
| 2012 | 20359439 | 93.8 | 0.484 | 0.516 |
| 2024 | 21781800 | 93.3 | 0.483 | 0.517 |

### Example Data Row (JSON)

```json
{
    "Census Year": "1946",
    "Population": 6657339,
    "Sex Ratio": 113.0,
    "P Male": 0.531,
    "P Female": 0.469
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=101> (Table 6.1.1)

## 39. [Sex Ratio by Sector, 2024](data/final-report-tables/chapter-6/6.1.2-Sex-Ratio-by-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Sex Ratio |
| :-- | :-- |
| Sri Lanka | 93.3 |
| Urban | 92.8 |
| Rural | 93.3 |
| Estate Rural | 94.4 |
| Estate Urban | 98.4 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "Sex Ratio": 93.3
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=102> (Table 6.1.2)

## 40. [Population by Age Groups and Sex, 2012 and](data/final-report-tables/chapter-6/6.1.3-Population-by-Age-Groups-and-Sex,-2012-and)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 21 rows)

| Age Group | Total 2012 | Male 2012 | Female 2012 | Total 2024 | Male 2024 | Female 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 20359439 | 9856634 | 10502805 | 21781800 | 10512344 | 11269456 |
| 00-04 | 1743862 | 879223 | 864639 | 1215120 | 611081 | 604039 |
| 05-09 | 1747752 | 882108 | 865644 | 1556523 | 788544 | 767979 |
| 10-14 | 1640052 | 829069 | 810983 | 1735196 | 880905 | 854291 |
| 15-19 | 1644249 | 819927 | 824322 | 1795038 | 907739 | 887299 |
| 20-24 | 1532883 | 742316 | 790567 | 1608606 | 790215 | 818391 |
| 25-29 | 1552848 | 743510 | 809338 | 1372458 | 662751 | 709707 |
| 30-34 | 1639415 | 796866 | 842549 | 1414060 | 682568 | 731492 |
| 35-39 | 1409077 | 686037 | 723040 | 1452703 | 705129 | 747574 |
| 40-44 | 1359209 | 661623 | 697586 | 1602344 | 785927 | 816417 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "Total 2012": 20359439,
    "Male 2012": 9856634,
    "Female 2012": 10502805,
    "Total 2024": 21781800,
    "Male 2024": 10512344,
    "Female 2024": 11269456
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=104> (Table 6.1.3)

## 41. [Percentage Distribution of Population by Age Group, 1946–2024](data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 14 rows)

| Age Group | P Census 1946 | P Census 1953 | P Census 1963 | P Census 1971 | P Census 1981 | P Census 2001 | P Census 2012 | P Census 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 00-04 | 0.129 | 0.149 | 0.152 | 0.131 | 0.125 | 0.085 | 0.086 | 0.056 |
| 05-09 | 0.122 | 0.134 | 0.137 | 0.132 | 0.113 | 0.088 | 0.086 | 0.071 |
| 10-14 | 0.121 | 0.114 | 0.126 | 0.127 | 0.114 | 0.09 | 0.081 | 0.08 |
| 15-19 | 0.102 | 0.087 | 0.097 | 0.107 | 0.108 | 0.097 | 0.081 | 0.081 |
| 20-24 | 0.096 | 0.095 | 0.084 | 0.1 | 0.102 | 0.094 | 0.075 | 0.074 |
| 25-29 | 0.087 | 0.088 | 0.07 | 0.075 | 0.086 | 0.079 | 0.076 | 0.063 |
| 30-34 | 0.068 | 0.064 | 0.063 | 0.058 | 0.076 | 0.076 | 0.081 | 0.065 |
| 35-39 | 0.07 | 0.066 | 0.062 | 0.057 | 0.057 | 0.074 | 0.069 | 0.067 |
| 40-44 | 0.048 | 0.046 | 0.046 | 0.046 | 0.047 | 0.069 | 0.067 | 0.074 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "P Census 1946": 1.0,
    "P Census 1953": 1.0,
    "P Census 1963": 1.0,
    "P Census 1971": 1.0,
    "P Census 1981": 1.0,
    "P Census 2001": 1.0,
    "P Census 2012": 1.0,
    "P Census 2024": 1.0
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=105> (Table 6.1.4)

## 42. [Population Over and Below 18 Years of Age by Sector and District, 2024](data/final-report-tables/chapter-6/6.1.5-Population-Over-and-Below-18-Years-of-Age-by-Sector-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Male Over 18 Years | Male Under 18 Years | Female Over 18 Years | Female Under 18 Years | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 252843 | 901956 | 244986 | 975630 | 2375415 |
| LK-12 | Gampaha | district | 279343 | 896126 | 271604 | 989069 | 2436142 |
| LK-13 | Kalutara | district | 160868 | 470238 | 156846 | 517832 | 1305784 |
| LK-21 | Kandy | district | 194314 | 502399 | 188986 | 576196 | 1461895 |
| LK-22 | Matale | district | 72380 | 182841 | 69766 | 201883 | 526870 |
| LK-23 | Nuwara Eliya | district | 105340 | 241131 | 104274 | 274535 | 725280 |
| LK-31 | Galle | district | 138737 | 388903 | 134856 | 434876 | 1097372 |
| LK-32 | Matara | district | 109369 | 292611 | 106295 | 329614 | 837889 |
| LK-33 | Hambantota | district | 93135 | 236075 | 91535 | 250673 | 671418 |
| LK-41 | Jaffna | district | 72254 | 209299 | 70534 | 242664 | 594751 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Male Over 18 Years": 252843,
    "Male Under 18 Years": 901956,
    "Female Over 18 Years": 244986,
    "Female Under 18 Years": 975630,
    "Total Value": 2375415
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=106> (Table 6.1.5)

## 43. [Elderly Population and Sex Ratio by Age Groups, 2012 and 2024](data/final-report-tables/chapter-6/6.1.6-Elderly-Population-and-Sex-Ratio-by-Age-Groups,-2012-and-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Census of Population and Housing - 2024 | -- | -- | -- | -- | -- | -- | -- |
| Aging Index | -- | -- | -- | -- | -- | -- | -- |
| The Aging Index is defined as the number of persons aged 60 and over for every 100 children under the | -- | -- | -- | -- | -- | -- | -- |
| age of 15 in a country. This index serves as a key indicator of the various stages of demographic transition | -- | -- | -- | -- | -- | -- | -- |
| within a population. | -- | -- | -- | -- | -- | -- | -- |
| 100 |  |  |  |  |  |  |  |
| 80 |  |  |  |  |  |  |  |
| 60 |  |  |  |  |  |  | 49.1 |
| 40 |  |  |  |  |  | 35.1 |  |
|  | 14.5 | 13.6 | 14.1 | 16.3 | 18.8 |  |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=109> (Table 6.1.6)

## 44. [Median Age of the Population, 1946-2024](data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population,-1946-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Census Year | Median Age All | Median Age Male | Median Age Female |
| :-- | :-- | :-- | :-- |
| 1946 | 21.3 | 22.1 | 20.5 |
| 1953 | 20.8 | 21.7 | 19.9 |
| 1963 | 19.4 | 20.0 | 18.4 |
| 1971 | 19.7 | 20.0 | 19.3 |
| 1981 | 21.4 | 21.5 | 21.4 |
| 2012 | 30.0 | 30.0 | 31.0 |
| 2024 | 35.0 | 34.0 | 36.0 |

### Example Data Row (JSON)

```json
{
    "Census Year": "1946",
    "Median Age All": 21.3,
    "Median Age Male": 22.1,
    "Median Age Female": 20.5
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=110> (Table 6.1.7)

## 45. [Population Distribution by Ethnic Group, 2024](data/final-report-tables/chapter-6/6.1.8-Population-Distribution-by-Ethnic-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 11 rows)

| Ethnicity | Population |
| :-- | :-- |
| Sri Lanka | 21781800 |
| Sinhalese | 16144037 |
| Sri Lanka Tamil | 2681627 |
| Indian Tamil/Malaiyaga Thamilar | 600360 |
| Sri Lanka Moor/Muslim | 2283246 |
| Burgher | 31721 |
| Malay | 26650 |
| Sri Lanka Chetty | 2443 |
| Bharatha | 1183 |
| Veddas | 1373 |

### Example Data Row (JSON)

```json
{
    "Ethnicity": "Sri Lanka",
    "Population": 21781800
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=111> (Table 6.1.8)

## 46. [Percentage Distribution of the Population by Ethnic Group and Province, 2024](data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Region Id | Region Name | Region Ent Type | P Sinhalese | P Sl Tamil | P Ind And Malaiyaga Tamil | P Sl Moor | P Malay | P Burgher | P Sl Chetty | P Bharatha | P Veddahs | P Other | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-1 | Western | province | 0.836 | 0.063 | 0.005 | 0.089 | 0.003 | 0.003 | 0.0 | 0.0 | 0.0 | 0.001 | 1.0 |
| LK-2 | Central | province | 0.658 | 0.083 | 0.15 | 0.107 | 0.001 | 0.001 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| LK-3 | Southern | province | 0.948 | 0.012 | 0.004 | 0.034 | 0.0 | 0.002 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| LK-4 | Northern | province | 0.032 | 0.915 | 0.003 | 0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| LK-5 | Eastern | province | 0.221 | 0.381 | 0.001 | 0.395 | 0.003 | 0.0 | 0.0 | 0.0 | 0.001 | 0.0 | 1.002 |
| LK-6 | North Western | province | 0.848 | 0.027 | 0.001 | 0.122 | 0.001 | 0.001 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| LK-7 | North Central | province | 0.905 | 0.009 | 0.0 | 0.085 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.001 | 1.0 |
| LK-8 | Uva | province | 0.814 | 0.069 | 0.069 | 0.046 | 0.001 | 0.001 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| LK-9 | Sabaragamuwa | province | 0.865 | 0.065 | 0.022 | 0.048 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-1",
    "Region Name": "Western",
    "Region Ent Type": "province",
    "P Sinhalese": 0.836,
    "P Sl Tamil": 0.063,
    "P Ind And Malaiyaga Tamil": 0.005,
    "P Sl Moor": 0.089,
    "P Malay": 0.003,
    "P Burgher": 0.003,
    "P Sl Chetty": 0.0,
    "P Bharatha": 0.0,
    "P Veddahs": 0.0,
    "P Other": 0.001,
    "Total Value": 1.0
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=112> (Table 6.1.9)

## 47. [Population by Ethnic Group, 1911 - 2024 (in](data/final-report-tables/chapter-6/6.1.10-Population-by-Ethnic-Group,-1911---2024-(in)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Ethnicity | Census 1911 Population K | Census 1921 Population K | Census 1931 Population K | Census 1946 Population K | Census 1953 Population K | Census 1963 Population K | Census 1971 Population K | Census 1981 Population K | Census 2001 Population K | Census 2012 Population K | Census 2024 Population K | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 4106399 | 4498600 | 5306000 | 6657300 | 8097900 | 10582000 | 12689900 | 14846800 | 16929700 | 20359400 | 21781800 | 125855799 |
| Low Country Sinhalese | 1716900 | 1927100 | 2216200 | 2902500 | 3469500 | 4470300 | 5425800 | 0 | 0 | 0 | 0 | 22128300 |
| Up-country (Kandyan) | 0 | 998600 | 1089100 | 1256800 | 1718000 | 2147200 | 3042600 | 3705500 | 0 | 0 | 0 | 13957800 |
| Sri Lanka Tamil | 528000 | 517299 | 598900 | 733700 | 884700 | 1164700 | 1424000 | 1886900 | 732100 | 2269100 | 2681600 | 13420999 |
| Indian Tamil | 531000 | 602700 | 818500 | 780600 | 974100 | 1123000 | 1174900 | 818700 | 855000 | 839500 | 0 | 8518000 |
| Sri Lanka Muslim | 233900 | 251900 | 289600 | 373600 | 464000 | 626800 | 828300 | 1046900 | 1339300 | 1892600 | 2283200 | 9630100 |
| Indian Muslim | 32700 | 33000 | 36300 | 35600 | 47500 | 55400 | 27400 | 0 | 0 | 0 | 0 | 267900 |
| European | 7600 | 8100 | 9200 | 5400 | 6500 | 0 | 0 | 0 | 0 | 0 | 0 | 36800 |
| Burgher & Eurasian | 26700 | 29400 | 32299 | 41900 | 46000 | 45900 | 45400 | 39470 | 35370 | 38270 | 31770 | 412479 |
| Malay | 13000 | 13400 | 16000 | 22500 | 25400 | 33400 | 43500 | 47000 | 54800 | 44100 | 26600 | 339700 |

### Example Data Row (JSON)

```json
{
    "Ethnicity": "Sri Lanka",
    "Census 1911 Population K": 4106399,
    "Census 1921 Population K": 4498600,
    "Census 1931 Population K": 5306000,
    "Census 1946 Population K": 6657300,
    "Census 1953 Population K": 8097900,
    "Census 1963 Population K": 10582000,
    "Census 1971 Population K": 12689900,
    "Census 1981 Population K": 14846800,
    "Census 2001 Population K": 16929700,
    "Census 2012 Population K": 20359400,
    "Census 2024 Population K": 21781800,
    "Total Value": 125855799
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=113> (Table 6.1.10)

## 48. [Distribution of Population by Ethnic Group and District, 2012 and 2024](data/final-report-tables/chapter-6/6.1.11-Distribution-of-Population-by-Ethnic-Group-and-District,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Total 2012 | Total 2024 | Sinhalese 2012 | Sinhalese 2024 | Sl Tamil 2012 | Sl Tamil 2024 | Ind And Malaiyaga Tamil 2012 | Ind And Malaiyaga Tamil 2024 | Sl Moor 2012 | Sl Moor 2024 | Burgher 2012 | Burgher 2024 | Malay 2012 | Malay 2024 | Other 2012 | Other 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2324349 | 2375415 | 1778971 | 1807945 | 235090 | 243856 | 24289 | 15427 | 249609 | 285346 | 13306 | 10643 | 14444 | 8249 | 8640 | 3949 |
| LK-12 | Gampaha | district | 2304833 | 2436142 | 2086469 | 2188512 | 81245 | 97925 | 9137 | 6575 | 97621 | 123220 | 10784 | 7030 | 12720 | 9488 | 6857 | 3392 |
| LK-13 | Kalutara | district | 1221948 | 1305784 | 1060107 | 1119109 | 23035 | 41361 | 23217 | 7198 | 113320 | 136412 | 1188 | 840 | 689 | 476 | 392 | 388 |
| LK-21 | Kandy | district | 1375382 | 1461895 | 1023488 | 1077312 | 69210 | 122772 | 85111 | 38311 | 191570 | 219905 | 2384 | 1891 | 2444 | 1001 | 1175 | 703 |
| LK-22 | Matale | district | 484531 | 526870 | 391305 | 424788 | 24279 | 42172 | 23238 | 7716 | 44786 | 51471 | 386 | 359 | 392 | 283 | 145 | 81 |
| LK-23 | Nuwara Eliya | district | 711644 | 725280 | 282053 | 281904 | 32563 | 60288 | 377637 | 362299 | 17652 | 19245 | 761 | 1252 | 543 | 216 | 435 | 76 |
| LK-31 | Galle | district | 1063334 | 1097372 | 1003722 | 1030354 | 13953 | 17600 | 6146 | 2883 | 38790 | 45672 | 256 | 244 | 106 | 85 | 361 | 534 |
| LK-32 | Matara | district | 814048 | 837889 | 767580 | 788804 | 8772 | 11119 | 12127 | 8082 | 25254 | 29430 | 131 | 259 | 58 | 44 | 126 | 151 |
| LK-33 | Hambantota | district | 599903 | 671418 | 582301 | 651274 | 2105 | 2054 | 120 | 121 | 6629 | 13809 | 146 | 99 | 8164 | 3931 | 438 | 130 |
| LK-41 | Jaffna | district | 583882 | 594751 | 2284 | 3395 | 577338 | 586491 | 1807 | 782 | 2162 | 3947 | 126 | 64 | 23 | 7 | 142 | 65 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total 2012": 2324349,
    "Total 2024": 2375415,
    "Sinhalese 2012": 1778971,
    "Sinhalese 2024": 1807945,
    "Sl Tamil 2012": 235090,
    "Sl Tamil 2024": 243856,
    "Ind And Malaiyaga Tamil 2012": 24289,
    "Ind And Malaiyaga Tamil 2024": 15427,
    "Sl Moor 2012": 249609,
    "Sl Moor 2024": 285346,
    "Burgher 2012": 13306,
    "Burgher 2024": 10643,
    "Malay 2012": 14444,
    "Malay 2024": 8249,
    "Other 2012": 8640,
    "Other 2024": 3949
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=115> (Table 6.1.11)

## 49. [Percentage Distribution of Population by Ethnic Group and District, 2012 and 2024](data/final-report-tables/chapter-6/6.1.12-Percentage-Distribution-of-Population-by-Ethnic-Group-and-District,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | P Total 2012 | P Total 2024 | P Sinhalese 2012 | P Sinhalese 2024 | P Sl Tamil 2012 | P Sl Tamil 2024 | P Ind And Malaiyaga Tamil 2012 | P Ind And Malaiyaga Tamil 2024 | P Sl Moor 2012 | P Sl Moor 2024 | P Burgher 2012 | P Burgher 2024 | P Malay 2012 | P Malay 2024 | P Other 2012 | P Other 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 0.114 | 0.109 | 0.117 | 0.112 | 0.104 | 0.091 | 0.029 | 0.026 | 0.132 | 0.125 | 0.347 | 0.336 | 0.327 | 0.31 | 0.338 | 0.279 |
| LK-12 | Gampaha | district | 0.113 | 0.112 | 0.137 | 0.136 | 0.036 | 0.037 | 0.011 | 0.011 | 0.052 | 0.054 | 0.282 | 0.222 | 0.288 | 0.356 | 0.269 | 0.24 |
| LK-13 | Kalutara | district | 0.06 | 0.06 | 0.07 | 0.069 | 0.01 | 0.015 | 0.028 | 0.012 | 0.06 | 0.06 | 0.031 | 0.026 | 0.016 | 0.018 | 0.015 | 0.027 |
| LK-21 | Kandy | district | 0.068 | 0.067 | 0.067 | 0.067 | 0.03 | 0.046 | 0.101 | 0.064 | 0.101 | 0.096 | 0.062 | 0.06 | 0.055 | 0.038 | 0.046 | 0.05 |
| LK-22 | Matale | district | 0.024 | 0.024 | 0.026 | 0.026 | 0.011 | 0.016 | 0.028 | 0.013 | 0.024 | 0.023 | 0.01 | 0.011 | 0.009 | 0.011 | 0.006 | 0.006 |
| LK-23 | Nuwara Eliya | district | 0.035 | 0.033 | 0.018 | 0.017 | 0.014 | 0.022 | 0.45 | 0.603 | 0.009 | 0.008 | 0.02 | 0.039 | 0.012 | 0.008 | 0.017 | 0.005 |
| LK-31 | Galle | district | 0.052 | 0.05 | 0.066 | 0.064 | 0.006 | 0.007 | 0.007 | 0.005 | 0.02 | 0.02 | 0.007 | 0.008 | 0.002 | 0.003 | 0.014 | 0.038 |
| LK-32 | Matara | district | 0.04 | 0.038 | 0.05 | 0.049 | 0.004 | 0.004 | 0.014 | 0.013 | 0.013 | 0.013 | 0.003 | 0.008 | 0.001 | 0.002 | 0.005 | 0.011 |
| LK-33 | Hambantota | district | 0.029 | 0.031 | 0.038 | 0.04 | 0.001 | 0.001 | 0 | 0.0 | 0.004 | 0.006 | 0.004 | 0.003 | 0.185 | 0.148 | 0.017 | 0.009 |
| LK-41 | Jaffna | district | 0.029 | 0.027 | 0.0 | 0.0 | 0.254 | 0.219 | 0.002 | 0.001 | 0.001 | 0.002 | 0.003 | 0.002 | 0.001 | 0.0 | 0.006 | 0.005 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "P Total 2012": 0.114,
    "P Total 2024": 0.109,
    "P Sinhalese 2012": 0.117,
    "P Sinhalese 2024": 0.112,
    "P Sl Tamil 2012": 0.104,
    "P Sl Tamil 2024": 0.091,
    "P Ind And Malaiyaga Tamil 2012": 0.029,
    "P Ind And Malaiyaga Tamil 2024": 0.026,
    "P Sl Moor 2012": 0.132,
    "P Sl Moor 2024": 0.125,
    "P Burgher 2012": 0.347,
    "P Burgher 2024": 0.336,
    "P Malay 2012": 0.327,
    "P Malay 2024": 0.31,
    "P Other 2012": 0.338,
    "P Other 2024": 0.279
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=116> (Table 6.1.12)

## 50. [Population and Percentage Distribution by Sector and Religion, 2024](data/final-report-tables/chapter-6/6.1.13-Population-and-Percentage-Distribution-by-Sector-and-Religion,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  | Religion |  |  |  |
| Sector | Total | Buddhist | Hindu | Islam | Roman | Other | Other |
|  |  |  |  |  | Catholic | Christian |  |
| Sri Lanka | 21,781,800 | 15,199,093 | 2,734,839 | 2,337,379 | 1,224,348 | 282,185 | 3,956 |
|  | 100.0 | 69.8 | 12.6 | 10.7 | 5.6 | 1.3 | 0.0 |
| Urban* | 3,819,203 | 2,060,541 | 498,717 | 783,638 | 380,543 | 94,038 | 1,726 |
|  | 100.0 | 54.0 | 13.0 | 20.5 | 10.0 | 2.5 | 0.0 |
| Rural | 17,096,918 | 13,044,342 | 1,539,173 | 1,544,664 | 801,977 | 164,634 | 2,128 |
|  | 100.0 | 76.3 | 9.0 | 9.0 | 4.7 | 1.0 | 0.0 |
| Estate Rural** | 865,679 | 94,210 | 696,949 | 9,077 | 41,828 | 23,513 | 102 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=122> (Table 6.1.13)

## 51. [Distribution of Population by Religion and District, 2012](data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District,-2012)

*Build Status (**5**/5) ✅ All Stages Complete*

### Lanka Data (first 30 of 1276 lines)

```json
{
    "_meta": {
        "source_url": "https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=123",
        "source_description": [
            "Table 6.1.14, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka"
        ],
        "what": {
            "Religion": "Distribution of Population by Religion and District, 2012"
        },
        "when": "2024",
        "where_types": [
            "district",
            "country",
            "ed",
            "province"
        ]
    },
    "Religion": {
        "2024": {
            "LK-11": {
                "region_id": "LK-11",
                "region_name": "Colombo",
                "region_ent_type": "district",
                "values": {
                    "Buddhist": 1632225,
                    "Islam": 274087,
                    "Hindu": 186454,
                    "RomanCatholic": 162314,
                    "OtherChristian": 66994,
                    "Other": 2275
...
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=123> (Table 6.1.14)

## 52. [Distribution of Population by Religion and District, 2024](data/final-report-tables/chapter-6/6.1.15-Distribution-of-Population-by-Religion-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 58 rows)

| Region Id | Region Name | Region Ent Type | Buddhist | Hindu | Islam | Roman Catholic | Other Christian | Other | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 1682524 | 197759 | 298422 | 139882 | 55624 | 1204 | 2375415 |
| LK-12 | Gampaha | district | 1744475 | 69429 | 134422 | 442291 | 44540 | 985 | 2436142 |
| LK-13 | Kalutara | district | 1080638 | 42528 | 138230 | 36510 | 7733 | 145 | 1305784 |
| LK-21 | Kandy | district | 1063511 | 144618 | 223997 | 18623 | 10919 | 227 | 1461895 |
| LK-22 | Matale | district | 418608 | 46181 | 52224 | 7797 | 2026 | 34 | 526870 |
| LK-23 | Nuwara Eliya | district | 278828 | 377266 | 21929 | 31705 | 15474 | 78 | 725280 |
| LK-31 | Galle | district | 1026031 | 15600 | 46038 | 4207 | 5377 | 119 | 1097372 |
| LK-32 | Matara | district | 787303 | 14625 | 29858 | 2445 | 3619 | 39 | 837889 |
| LK-33 | Hambantota | district | 649736 | 1401 | 17947 | 1017 | 1247 | 70 | 671418 |
| LK-41 | Jaffna | district | 2788 | 489521 | 4352 | 77197 | 20857 | 36 | 594751 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Buddhist": 1682524,
    "Hindu": 197759,
    "Islam": 298422,
    "Roman Catholic": 139882,
    "Other Christian": 55624,
    "Other": 1204,
    "Total Value": 2375415
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=124> (Table 6.1.15)

## 53. [Distribution of the Population Aged 5 Years and Over by Level of Physical and Mental Difficulties for EachFunctional Domain, 2024](data/final-report-tables/chapter-6/6.2.1-Distribution-of-the-Population-Aged-5-Years-and-Over-by-Level-of-Physical-and-Mental-Difficulties-for-EachFunctional-Domain,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Functional Domains | Number | Rate  
(per 1,000 | Number | Rate  
(per 1,000 | Number | Rate  
(per 1,000 | Number | Rate  
(per 1,000 |
|  |  | persons) |  | persons) |  | persons) |  | persons) |
| Seeing | 18,626,725 | 906 | 1,747,377 | 85 | 168,207 | 8 | 24,371 | 1 |
| Hearing | 19,833,909 | 965 | 602,674 | 29 | 105,760 | 5 | 24,337 | 1 |
| Walking or climbing steps | 18,862,616 | 917 | 1,256,095 | 61 | 369,762 | 18 | 78,207 | 4 |
| Remembering or 
concentrating on something | 19,779,068 | 962 | 619,786 | 30 | 133,641 | 6 | 34,185 | 2 |
| Selfcare, such as washing all 
over or dressing | 19,926,695 | 969 | 450,693 | 22 | 124,756 | 6 | 64,536 | 3 |
| Communicating with others | 20,145,867 | 979 | 308,015 | 15 | 72,412 | 4 | 40,386 | 2 |
| Communicating with others | 20,145,867 | 979 | 308,015 | 15 | 72,412 | 4 | 40,386 | 2 |
| The highest number of individuals reporting any level of difficulty (“some difficulty,” “a lot of difficulty,” or |  |  |  |  |  |  |  |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=127> (Table 6.2.1)

## 54. [Distribution of Persons Aged 5 Years and Over with Physical and Mental Difficulties by District and Difficulties,2024](data/final-report-tables/chapter-6/6.2.2-Distribution-of-Persons-Aged-5-Years-and-Over-with-Physical-and-Mental-Difficulties-by-District-and-Difficulties,2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 26 rows)

| Null | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 1939955 | 732771 | 1704064 | 787612 | 639985 | 420813 | 14341480 | 20566680 |
| Colombo | 152592 | 59508 | 150614 | 69279 | 55244 | 40731 | 1743322 | 2271290 |
| Gampaha | 194156 | 76279 | 184771 | 85190 | 65653 | 44483 | 1668658 | 2319190 |
| Kalutara | 100364 | 42776 | 95264 | 45878 | 36097 | 25241 | 894125 | 1239745 |
| Kandy | 133777 | 54309 | 127934 | 57599 | 41366 | 29762 | 937752 | 1382499 |
| Matale | 52463 | 20217 | 48307 | 22094 | 15106 | 10414 | 328309 | 496910 |
| Nuwara Eliya | 72180 | 23606 | 63822 | 26066 | 22496 | 13826 | 458435 | 680431 |
| Galle | 100166 | 40849 | 85974 | 43463 | 30609 | 23279 | 715115 | 1039455 |
| Matara | 91333 | 33262 | 73867 | 35908 | 22831 | 17363 | 518248 | 792812 |
| Hambantota | 76574 | 26427 | 60341 | 28688 | 20944 | 15295 | 403350 | 631619 |

### Example Data Row (JSON)

```json
{
    "Null": "Sri Lanka",
    "Difficulty In Seeing": 1939955,
    "Difficulty In Hearing": 732771,
    "Difficulty In Walking Or Climbing Steps": 1704064,
    "Difficulty In Remembering Or Concentrating": 787612,
    "Difficulty In Selfcare Such As Washing Or Dressing": 639985,
    "Difficulty In Communicating With Others": 420813,
    "No Disability": 14341480,
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=128> (Table 6.2.2)

## 55. [Distribution of Persons Aged 5 Years and Over with Physical and Mental Difficulties by Age Group andDifficulties, 2024](data/final-report-tables/chapter-6/6.2.3-Distribution-of-Persons-Aged-5-Years-and-Over-with-Physical-and-Mental-Difficulties-by-Age-Group-andDifficulties,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 17 rows)

| Age Group | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | No Disability | Total Description | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 1939955 | 732771 | 1704064 | 787612 | 639985 | 420813 | 14341480 | population_aged_5_years_and_above | 20566680 |
| 05 - 09 | 11808 | 4493 | 11683 | 13430 | 29556 | 17505 | 1468048 | population_aged_5_years_and_above | 1556523 |
| 10 - 14 | 21988 | 6004 | 12967 | 12676 | 11908 | 14088 | 1655565 | population_aged_5_years_and_above | 1735196 |
| 15 - 19 | 30524 | 6589 | 14523 | 13647 | 10169 | 14490 | 1705096 | population_aged_5_years_and_above | 1795038 |
| 20 - 24 | 27860 | 6274 | 14656 | 12703 | 9315 | 13383 | 1524415 | population_aged_5_years_and_above | 1608606 |
| 25 - 29 | 24105 | 6590 | 15010 | 12176 | 8836 | 12367 | 1293374 | population_aged_5_years_and_above | 1372458 |
| 30 - 34 | 26681 | 7805 | 19457 | 13634 | 9723 | 13393 | 1323367 | population_aged_5_years_and_above | 1414060 |
| 35 - 39 | 38818 | 8894 | 27929 | 15406 | 11353 | 13775 | 1336528 | population_aged_5_years_and_above | 1452703 |
| 40 - 44 | 106436 | 13057 | 45340 | 19938 | 14847 | 15870 | 1386856 | population_aged_5_years_and_above | 1602344 |
| 45 - 49 | 163791 | 18517 | 68656 | 23994 | 18532 | 17318 | 1179957 | population_aged_5_years_and_above | 1490765 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "Difficulty In Seeing": 1939955,
    "Difficulty In Hearing": 732771,
    "Difficulty In Walking Or Climbing Steps": 1704064,
    "Difficulty In Remembering Or Concentrating": 787612,
    "Difficulty In Selfcare Such As Washing Or Dressing": 639985,
    "Difficulty In Communicating With Others": 420813,
    "No Disability": 14341480,
    "Total Description": "population_aged_5_years_and_above",
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=129> (Table 6.2.3)

## 56. [Distribution of Persons Aged 5 Years and Over with Disabilities by Sex and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.4-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Sex-and-Domain-of-Disability,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 |
| :-- | :-- |
|  | Census of Population and Housing  - 2024 |
| 6.2.4 Persons with Physical and Mental Disabilities |  |
| For each type of functional domain considered, the level of difficulty reported by an individual was used to |  |
| identify persons with disabilities. If an individual reported “a lot of difficulty” or “cannot do at all” for any |  |
| functionality, then they were classified as a person with a disability. An individual may have one or more |  |
| disabilities. |  |
| Accordingly, 727,293 persons aged 5 years and over were identified having at least one disability under |  |
| 6 | functional  domains:  seeing,  hearing,  walking  or  climbing  steps,  remembering  or  concentrating, |
| performing daily activities independently, and communicating with others. Any individual with at least one |  |
| disability is included in this count. Expressed as a rate, this corresponds to 35 persons with a disability per |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=130> (Table 6.2.4)

## 57. [Distribution of Persons Aged 5 Years and Over with Disabilities by Sector and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.5-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Sector-and-Domain-of-Disability,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  | Sector |  |  |
|  |  | Total | Urban | Estate Urban | Rural | Estate Rural |
| Total population aged 5 
years and over | Number | 20,566,680 | 3,613,813 | 11,299 | 16,131,086 | 810,482 |
| Population with at least one | Number | 727,293 | 96,426 | 260 | 601,740 | 28,867 |
| disability | Rate  
(per 1,000 persons) | 35 | 27 | 23 | 37 | 36 |
| Domain of Disability |  | Total | Urban | Estate Urban | Rural | Estate Rural |
| Seeing | Number | 192,578 | 23,378 | 73 | 159,285 | 9,842 |
|  | Rate  
(per 1,000 persons) | 9 | 6 | 6 | 10 | 12 |
| Hearing | Number | 130,097 | 14,653 | 45 | 110,852 | 4,547 |
|  | Rate  
(per 1,000 persons) | 6 | 4 | 4 | 7 | 6 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=131> (Table 6.2.5)

## 58. [Distribution of Persons Aged 5 Years and Over with Disabilities by District and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.6-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-District-and-Domain-of-Disability,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 26 rows)

| Null | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 192578 | 130097 | 447969 | 167826 | 189292 | 112798 | 19326120 | 20566680 |
| Colombo | 14104 | 9047 | 36504 | 14600 | 16175 | 9811 | 2171049 | 2271290 |
| Gampaha | 18644 | 13115 | 47894 | 18425 | 19647 | 11712 | 2189753 | 2319190 |
| Kalutara | 9481 | 6799 | 23755 | 10042 | 10463 | 6722 | 1172483 | 1239745 |
| Kandy | 13417 | 9188 | 31825 | 11750 | 11875 | 7553 | 1296891 | 1382499 |
| Matale | 5188 | 3644 | 12578 | 4415 | 4266 | 2744 | 464075 | 496910 |
| Nuwara Eliya | 8845 | 4379 | 15715 | 5311 | 6415 | 3401 | 636365 | 680431 |
| Galle | 9732 | 7556 | 22876 | 9813 | 10001 | 6727 | 972750 | 1039455 |
| Matara | 8935 | 6519 | 20559 | 8317 | 8065 | 5307 | 735110 | 792812 |
| Hambantota | 7631 | 4848 | 16678 | 6608 | 6351 | 4326 | 585177 | 631619 |

### Example Data Row (JSON)

```json
{
    "Null": "Sri Lanka",
    "Difficulty In Seeing": 192578,
    "Difficulty In Hearing": 130097,
    "Difficulty In Walking Or Climbing Steps": 447969,
    "Difficulty In Remembering Or Concentrating": 167826,
    "Difficulty In Selfcare Such As Washing Or Dressing": 189292,
    "Difficulty In Communicating With Others": 112798,
    "No Disability": 19326120,
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=132> (Table 6.2.6)

## 59. [Distribution of Persons Aged 5 Years and Over with Disabilities by Age Group and Domain of Disability,](data/final-report-tables/chapter-6/6.2.7-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Age-Group-and-Domain-of-Disability,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 17 rows)

| Age Group | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | Difficulty In Communicating With Others Rate Per 1000 Persons | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 192578 | 130097 | 447969 | 167826 | 189292 | 112798 | 5.0 | 19326115.0 | 20566680.0 |
| 05 - 09 | 2513 | 1693 | 3685 | 4215 | 6959 | 5358 | 3.0 | 1532097.0 | 1556523.0 |
| 10 - 14 | 3145 | 2050 | 4264 | 5822 | 5232 | 6095 | 4.0 | 1708584.0 | 1735196.0 |
| 15 - 19 | 3346 | 2151 | 4698 | 6514 | 4983 | 6287 | 4.0 | 1767055.0 | 1795038.0 |
| 20 - 24 | 2911 | 2163 | 4450 | 5909 | 4392 | 5651 | 4.0 | 1583126.0 | 1608606.0 |
| 25 - 29 | 2499 | 2515 | 4362 | 5455 | 3838 | 5444 | 4.0 | 1348341.0 | 1372458.0 |
| 30 - 34 | 2915 | 2918 | 5426 | 5882 | 4104 | 5682 | 4.0 | 1387129.0 | 1414060.0 |
| 35 - 39 | 3686 | 2864 | 7291 | 5813 | 4139 | 5317 | 4.0 | 1423589.0 | 1452703.0 |
| 40 - 44 | 5677 | 3549 | 10262 | 6751 | 4936 | 5576 | 3.0 | 1565590.0 | 1602344.0 |
| 45 - 49 | 7939 | 4754 | 14371 | 6761 | 5686 | 6229 | 4.0 | 1445021.0 | 1490765.0 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "Difficulty In Seeing": 192578,
    "Difficulty In Hearing": 130097,
    "Difficulty In Walking Or Climbing Steps": 447969,
    "Difficulty In Remembering Or Concentrating": 167826,
    "Difficulty In Selfcare Such As Washing Or Dressing": 189292,
    "Difficulty In Communicating With Others": 112798,
    "Difficulty In Communicating With Others Rate Per 1000 Persons": 5.0,
    "No Disability": 19326115.0,
    "Total Value": 20566680.0
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=133> (Table 6.2.7)

## 60. [Distribution of Persons with a Single Disability and with Multiple Disabilities by Age Group, 2024](data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 17 rows)

| Age Group | With Single Disability | With More Than One Disability | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 452247 | 275046 | 19839387 | 20566680 |
| 05 - 09 | 7320 | 5419 | 1543784 | 1556523 |
| 10 - 14 | 6995 | 6400 | 1721801 | 1735196 |
| 15 - 19 | 7643 | 6713 | 1780682 | 1795038 |
| 20 - 24 | 7169 | 6153 | 1595284 | 1608606 |
| 25 - 29 | 7156 | 5950 | 1359352 | 1372458 |
| 30 - 34 | 8909 | 6515 | 1398636 | 1414060 |
| 35 - 39 | 11522 | 6555 | 1434626 | 1452703 |
| 40 - 44 | 16534 | 7734 | 1578076 | 1602344 |
| 45 - 49 | 21690 | 9434 | 1459641 | 1490765 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "With Single Disability": 452247,
    "With More Than One Disability": 275046,
    "No Disability": 19839387,
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=134> (Table 6.2.8)

## 61. [Distribution of Persons Aged 5 Years and Over with Disabilities by Marital Status and Sex, 2024](data/final-report-tables/chapter-6/6.2.9-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Marital Status | Total | Male | Female | Total With Disability | Male With Disability | Female With Disability |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 20566680 | 9901263 | 10665417 | 727293 | 313354 | 413939 |
| Never Married | 7885030 | 4197243 | 3687787 | 139784 | 75568 | 64216 |
| Married | 11161078 | 5417431 | 5743647 | 385815 | 205805 | 180010 |
| Widowed | 1234418 | 175421 | 1058997 | 187613 | 25746 | 161867 |
| Divorced | 74355 | 28952 | 45403 | 3161 | 1356 | 1805 |
| Legally  Separated | 44904 | 17047 | 27857 | 1837 | 814 | 1023 |
| Separated   (not Legally) | 166895 | 65169 | 101726 | 9083 | 4065 | 5018 |

### Example Data Row (JSON)

```json
{
    "Marital Status": "Sri Lanka",
    "Total": 20566680,
    "Male": 9901263,
    "Female": 10665417,
    "Total With Disability": 727293,
    "Male With Disability": 313354,
    "Female With Disability": 413939
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=135> (Table 6.2.9)

## 62. [Distribution of Persons Aged 5 Years and Over with Disabilities by Highest Educational Qualification and Sex,2024](data/final-report-tables/chapter-6/6.2.10-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-and-Sex,2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Highest Educational Qualification | Total | Male | Female | Total With Disability | Male With Disability | Female With Disability |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 20566680 | 9901263 | 10665417 | 727293 | 313354 | 413939 |
| Never attended School | 686465 | 282453 | 404012 | 110110 | 41224 | 68886 |
| Studied/Studying Special  School/Educational unit | 42104 | 24061 | 18043 | 14517 | 8447 | 6070 |
| Passed Grade 1-5* | 3601416 | 1742869 | 1858547 | 227992 | 93332 | 134660 |
| Passed Grade 6-8 | 2766674 | 1418432 | 1348242 | 127874 | 58185 | 69689 |
| Passed Grade 9-10 | 4623851 | 2363972 | 2259879 | 116913 | 53514 | 63399 |
| G.C.E. (O/L) or equivalent | 4266317 | 2092848 | 2173469 | 81876 | 37019 | 44857 |
| G.C.E. (A/L) or equivalent | 3557265 | 1543135 | 2014130 | 39559 | 17330 | 22229 |
| Degree & above | 1022588 | 433493 | 589095 | 8452 | 4303 | 4149 |
| Degree & above | 1022588 | 433493 | 589095 | 8452 | 4303 | 4149 |

### Example Data Row (JSON)

```json
{
    "Highest Educational Qualification": "Sri Lanka",
    "Total": 20566680,
    "Male": 9901263,
    "Female": 10665417,
    "Total With Disability": 727293,
    "Male With Disability": 313354,
    "Female With Disability": 413939
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=135> (Table 6.2.10)

## 63. [Distribution of Persons Aged 5 Years and Over with Disabilities by Marital Status and Domain of Disability,2024](data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability,2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Marital Status | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 192578 | 130097 | 447969 | 167826 | 189292 | 112798 | 19326120 | 20566680 |
| Never Married | 26799 | 24124 | 55653 | 63731 | 47650 | 53285 | 7613788 | 7885030 |
| Married | 108272 | 64434 | 247239 | 58641 | 84887 | 38237 | 10559368 | 11161078 |
| Widowed | 54018 | 39306 | 137784 | 42185 | 54247 | 19327 | 887551 | 1234418 |
| Divorced | 712 | 499 | 1553 | 840 | 633 | 494 | 69624 | 74355 |
| Legally Separated | 430 | 268 | 981 | 417 | 332 | 245 | 42231 | 44904 |
| Separated(not Legally) | 2347 | 1466 | 4759 | 2012 | 1543 | 1210 | 153558 | 166895 |

### Example Data Row (JSON)

```json
{
    "Marital Status": "Sri Lanka",
    "Difficulty In Seeing": 192578,
    "Difficulty In Hearing": 130097,
    "Difficulty In Walking Or Climbing Steps": 447969,
    "Difficulty In Remembering Or Concentrating": 167826,
    "Difficulty In Selfcare Such As Washing Or Dressing": 189292,
    "Difficulty In Communicating With Others": 112798,
    "No Disability": 19326120,
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=136> (Table 6.2.11)

## 64. [Distribution of Persons Aged 5 Years and Over with Disabilities by Highest Educational Qualification andDomain of Disability, 2024](data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Highest Educational Qualification | Difficulty In Seeing | Difficulty In Hearing | Difficulty In Walking Or Climbing Steps | Difficulty In Remembering Or Concentrating | Difficulty In Selfcare Such As Washing Or Dressing | Difficulty In Communicating With Others | No Disability | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 192578 | 130097 | 447969 | 167826 | 189292 | 112798 | 19326120 | 20566680 |
| Never attended School | 30146 | 27485 | 61681 | 46627 | 43022 | 39767 | 437737 | 686465 |
| Studied/Studying Special  School/ Educational unit | 1086 | 3518 | 2664 | 7992 | 4516 | 9367 | 12961 | 42104 |
| Passed Grade 1-5* | 66400 | 45542 | 144615 | 51177 | 60164 | 28445 | 3205073 | 3601416 |
| Passed Grade 6-8 | 33325 | 21432 | 82747 | 23477 | 29113 | 12753 | 2563827 | 2766674 |
| Passed Grade 9-10 | 29431 | 16295 | 71595 | 19057 | 23440 | 11283 | 4452750 | 4623851 |
| G.C.E. (O/L) or equivalent | 20120 | 10246 | 53684 | 11951 | 17462 | 6739 | 4146115 | 4266317 |
| G.C.E. (A/L) or equivalent | 9754 | 4577 | 25683 | 6207 | 9369 | 3538 | 3498137 | 3557265 |
| Degree & above | 2316 | 1002 | 5300 | 1338 | 2206 | 906 | 1009520 | 1022588 |

### Example Data Row (JSON)

```json
{
    "Highest Educational Qualification": "Sri Lanka",
    "Difficulty In Seeing": 192578,
    "Difficulty In Hearing": 130097,
    "Difficulty In Walking Or Climbing Steps": 447969,
    "Difficulty In Remembering Or Concentrating": 167826,
    "Difficulty In Selfcare Such As Washing Or Dressing": 189292,
    "Difficulty In Communicating With Others": 112798,
    "No Disability": 19326120,
    "Total Value": 20566680
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=136> (Table 6.2.12)

## 65. [Economic Activities of Persons Aged 15 Years and Over with Disabilities, 2024](data/final-report-tables/chapter-6/6.2.13-Economic-Activities-of-Persons-Aged-15-Years-and-Over-with-Disabilities,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Census of Population and Housing  - 2024 | -- | -- | -- | -- | -- | -- |
| Table  6.2.12  shows  the  prevalence  of  each  disability  domain  according  to  the  highest  educational | -- | -- | -- | -- | -- | -- |
| qualification attained. The highest rate of seeing disability and the highest rate of walking or climbing stairs | -- | -- | -- | -- | -- | -- |
| disability are reported among person who have not attended school while disability rates of all other types | -- | -- | -- | -- | -- | -- |
| of disabilities are highest among persons who are studying or have attended a special school/educational | -- | -- | -- | -- | -- | -- |
| unit. | -- | -- | -- | -- | -- | -- |
|  |  |  | Persons with at least one disability |  |  |  |
| Status of Economic Activity | Total | % | Male |  | Female |  |
|  |  |  | Number | % | Number | % |
| Aged 15 years and over | 701,159 | 100.0 | 298,438 | 100.0 | 402,721 | 100.0 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=137> (Table 6.2.13)

## 66. [Economic Activity of Persons Aged 15 Years and Over with Disabilities by Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.14-Economic-Activity-of-Persons-Aged-15-Years-and-Over-with-Disabilities-by-Domain-of-Disability,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  |  | climbing steps |  | concentrating |  | dressing |  |  |  |
|  | Number | % | Number | % | Number | % | Number | % | Number | % | Number | % |
| Persons with disabilities aged 15 and over | 186,920 | 100.0 | 126,354 | 100.0 | 440,020 | 100.0 | 157,789 | 100.0 | 177,101 | 100.0 | 101,345 | 100.0 |
| Economically active | 31,863 | 17.0 | 18,240 | 14.4 | 37,321 | 8.5 | 6,518 | 4.1 | 4,624 | 2.6 | 9,828 | 9.7 |
| Economically inactive | 155,057 | 83.0 | 108,114 | 85.6 | 402,699 | 91.5 | 151,271 | 95.9 | 172,477 | 97.4 | 91,517 | 90.3 |
| Economically active | 31,863 | 100.0 | 18,240 | 100.0 | 37,321 | 100.0 | 6,518 | 100.0 | 4,624 | 100.0 | 9,828 | 100.0 |
| Employed | 30,041 | 94.3 | 17,459 | 95.7 | 35,127 | 94.1 | 6,004 | 92.1 | 4,011 | 86.7 | 9,206 | 93.7 |
| Unemployed | 1,822 | 5.7 | 781 | 4.3 | 2,194 | 5.9 | 514 | 7.9 | 613 | 13.3 | 622 | 6.3 |
| Economically inactive | 155,057 | 100.0 | 108,114 | 100.0 | 402,699 | 100.0 | 151,271 | 100.0 | 172,477 | 100.0 | 91,517 | 100.0 |
| Engaged educational or vocational training 
activities | 3,336 | 2.2 | 1,289 | 1.2 | 1,606 | 0.4 | 1,255 | 0.8 | 904 | 0.5 | 1,675 | 1.8 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=138> (Table 6.2.14)

## 67. [Number of Persons Reporting and Not Reporting Diseases, 2024](data/final-report-tables/chapter-6/6.3.1-Number-of-Persons-Reporting-and-Not-Reporting-Diseases,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 |
| :-- | :-- |
| 6.3 Non-Communicable Diseases |  |
| I
ntroduction |  |
| According to the World Health Organization (WHO), Non-Communicable Diseases (NCDs), also referred |  |
| to as chronic illnesses, are diseases of long duration that are not transmitted directly from one person to |  |
| another.  These  conditions  arise | from  a  combination  of  genetic,  physiological,  environmental,  and |
| behavioral  factors1.  Considering  the  rapid  increase  in  NCDs,  information  on  several  prevalent  non- |  |
| communicable diseases was collected from all usual residents in Sri Lanka during the Census of Population |  |
| and Housing - 2024 for the first time in census history. Accordingly, this chapter presents prevalence of |  |
| some commonly reported NCDs such as diabetes, high cholesterol, high blood pressure, heart disease, |  |
| kidney disease, thalassemia, cancer, stroke, asthma, and epilepsy. |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=139> (Table 6.3.1)

## 68. [Prevalence Rates of the Population with at Least One Non-Communicable Disease by Age Group and Sex,](data/final-report-tables/chapter-6/6.3.2-Prevalence-Rates-of-the-Population-with-at-Least-One-Non-Communicable-Disease-by-Age-Group-and-Sex,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 22 rows)

| Age Group | Total | Male | Female | Total With At Least One Ncd | Male With At Least One Ncd | Female With At Least One Ncd | P Total | P Male | P Female |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 21779483 | 10510498 | 11268985 | 4185749 | 1725859 | 2459890 | 0.192 | 0.164 | 0.218 |
| 00-04 | 1215095 | 611067 | 604028 | 13673 | 7507 | 6166 | 0.011 | 0.012 | 0.01 |
| 05-09 | 1556507 | 788536 | 767971 | 29688 | 16709 | 12979 | 0.019 | 0.021 | 0.017 |
| 10-14 | 1735181 | 880895 | 854286 | 35588 | 20225 | 15363 | 0.021 | 0.023 | 0.018 |
| 15-19 | 1795024 | 907730 | 887294 | 31370 | 16270 | 15100 | 0.017 | 0.018 | 0.017 |
| 20-24 | 1608577 | 790203 | 818374 | 29256 | 13480 | 15776 | 0.018 | 0.017 | 0.019 |
| 25-29 | 1372421 | 662725 | 709696 | 36874 | 16189 | 20685 | 0.027 | 0.024 | 0.029 |
| 30-34 | 1414013 | 682539 | 731474 | 67032 | 28862 | 38170 | 0.047 | 0.042 | 0.052 |
| 35-39 | 1452617 | 705065 | 747552 | 127106 | 56111 | 70995 | 0.088 | 0.08 | 0.095 |
| 40-44 | 1602207 | 785827 | 816380 | 239883 | 107296 | 132587 | 0.15 | 0.137 | 0.162 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "Total": 21779483,
    "Male": 10510498,
    "Female": 11268985,
    "Total With At Least One Ncd": 4185749,
    "Male With At Least One Ncd": 1725859,
    "Female With At Least One Ncd": 2459890,
    "P Total": 0.192,
    "P Male": 0.164,
    "P Female": 0.218
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=140> (Table 6.3.2)

## 69. [Number of Individuals Living with Non-Communicable Diseases and Prevalence Rates, 2024](data/final-report-tables/chapter-6/6.3.3-Number-of-Individuals-Living-with-Non-Communicable-Diseases-and-Prevalence-Rates,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Disease | Population | Prevelence Rate |
| :-- | :-- | :-- |
| High Blood Pressure | 2200179 | 10.1 |
| Diabetes | 1850857 | 8.5 |
| High Cholesterol | 1795939 | 8.2 |
| Heart Disease | 534480 | 2.5 |
| Asthma | 401406 | 1.8 |
| Kidney Disease | 171348 | 0.8 |
| Stroke/Paralysis | 128396 | 0.6 |
| Cancer | 85787 | 0.4 |
| Epilepsy | 65008 | 0.3 |
| Thalassemia | 18645 | 0.1 |

### Example Data Row (JSON)

```json
{
    "Disease": "High Blood Pressure",
    "Population": 2200179,
    "Prevelence Rate": 10.1
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=141> (Table 6.3.3)

## 70. [Prevalence Rates of Non-Communicable Diseases by District, 2024](data/final-report-tables/chapter-6/6.3.4-Prevalence-Rates-of-Non-Communicable-Diseases-by-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 60 rows)

| Region Id | Region Name | Region Ent Type | Total Value | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2374869.355 | 0.107 | 0.091 | 0.105 | 0.025 | 0.005 | 0.001 | 0.003 | 0.004 | 0.012 | 0.002 |
| LK-12 | Gampaha | district | 2435913.363 | 0.105 | 0.096 | 0.107 | 0.025 | 0.006 | 0.001 | 0.004 | 0.005 | 0.012 | 0.002 |
| LK-13 | Kalutara | district | 1305708.339 | 0.092 | 0.089 | 0.102 | 0.024 | 0.006 | 0.001 | 0.004 | 0.006 | 0.012 | 0.003 |
| LK-21 | Kandy | district | 1461755.352 | 0.088 | 0.082 | 0.116 | 0.027 | 0.006 | 0.001 | 0.004 | 0.006 | 0.019 | 0.003 |
| LK-22 | Matale | district | 526849.34 | 0.078 | 0.079 | 0.113 | 0.025 | 0.011 | 0.001 | 0.004 | 0.006 | 0.02 | 0.003 |
| LK-23 | Nuwara Eliya | district | 725251.279 | 0.054 | 0.049 | 0.102 | 0.027 | 0.006 | 0.001 | 0.004 | 0.009 | 0.022 | 0.005 |
| LK-31 | Galle | district | 1097225.334 | 0.08 | 0.09 | 0.098 | 0.027 | 0.006 | 0.001 | 0.004 | 0.006 | 0.019 | 0.003 |
| LK-32 | Matara | district | 837756.359 | 0.084 | 0.096 | 0.103 | 0.03 | 0.007 | 0.001 | 0.004 | 0.005 | 0.025 | 0.004 |
| LK-33 | Hambantota | district | 671383.333 | 0.08 | 0.095 | 0.09 | 0.025 | 0.007 | 0.001 | 0.004 | 0.006 | 0.022 | 0.003 |
| LK-41 | Jaffna | district | 594699.375 | 0.104 | 0.099 | 0.105 | 0.021 | 0.006 | 0.001 | 0.004 | 0.006 | 0.024 | 0.005 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total Value": 2374869.355,
    "P Diabetes": 0.107,
    "P High Cholesterol": 0.091,
    "P High Blood Pressure": 0.105,
    "P Heart Disease": 0.025,
    "P Kidney Disease": 0.005,
    "P Thalassemia": 0.001,
    "P Cancer": 0.003,
    "P Stroke": 0.004,
    "P Asthma": 0.012,
    "P Epilepsy": 0.002
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=142> (Table 6.3.4)

## 71. [Prevalence Rates of Self-Reported Illnesses by Sector, 2024](data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Urban* | 0.104 | 0.089 | 0.103 | 0.024 | 0.005 | 0.001 | 0.003 | 0.004 | 0.014 | 0.002 |
| Rural | 0.083 | 0.083 | 0.101 | 0.025 | 0.009 | 0.001 | 0.004 | 0.006 | 0.019 | 0.003 |
| Estate Rural** | 0.044 | 0.036 | 0.082 | 0.024 | 0.005 | 0.001 | 0.003 | 0.008 | 0.025 | 0.006 |

### Example Data Row (JSON)

```json
{
    "Sector": "Urban*",
    "P Diabetes": 0.104,
    "P High Cholesterol": 0.089,
    "P High Blood Pressure": 0.103,
    "P Heart Disease": 0.024,
    "P Kidney Disease": 0.005,
    "P Thalassemia": 0.001,
    "P Cancer": 0.003,
    "P Stroke": 0.004,
    "P Asthma": 0.014,
    "P Epilepsy": 0.002
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=143> (Table 6.3.5)

## 72. [Prevalence Rates of Non-Communicable Diseases by Sex, 2024](data/final-report-tables/chapter-6/6.3.6-Prevalence-Rates-of-Non-Communicable-Diseases-by-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 11 rows)

| Disease | Males With Disease | P Male Prevalence Rate | Females With Disease | P Female Prevalence Rate |
| :-- | :-- | :-- | :-- | :-- |
| At Least One NCD | 1725859 | 0.164 | 2459890 | 0.218 |
| High Blood Pressure (Hypertension) | 772517 | 0.073 | 1427662 | 0.127 |
| Diabetes | 766406 | 0.073 | 1084451 | 0.096 |
| High Cholesterol | 638387 | 0.061 | 1157552 | 0.103 |
| Heart Disease | 282539 | 0.027 | 251941 | 0.022 |
| Asthma | 164019 | 0.016 | 237387 | 0.021 |
| Kidney Disease | 105929 | 0.01 | 65419 | 0.006 |
| Stroke/Paralysis | 73088 | 0.007 | 55308 | 0.005 |
| Cancer | 26433 | 0.003 | 59354 | 0.005 |
| Epilepsy | 36984 | 0.004 | 28024 | 0.002 |

### Example Data Row (JSON)

```json
{
    "Disease": "At Least One NCD",
    "Males With Disease": 1725859,
    "P Male Prevalence Rate": 0.164,
    "Females With Disease": 2459890,
    "P Female Prevalence Rate": 0.218
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=143> (Table 6.3.6)

## 73. [Prevalence Rates of Non-Communicable Diseases by Age Group, 2024](data/final-report-tables/chapter-6/6.3.7-Prevalence-Rates-of-Non-Communicable-Diseases-by-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 21 rows)

| Age Group | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka* | 0.085 | 0.082 | 0.101 | 0.025 | 0.008 | 0.001 | 0.004 | 0.006 | 0.018 | 0.003 |
| Less than 5 | 0.001 | 0.0 | 0.0 | 0.003 | 0.001 | 0.001 | 0.0 | 0.0 | 0.004 | 0.002 |
| 5-9 | 0.001 | 0.0 | 0.0 | 0.003 | 0.001 | 0.001 | 0.0 | 0.0 | 0.011 | 0.002 |
| 10-14 | 0.001 | 0.0 | 0.0 | 0.003 | 0.001 | 0.001 | 0.0 | 0.0 | 0.011 | 0.002 |
| 15-19 | 0.001 | 0.0 | 0.001 | 0.003 | 0.001 | 0.001 | 0.0 | 0.001 | 0.008 | 0.003 |
| 20-24 | 0.002 | 0.001 | 0.001 | 0.002 | 0.001 | 0.001 | 0.0 | 0.001 | 0.008 | 0.003 |
| 25-29 | 0.006 | 0.004 | 0.004 | 0.002 | 0.001 | 0.001 | 0.001 | 0.001 | 0.009 | 0.003 |
| 30-34 | 0.014 | 0.011 | 0.009 | 0.004 | 0.002 | 0.001 | 0.001 | 0.001 | 0.01 | 0.003 |
| 35-39 | 0.032 | 0.027 | 0.024 | 0.007 | 0.003 | 0.001 | 0.002 | 0.001 | 0.013 | 0.003 |
| 40-44 | 0.062 | 0.054 | 0.051 | 0.012 | 0.004 | 0.001 | 0.003 | 0.002 | 0.015 | 0.004 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka*",
    "P Diabetes": 0.085,
    "P High Cholesterol": 0.082,
    "P High Blood Pressure": 0.101,
    "P Heart Disease": 0.025,
    "P Kidney Disease": 0.008,
    "P Thalassemia": 0.001,
    "P Cancer": 0.004,
    "P Stroke": 0.006,
    "P Asthma": 0.018,
    "P Epilepsy": 0.003
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=144> (Table 6.3.7)

## 74. [Prevalence Rates of Non-Communicable Diseases by Broad Age Groups, 2024](data/final-report-tables/chapter-6/6.3.8-Prevalence-Rates-of-Non-Communicable-Diseases-by-Broad-Age-Groups,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age Group | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka* | 0.085 | 0.082 | 0.101 | 0.025 | 0.008 | 0.001 | 0.004 | 0.006 | 0.018 | 0.003 |
| 0 - 14 | 0.001 | 0.0 | 0.0 | 0.003 | 0.001 | 0.001 | 0.0 | 0.0 | 0.009 | 0.002 |
| 15 - 59 | 0.06 | 0.055 | 0.058 | 0.014 | 0.004 | 0.001 | 0.003 | 0.003 | 0.014 | 0.003 |
| 60 & Over | 0.268 | 0.27 | 0.364 | 0.084 | 0.028 | 0.001 | 0.012 | 0.023 | 0.043 | 0.003 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka*",
    "P Diabetes": 0.085,
    "P High Cholesterol": 0.082,
    "P High Blood Pressure": 0.101,
    "P Heart Disease": 0.025,
    "P Kidney Disease": 0.008,
    "P Thalassemia": 0.001,
    "P Cancer": 0.004,
    "P Stroke": 0.006,
    "P Asthma": 0.018,
    "P Epilepsy": 0.003
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=145> (Table 6.3.8)

## 75. [Prevalence Rates of Non-Communicable Diseases by Marital Status, 2024](data/final-report-tables/chapter-6/6.3.9-Prevalence-Rates-of-Non-Communicable-Diseases-by-Marital-Status,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Marital Status | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka* | 0.085 | 0.082 | 0.101 | 0.025 | 0.008 | 0.001 | 0.004 | 0.006 | 0.018 | 0.003 |
| Never Married | 0.008 | 0.007 | 0.009 | 0.004 | 0.002 | 0.001 | 0.001 | 0.001 | 0.009 | 0.004 |
| Married | 0.127 | 0.12 | 0.142 | 0.035 | 0.011 | 0.001 | 0.005 | 0.008 | 0.022 | 0.002 |
| Widowed | 0.27 | 0.295 | 0.404 | 0.075 | 0.022 | 0.001 | 0.012 | 0.021 | 0.048 | 0.003 |
| Divorced | 0.106 | 0.108 | 0.119 | 0.028 | 0.009 | 0.001 | 0.007 | 0.007 | 0.026 | 0.006 |
| Legally Separated | 0.101 | 0.108 | 0.116 | 0.028 | 0.009 | 0.001 | 0.008 | 0.007 | 0.028 | 0.006 |
| Separated (Not legally) | 0.102 | 0.107 | 0.124 | 0.033 | 0.012 | 0.001 | 0.008 | 0.008 | 0.036 | 0.007 |

### Example Data Row (JSON)

```json
{
    "Marital Status": "Sri Lanka*",
    "P Diabetes": 0.085,
    "P High Cholesterol": 0.082,
    "P High Blood Pressure": 0.101,
    "P Heart Disease": 0.025,
    "P Kidney Disease": 0.008,
    "P Thalassemia": 0.001,
    "P Cancer": 0.004,
    "P Stroke": 0.006,
    "P Asthma": 0.018,
    "P Epilepsy": 0.003
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=145> (Table 6.3.9)

## 76. [Prevalence Rates of Non-Communicable Diseases by Ethnic Group, 2024](data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 11 rows)

| Ethnicity | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka* | 0.085 | 0.082 | 0.101 | 0.025 | 0.008 | 0.001 | 0.004 | 0.006 | 0.018 | 0.003 |
| Sinhala | 0.086 | 0.087 | 0.105 | 0.026 | 0.008 | 0.001 | 0.004 | 0.006 | 0.017 | 0.003 |
| Sri Lanka Tamil | 0.08 | 0.072 | 0.088 | 0.021 | 0.007 | 0.001 | 0.003 | 0.006 | 0.03 | 0.004 |
| Indian Tamil/Malaiyaga  Thamilar | 0.046 | 0.035 | 0.085 | 0.024 | 0.005 | 0.001 | 0.003 | 0.009 | 0.024 | 0.006 |
| Sri Lanka Moor/ Muslim | 0.092 | 0.077 | 0.093 | 0.021 | 0.005 | 0.001 | 0.002 | 0.004 | 0.017 | 0.003 |
| Burgher | 0.107 | 0.1 | 0.122 | 0.031 | 0.006 | 0.001 | 0.005 | 0.006 | 0.019 | 0.002 |
| Malay | 0.115 | 0.104 | 0.138 | 0.03 | 0.007 | 0.001 | 0.004 | 0.005 | 0.017 | 0.003 |
| Sri Lanka Chetty | 0.078 | 0.095 | 0.105 | 0.021 | 0.006 | 0.001 | 0.003 | 0.007 | 0.015 | 0.003 |
| Bharatha | 0.096 | 0.089 | 0.104 | 0.024 | 0.004 | 0 | 0.002 | 0.007 | 0.012 | 0.001 |
| Veddas | 0.063 | 0.041 | 0.053 | 0.014 | 0.02 | 0.007 | 0.003 | 0.012 | 0.026 | 0.005 |

### Example Data Row (JSON)

```json
{
    "Ethnicity": "Sri Lanka*",
    "P Diabetes": 0.085,
    "P High Cholesterol": 0.082,
    "P High Blood Pressure": 0.101,
    "P Heart Disease": 0.025,
    "P Kidney Disease": 0.008,
    "P Thalassemia": 0.001,
    "P Cancer": 0.004,
    "P Stroke": 0.006,
    "P Asthma": 0.018,
    "P Epilepsy": 0.003
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=146> (Table 6.3.10)

## 77. [Prevalence Rates for the Population Aged 25 and Over by Highest Educational Qualification, 2024](data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Education | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Population aged 25 and over* | 0.133 | 0.129 | 0.158 | 0.037 | 0.012 | 0.001 | 0.006 | 0.009 | 0.024 | 0.003 |
| Never attended school | 0.177 | 0.178 | 0.275 | 0.062 | 0.024 | 0.002 | 0.01 | 0.031 | 0.065 | 0.015 |
| Studied/ Studying at the special  school/special educational unit | 0.08 | 0.06 | 0.068 | 0.019 | 0.006 | 0.002 | 0.002 | 0.011 | 0.016 | 0.036 |
| Passed grade 1 - 5 | 0.201 | 0.209 | 0.287 | 0.069 | 0.027 | 0.001 | 0.01 | 0.022 | 0.054 | 0.006 |
| Passed grade 6 - 8 | 0.183 | 0.183 | 0.231 | 0.059 | 0.02 | 0.001 | 0.009 | 0.015 | 0.036 | 0.005 |
| Passed grade 9 - 10 | 0.121 | 0.117 | 0.137 | 0.033 | 0.01 | 0.001 | 0.006 | 0.007 | 0.022 | 0.003 |
| G.C.E. (O/L) or equal | 0.124 | 0.117 | 0.135 | 0.031 | 0.008 | 0.001 | 0.005 | 0.005 | 0.016 | 0.002 |
| G.C.E. (A/L) or equal | 0.097 | 0.089 | 0.1 | 0.02 | 0.005 | 0.001 | 0.004 | 0.003 | 0.009 | 0.001 |
| Degree & above | 0.074 | 0.065 | 0.07 | 0.013 | 0.003 | 0.0 | 0.002 | 0.002 | 0.006 | 0.001 |

### Example Data Row (JSON)

```json
{
    "Education": "Population aged 25 and over*",
    "P Diabetes": 0.133,
    "P High Cholesterol": 0.129,
    "P High Blood Pressure": 0.158,
    "P Heart Disease": 0.037,
    "P Kidney Disease": 0.012,
    "P Thalassemia": 0.001,
    "P Cancer": 0.006,
    "P Stroke": 0.009,
    "P Asthma": 0.024,
    "P Epilepsy": 0.003
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=147> (Table 6.3.11)

## 78. [Prevalence Rates of NCDs by Employment Status, 2024](data/final-report-tables/chapter-6/6.3.12-Prevalence-Rates-of-NCDs-by-Employment-Status,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Employment Status | P Diabetes | P High Cholesterol | P High Blood Pressure | P Heart Disease | P Kidney Disease | P Thalassemia | P Cancer | P Stroke | P Asthma | P Epilepsy |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Employed population aged 15  and over | 0.078 | 0.071 | 0.079 | 0.021 | 0.006 | 0.001 | 0.002 | 0.002 | 0.015 | 0.002 |
| Government paid employee | 0.061 | 0.055 | 0.053 | 0.011 | 0.003 | 0.0 | 0.002 | 0.001 | 0.007 | 0.001 |
| Semi government paid  employee | 0.076 | 0.069 | 0.065 | 0.015 | 0.003 | 0.0 | 0.002 | 0.001 | 0.009 | 0.001 |
| Paid employee (private sector) | 0.058 | 0.052 | 0.058 | 0.016 | 0.004 | 0.001 | 0.002 | 0.001 | 0.015 | 0.003 |
| Employer (have employees) | 0.138 | 0.11 | 0.105 | 0.028 | 0.005 | 0.0 | 0.002 | 0.002 | 0.009 | 0.001 |
| Own account worker   (don't have employees) | 0.104 | 0.096 | 0.11 | 0.032 | 0.011 | 0.001 | 0.003 | 0.003 | 0.02 | 0.003 |
| Contributing to family enterprise  (unpaid family worker) | 0.096 | 0.107 | 0.134 | 0.028 | 0.011 | 0.001 | 0.004 | 0.002 | 0.025 | 0.003 |

### Example Data Row (JSON)

```json
{
    "Employment Status": "Employed population aged 15  and over",
    "P Diabetes": 0.078,
    "P High Cholesterol": 0.071,
    "P High Blood Pressure": 0.079,
    "P Heart Disease": 0.021,
    "P Kidney Disease": 0.006,
    "P Thalassemia": 0.001,
    "P Cancer": 0.002,
    "P Stroke": 0.002,
    "P Asthma": 0.015,
    "P Epilepsy": 0.002
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=148> (Table 6.3.12)

## 79. [Population Aged 3 Years and Over by Sex and Educational Activity During the Census Reference Period,](data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Null | Male | Female | Total Value |
| :-- | :-- | :-- | :-- |
| Preschool education | 243648 | 238458 | 482106 |
| School education | 2157831 | 2193394 | 4351225 |
| Degree/Postgraduate education | 120745 | 200244 | 320989 |
| Vocational training/Technical education | 70149 | 52308 | 122457 |
| Other educational activity | 125671 | 140742 | 266413 |
| Not studying | 7469270 | 8122199 | 15591469 |

### Example Data Row (JSON)

```json
{
    "Null": "Preschool education",
    "Male": 243648,
    "Female": 238458,
    "Total Value": 482106
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=149> (Table 7.1)

## 80. [Percentage Pistribution of Population Aged 03 Years and Over by Educational Activity and Age Group, 2024](data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age Group | P Pre School | P School Education | P Undergraduate Or Postgraduate Education | P Vocational Training Or Technical Education | P Other Educational Activity | P Not Studying |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 3 - 4 | 0.422 | 0.0 | 0.0 | 0.0 | 0.001 | 0.577 |
| 5 -14 | 0.074 | 0.884 | 0.0 | 0.0 | 0.007 | 0.035 |
| 15 -18 | 0.0 | 0.794 | 0.003 | 0.01 | 0.023 | 0.17 |
| 19 - 24 | 0.0 | 0.151 | 0.109 | 0.042 | 0.059 | 0.639 |
| 25 and over | 0.0 | 0.0 | 0.008 | 0.002 | 0.007 | 0.983 |

### Example Data Row (JSON)

```json
{
    "Age Group": "3 - 4",
    "P Pre School": 0.422,
    "P School Education": 0.0,
    "P Undergraduate Or Postgraduate Education": 0.0,
    "P Vocational Training Or Technical Education": 0.0,
    "P Other Educational Activity": 0.001,
    "P Not Studying": 0.577
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=150> (Table 7.2)

## 81. [Children Enrolled in Pre-school Education During the Reference Period by Age, 2024](data/final-report-tables/chapter-7/7.3-Children-Enrolled-in-Pre-school-Education-During-the-Reference-Period-by-Age,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age | Total Population | Pre School Population | P Preschool |
| :-- | :-- | :-- | :-- |
| 3 years | 276648 | 53785 | 0.194 |
| 4 years | 291331 | 185644 | 0.637 |
| 5 years | 302414 | 235434 | 0.779 |
| 6 years | 312159 | 7243 | 0.023 |

### Example Data Row (JSON)

```json
{
    "Age": "3 years",
    "Total Population": 276648,
    "Pre School Population": 53785,
    "P Preschool": 0.194
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=150> (Table 7.3)

## 82. [Percentage of Children Receiving Preschool Education by Age Group and District, 2024](data/final-report-tables/chapter-7/7.4-Percentage-of-Children-Receiving-Preschool-Education-by-Age-Group-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | P 3 Years | P 4 Years | P 5 Years | P 6 Years |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 0.411 | 0.82 | 0.669 | 0.032 |
| LK-12 | Gampaha | district | 0.347 | 0.824 | 0.718 | 0.026 |
| LK-13 | Kalutara | district | 0.233 | 0.786 | 0.777 | 0.025 |
| LK-21 | Kandy | district | 0.118 | 0.535 | 0.783 | 0.02 |
| LK-22 | Matale | district | 0.099 | 0.555 | 0.808 | 0.021 |
| LK-23 | Nuwara Eliya | district | 0.239 | 0.659 | 0.753 | 0.031 |
| LK-31 | Galle | district | 0.141 | 0.663 | 0.804 | 0.021 |
| LK-32 | Matara | district | 0.121 | 0.603 | 0.829 | 0.014 |
| LK-33 | Hambantota | district | 0.086 | 0.491 | 0.8 | 0.017 |
| LK-41 | Jaffna | district | 0.409 | 0.846 | 0.838 | 0.028 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "P 3 Years": 0.411,
    "P 4 Years": 0.82,
    "P 5 Years": 0.669,
    "P 6 Years": 0.032
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=151> (Table 7.4)

## 83. [Population Engaged in School Education During the Reference Period by Age Group and Sex,](data/final-report-tables/chapter-7/7.5-Population-Engaged-in-School-Education-During-the-Reference-Period-by-Age-Group-and-Sex,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Null | Total | Total In School | Male | Male In School | Female | Female In School |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 05 - 10 | 1893872 | 1578999 | 959815 | 799153 | 934057 | 779846 |
| 11 - 14 | 1397847 | 1329915 | 709634 | 672962 | 688213 | 656953 |
| 15 - 16 | 720137 | 658982 | 365655 | 331356 | 354482 | 327626 |
| 17 - 18 | 726524 | 488622 | 367328 | 225986 | 359196 | 262636 |
| 19 - 24 | 1956983 | 294707 | 964971 | 128374 | 992012 | 166333 |

### Example Data Row (JSON)

```json
{
    "Null": "05 - 10",
    "Total": 1893872,
    "Total In School": 1578999,
    "Male": 959815,
    "Male In School": 799153,
    "Female": 934057,
    "Female In School": 779846
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=152> (Table 7.5)

## 84. [The Educational Level of the Population Age 25 Years and Over by Sex, 2012 and 2024](data/final-report-tables/chapter-7/7.6-The-Educational-Level-of-the-Population-Age-25-Years-and-Over-by-Sex,-2012-and-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Educational level | 2012 |  | 2024 |  | 2012 |  | 2024 |  | 2012 |  | 2024 |  |
|  | Number | (%) | Number | (%) | Number | (%) | Number | (%) | Number | (%) | Number | (%) |
| Population 25 years and over | 12,050,641 | 100.0 | 13,871,317 | 100.0 | 5,703,991 | 100.0 | 6,533,860 | 100.0 | 6,346,650 | 100.0 | 7,337,457 | 100.0 |
| No schooling | 561,163 | 4.7 | 400,511 | 2.9 | 172,292 | 3.0 | 136,168 | 2.1 | 388,871 | 6.1 | 264,343 | 3.6 |
| Primary educational level | 2,214,792 | 18.4 | 1,738,942 | 12.5 | 1,058,900 | 18.6 | 794,197 | 12.2 | 1,155,892 | 18.2 | 944,745 | 12.9 |
| Passed Grades 1- 5* | 2,214,792 | 18.4 | 1738942 | 12.5 | 1,058,900 | 18.6 | 794,197 | 12.2 | 1,155,892 | 18.2 | 944,745 | 12.9 |
| Secondary educational level | 7,079,569 | 58.7 | 8,096,402 | 58.4 | 3,499,694 | 61.4 | 4,025,986 | 61.6 | 3,579,875 | 56.4 | 4,070,416 | 55.5 |
| Passed Grades 6 - 8 | 1,889,721 | 15.7 | 1,655,756 | 11.9 | 991,099 | 17.4 | 848,236 | 13.0 | 898,622 | 14.2 | 807,520 | 11.0 |
| Passed Grades 9 - 10 | 2,886,830 | 23.9 | 3,385,775 | 24.5 | 1,407,833 | 24.7 | 1,692,481 | 25.9 | 1,478,997 | 23.3 | 1,693,294 | 23.1 |
| G.C.E. O/L or equivalent | 2,303,018 | 19.1 | 3,054,871 | 22.0 | 1,100,762 | 19.3 | 1,485,269 | 22.7 | 1,202,256 | 18.9 | 1,569,602 | 21.4 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=153> (Table 7.6)

## 85. [Percentage Distribution of Population Aged 25 and Over by Educational Level and District, 2012 and 2024](data/final-report-tables/chapter-7/7.7-Percentage-Distribution-of-Population-Aged-25-and-Over-by-Educational-Level-and-District,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Total 2012 | Total 2024 | P No Schooling 2012 | P No Schooling 2024 | P Passed 1 5 Years 2012 | P Passed 1 5 Years 2024 | P Passed 6 10 Years 2012 | P Passed 6 10 Years 2024 | P Gce Ol 2012 | P Gce Ol 2024 | P Gce Al 2012 | P Gce Al 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 1450574 | 1601927 | 0.026 | 0.016 | 0.096 | 0.058 | 0.332 | 0.266 | 0.253 | 0.259 | 0.294 | 0.401 |
| LK-12 | Gampaha | district | 1419483 | 1620233 | 0.018 | 0.011 | 0.097 | 0.061 | 0.408 | 0.332 | 0.252 | 0.271 | 0.226 | 0.325 |
| LK-13 | Kalutara | district | 748643 | 847732 | 0.031 | 0.018 | 0.145 | 0.094 | 0.4 | 0.366 | 0.224 | 0.238 | 0.2 | 0.284 |
| LK-21 | Kandy | district | 814087 | 922349 | 0.053 | 0.03 | 0.167 | 0.11 | 0.373 | 0.324 | 0.196 | 0.233 | 0.211 | 0.303 |
| LK-22 | Matale | district | 288729 | 332816 | 0.057 | 0.035 | 0.216 | 0.151 | 0.419 | 0.409 | 0.16 | 0.195 | 0.148 | 0.21 |
| LK-23 | Nuwara Eliya | district | 410561 | 442909 | 0.102 | 0.083 | 0.315 | 0.225 | 0.356 | 0.365 | 0.135 | 0.181 | 0.092 | 0.146 |
| LK-31 | Galle | district | 636778 | 711223 | 0.039 | 0.023 | 0.176 | 0.118 | 0.413 | 0.381 | 0.187 | 0.21 | 0.186 | 0.268 |
| LK-32 | Matara | district | 486477 | 537436 | 0.056 | 0.032 | 0.189 | 0.127 | 0.397 | 0.382 | 0.183 | 0.208 | 0.175 | 0.251 |
| LK-33 | Hambantota | district | 351758 | 421054 | 0.061 | 0.032 | 0.219 | 0.145 | 0.414 | 0.399 | 0.165 | 0.215 | 0.14 | 0.209 |
| LK-41 | Jaffna | district | 333896 | 383511 | 0.014 | 0.007 | 0.214 | 0.134 | 0.435 | 0.422 | 0.18 | 0.199 | 0.157 | 0.238 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total 2012": 1450574,
    "Total 2024": 1601927,
    "P No Schooling 2012": 0.026,
    "P No Schooling 2024": 0.016,
    "P Passed 1 5 Years 2012": 0.096,
    "P Passed 1 5 Years 2024": 0.058,
    "P Passed 6 10 Years 2012": 0.332,
    "P Passed 6 10 Years 2024": 0.266,
    "P Gce Ol 2012": 0.253,
    "P Gce Ol 2024": 0.259,
    "P Gce Al 2012": 0.294,
    "P Gce Al 2024": 0.401
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=154> (Table 7.7)

## 86. [Language Literacy Rate by Census Year and Sex, 2024](data/final-report-tables/chapter-7/7.8-Language-Literacy-Rate-by-Census-Year-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 13 rows)

| Null | P Total Literacy Rate | P Male Literacy Rate | P Female Literacy Rate |
| :-- | :-- | :-- | :-- |
| 1881 | 0.174 | 0.298 | 0.031 |
| 1891 | 0.217 | 0.361 | 0.053 |
| 1901 | 0.264 | 0.42 | 0.085 |
| 1911 | 0.31 | 0.472 | 0.125 |
| 1921 | 0.399 | 0.563 | 0.212 |
| 1946 | 0.578 | 0.701 | 0.438 |
| 1953 | 0.654 | 0.759 | 0.536 |
| 1963 | 0.771 | 0.858 | 0.675 |
| 1971 | 0.785 | 0.856 | 0.709 |
| 1981 | 0.872 | 0.911 | 0.832 |

### Example Data Row (JSON)

```json
{
    "Null": "1881",
    "P Total Literacy Rate": 0.174,
    "P Male Literacy Rate": 0.298,
    "P Female Literacy Rate": 0.031
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=155> (Table 7.8)

## 87. [Language Literacy Rate by Language and Age Group, 2024](data/final-report-tables/chapter-7/7.9-Language-Literacy-Rate-by-Language-and-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Null | P Sinhala Literacy Rate | P Tamil Literacy Rate | P English Literacy Rate |
| :-- | :-- | :-- | :-- |
| Sri Lanka | 0.852 | 0.453 | 0.573 |
| 10-14 | 0.859 | 0.635 | 0.706 |
| 15-19 | 0.872 | 0.627 | 0.791 |
| 20-29 | 0.861 | 0.544 | 0.736 |
| 30-39 | 0.861 | 0.47 | 0.635 |
| 40-49 | 0.86 | 0.409 | 0.539 |
| 50-59 | 0.848 | 0.361 | 0.456 |
| 60 and above | 0.823 | 0.308 | 0.35 |

### Example Data Row (JSON)

```json
{
    "Null": "Sri Lanka",
    "P Sinhala Literacy Rate": 0.852,
    "P Tamil Literacy Rate": 0.453,
    "P English Literacy Rate": 0.573
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=156> (Table 7.9)

## 88. [Language Literacy Rate by Language and District, 2024](data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Population 10 And Over | P Literacy At Least One Language | P Literacy Sinhala | P Literacy Tamil | P Literacy English |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2139371 | 0.986 | 0.941 | 0.415 | 0.742 |
| LK-12 | Gampaha | district | 2169227 | 0.989 | 0.971 | 0.329 | 0.672 |
| LK-13 | Kalutara | district | 1151651 | 0.985 | 0.96 | 0.366 | 0.625 |
| LK-21 | Kandy | district | 1275003 | 0.975 | 0.909 | 0.501 | 0.648 |
| LK-22 | Matale | district | 456498 | 0.967 | 0.914 | 0.424 | 0.548 |
| LK-23 | Nuwara Eliya | district | 623842 | 0.936 | 0.595 | 0.68 | 0.471 |
| LK-31 | Galle | district | 962957 | 0.978 | 0.97 | 0.298 | 0.594 |
| LK-32 | Matara | district | 732282 | 0.971 | 0.961 | 0.281 | 0.553 |
| LK-33 | Hambantota | district | 577879 | 0.972 | 0.968 | 0.288 | 0.52 |
| LK-41 | Jaffna | district | 520973 | 0.983 | 0.171 | 0.979 | 0.41 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population 10 And Over": 2139371,
    "P Literacy At Least One Language": 0.986,
    "P Literacy Sinhala": 0.941,
    "P Literacy Tamil": 0.415,
    "P Literacy English": 0.742
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=157> (Table 7.10)

## 89. [Language Literacy Rate by Language and Ethnic Group, 2012 and 2024](data/final-report-tables/chapter-7/7.11-Language-Literacy-Rate-by-Language-and-Ethnic-Group,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Null | P Sinhala Literacy Rate 2012 | P Sinhala Literacy Rate 2024 | P Tamil Literacy Rate 2012 | P Tamil Literacy Rate 2024 | P English Literacy Rate 2012 | P English Literacy Rate 2024 | P At Least One Literacy Rate 2012 | P At Least One Literacy Rate 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 0.797 | 0.852 | 0.264 | 0.453 | 0.308 | 0.573 | 0.957 | 0.974 |
| Sinhala | 0.964 | 0.978 | 0.053 | 0.292 | 0.311 | 0.586 | 0.965 | 0.981 |
| Sri Lanka Tamil | 0.173 | 0.363 | 0.941 | 0.94 | 0.243 | 0.452 | 0.943 | 0.956 |
| Indian Tamil/Malaiyaga Thamilar | 0.209 | 0.408 | 0.862 | 0.9 | 0.194 | 0.446 | 0.864 | 0.911 |
| Sri Lanka Moor/Muslim | 0.406 | 0.625 | 0.948 | 0.945 | 0.387 | 0.654 | 0.95 | 0.968 |
| Burgher | 0.77 | 0.818 | 0.291 | 0.538 | 0.974 | 0.793 | 0.982 | 0.98 |
| Malay | 0.818 | 0.927 | 0.971 | 0.709 | 0.668 | 0.854 | 0.976 | 0.981 |
| Other | 0.541 | 0.561 | 0.383 | 0.331 | 0.808 | 0.702 | 0.95 | 0.899 |

### Example Data Row (JSON)

```json
{
    "Null": "Sri Lanka",
    "P Sinhala Literacy Rate 2012": 0.797,
    "P Sinhala Literacy Rate 2024": 0.852,
    "P Tamil Literacy Rate 2012": 0.264,
    "P Tamil Literacy Rate 2024": 0.453,
    "P English Literacy Rate 2012": 0.308,
    "P English Literacy Rate 2024": 0.573,
    "P At Least One Literacy Rate 2012": 0.957,
    "P At Least One Literacy Rate 2024": 0.974
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=158> (Table 7.11)

## 90. [Computer and Digital Literacy Rate by Sector,2024](data/final-report-tables/chapter-7/7.12-Computer-and-Digital-Literacy-Rate-by-Sector,2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Computer Literacy Rate | Digital Literacy Rate |
| :-- | :-- | :-- |
| Sri Lanka | 34.7 | 67.6 |
| Urban* | 47.0 | 76.8 |
| Rural | 33.0 | 66.4 |
| Estate Rural** | 14.9 | 50.2 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "Computer Literacy Rate": 34.7,
    "Digital Literacy Rate": 67.6
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=159> (Table 7.12)

## 91. [Computer and Digital Literacy Rate by District, 2024](data/final-report-tables/chapter-7/7.13-Computer-and-Digital-Literacy-Rate-by-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Population Aged 5 And Over | Computer Literacy Rate | Digital Literacy Rate |
| :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2271290 | 51.0 | 78.7 |
| LK-12 | Gampaha | district | 2319190 | 42.7 | 73.7 |
| LK-13 | Kalutara | district | 1239745 | 37.1 | 69.1 |
| LK-21 | Kandy | district | 1382499 | 38.5 | 69.0 |
| LK-22 | Matale | district | 496910 | 31.4 | 65.7 |
| LK-23 | Nuwara Eliya | district | 680431 | 23.9 | 56.4 |
| LK-31 | Galle | district | 1039455 | 36.1 | 67.1 |
| LK-32 | Matara | district | 792812 | 35.0 | 65.9 |
| LK-33 | Hambantota | district | 631619 | 30.1 | 64.1 |
| LK-41 | Jaffna | district | 559228 | 29.0 | 66.5 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Population Aged 5 And Over": 2271290,
    "Computer Literacy Rate": 51.0,
    "Digital Literacy Rate": 78.7
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=159> (Table 7.13)

## 92. [Computer and Digital Literacy Rate by Age Group,](data/final-report-tables/chapter-7/7.14-Computer-and-Digital-Literacy-Rate-by-Age-Group,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 12 rows)

| Null | Population Aged 5 Or Over | P Computer Literacy Rate | P Digital Literacy Rate |
| :-- | :-- | :-- | :-- |
| Sri Lanka | 20566680 | 0.347 | 0.676 |
| 5-9 | 1556523 | 0.119 | 0.399 |
| 10-14 | 1735196 | 0.412 | 0.881 |
| 15-19 | 1795038 | 0.643 | 0.97 |
| 20-24 | 1608606 | 0.655 | 0.948 |
| 25-29 | 1372458 | 0.577 | 0.93 |
| 30-34 | 1414060 | 0.482 | 0.902 |
| 35-39 | 1452703 | 0.418 | 0.86 |
| 40-49 | 1602344 | 0.338 | 0.75 |
| 50-59 | 1490765 | 0.25 | 0.544 |

### Example Data Row (JSON)

```json
{
    "Null": "Sri Lanka",
    "Population Aged 5 Or Over": 20566680,
    "P Computer Literacy Rate": 0.347,
    "P Digital Literacy Rate": 0.676
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=160> (Table 7.14)

## 93. [Economically Active and Inactive Population by Sex, 2024](data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sex | Economically Active | Economically Inactive | Total Value |
| :-- | :-- | :-- | :-- |
| Male | 5550374 | 2681440 | 8231814 |
| Female | 2612567 | 6430580 | 9043147 |

### Example Data Row (JSON)

```json
{
    "Sex": "Male",
    "Economically Active": 5550374,
    "Economically Inactive": 2681440,
    "Total Value": 8231814
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=163> (Table 8.1)

## 94. [Economically Active Population, by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.2-Economically-Active-Population,-by-Sector-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Economically Active | Economically Inactive | Total Value |
| :-- | :-- | :-- | :-- |
| Urban | 943483 | 438711 | 1382194 |
| Estate - Urban | 3176 | 1689 | 4865 |
| Rural | 4395189 | 2046141 | 6441330 |
| Estate - Rural | 208526 | 126026 | 334552 |

### Example Data Row (JSON)

```json
{
    "Sector": "Urban",
    "Economically Active": 943483,
    "Economically Inactive": 438711,
    "Total Value": 1382194
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=164> (Table 8.2)

## 95. [Economically Active Population by Sex and Age Group, 2024](data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 14 rows)

| Age Group | Male Economically Active | Female Economically Active | Total Value |
| :-- | :-- | :-- | :-- |
| Sri Lanka | 5550374 | 2612567 | 8162941 |
| 15 - 19 | 105358 | 44085 | 149443 |
| 20 - 24 | 431002 | 229585 | 660587 |
| 25 - 29 | 548881 | 289710 | 838591 |
| 30 - 34 | 627056 | 298652 | 925708 |
| 35 - 39 | 658779 | 311866 | 970645 |
| 40 - 44 | 729822 | 344964 | 1074786 |
| 45 - 49 | 666969 | 322647 | 989616 |
| 50 - 54 | 577876 | 275996 | 853872 |
| 55 - 59 | 489343 | 228097 | 717440 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Sri Lanka",
    "Male Economically Active": 5550374,
    "Female Economically Active": 2612567,
    "Total Value": 8162941
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=165> (Table 8.3)

## 96. [Labour Force Participation Rate by Age Group and Sex, 2024](data/final-report-tables/chapter-8/8.4-Labour-Force-Participation-Rate-by-Age-Group-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 14 rows)

| Age Group | P Total Labour Force Participation Rate | P Male Labour Force Participation Rate | P Female Labour Force Participation Rate |
| :-- | :-- | :-- | :-- |
| Aged 15 & over | 0.473 | 0.674 | 0.289 |
| 15 - 19 | 0.083 | 0.116 | 0.05 |
| 20 - 24 | 0.411 | 0.545 | 0.281 |
| 25 - 29 | 0.611 | 0.828 | 0.408 |
| 30 - 34 | 0.655 | 0.919 | 0.408 |
| 35 - 39 | 0.668 | 0.934 | 0.417 |
| 40 - 44 | 0.671 | 0.929 | 0.423 |
| 45 - 49 | 0.664 | 0.913 | 0.424 |
| 50 - 54 | 0.636 | 0.888 | 0.4 |
| 55 - 59 | 0.562 | 0.811 | 0.339 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Aged 15 & over",
    "P Total Labour Force Participation Rate": 0.473,
    "P Male Labour Force Participation Rate": 0.674,
    "P Female Labour Force Participation Rate": 0.289
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=166> (Table 8.4)

## 97. [Labour Force Participation Rate, by Highest Educational Qualification Attained and Sex, 2024](data/final-report-tables/chapter-8/8.5-Labour-Force-Participation-Rate,-by-Highest-Educational-Qualification-Attained-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Level Of Education | P Male Labour Force Participation Rate | P Female Labour Force Participation Rate |
| :-- | :-- | :-- |
| Never attended School | 0.486 | 0.192 |
| Studied in a special school/special unit | 0.251 | 0.223 |
| Passed Grade 1 - 5 | 0.623 | 0.206 |
| Passed Grade 6 - 8 | 0.701 | 0.221 |
| Passed Grade 9 - 10 | 0.696 | 0.247 |
| Passed GCE O/L | 0.651 | 0.229 |
| Passed GCE A/L | 0.678 | 0.351 |
| Degree or above | 0.776 | 0.73 |

### Example Data Row (JSON)

```json
{
    "Level Of Education": "Never attended School",
    "P Male Labour Force Participation Rate": 0.486,
    "P Female Labour Force Participation Rate": 0.192
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=167> (Table 8.5)

## 98. [Employed Population by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Male | Female | Total Value |
| :-- | :-- | :-- | :-- |
| Urban | 900141 | 393746 | 1293887 |
| Estate - Urban | 3025 | 1577 | 4602 |
| Rural | 4220045 | 1847052 | 6067097 |
| Estate - Rural | 194492 | 111154 | 305646 |

### Example Data Row (JSON)

```json
{
    "Sector": "Urban",
    "Male": 900141,
    "Female": 393746,
    "Total Value": 1293887
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=168> (Table 8.6)

## 99. [Employed Population, by Highest Educational Attainment and Sex, 2024](data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Educational Level | Male | Female | Total Value |
| :-- | :-- | :-- | :-- |
| Never attended School | 67915 | 49378 | 117293 |
| Studied in a special school / special unit | 3923 | 2719 | 6642 |
| Passed Grade 1 - 5 | 493163 | 183967 | 677130 |
| Passed Grade 6 - 8 | 618673 | 171412 | 790085 |
| Passed Grade 9 - 10 | 1536837 | 486618 | 2023455 |
| Passed GCE O/L | 1288859 | 430468 | 1719327 |
| Passed GCE A/L | 982912 | 621725 | 1604637 |
| Degree or above | 325421 | 407242 | 732663 |

### Example Data Row (JSON)

```json
{
    "Educational Level": "Never attended School",
    "Male": 67915,
    "Female": 49378,
    "Total Value": 117293
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=169> (Table 8.7)

## 100. [Employed Population by Employment Status and Sex, 2024](data/final-report-tables/chapter-8/8.8-Employed-Population-by-Employment-Status-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Employment Status | Male | Female | Total Value |
| :-- | :-- | :-- | :-- |
| Government/Semi-Government Paid Employee | 741649 | 591757 | 1333406 |
| Private Sector Paid Employee | 2248841 | 995932 | 3244773 |
| Employer | 242488 | 35380 | 277868 |
| Own Account Worker | 1906739 | 500875 | 2407614 |
| Contributing to Family Enterprise | 177986 | 229585 | 407571 |

### Example Data Row (JSON)

```json
{
    "Employment Status": "Government/Semi-Government Paid Employee",
    "Male": 741649,
    "Female": 591757,
    "Total Value": 1333406
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=170> (Table 8.8)

## 101. [Unemployed Population by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Male | Female | Total Value |
| :-- | :-- | :-- | :-- |
| Urban | 43342 | 44965 | 88307 |
| Estate - Urban | 151 | 112 | 263 |
| Rural | 175144 | 199089 | 374233 |
| Estate - Rural | 14034 | 14872 | 28906 |

### Example Data Row (JSON)

```json
{
    "Sector": "Urban",
    "Male": 43342,
    "Female": 44965,
    "Total Value": 88307
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=171> (Table 8.9)

## 102. [Employment Rate and Unemployment Rate by District, 2024](data/final-report-tables/chapter-8/8.10-Employment-Rate-and-Unemployment-Rate-by-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Employed | Unemployed | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 867111 | 53635 | 920746 |
| LK-12 | Gampaha | district | 889380 | 52943 | 942323 |
| LK-13 | Kalutara | district | 462465 | 26157 | 488622 |
| LK-21 | Kandy | district | 477418 | 35467 | 512885 |
| LK-22 | Matale | district | 186449 | 10062 | 196511 |
| LK-23 | Nuwara Eliya | district | 251699 | 25234 | 276933 |
| LK-31 | Galle | district | 389323 | 23061 | 412384 |
| LK-32 | Matara | district | 300965 | 18307 | 319272 |
| LK-33 | Hambantota | district | 221480 | 16993 | 238473 |
| LK-41 | Jaffna | district | 183239 | 13246 | 196485 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Employed": 867111,
    "Unemployed": 53635,
    "Total Value": 920746
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=172> (Table 8.10)

## 103. [Economically Inactive Population by Main Reason for Inactivity, 2024](data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Reason For Being Inactive | Population |
| :-- | :-- |
| Engaged in Household work/Childcare/Elder Care | 3358527 |
| Engage in educational/Vocational training | 2365048 |
| Unable/Too old to work/Retired | 2190230 |
| Long term illness/Disabled | 517647 |
| Does not want/interest to do any economic activity | 447121 |
| Other | 173895 |
| Income Recipient such as from investment, rental and interest | 59552 |

### Example Data Row (JSON)

```json
{
    "Reason For Being Inactive": "Engaged in Household work/Childcare/Elder Care",
    "Population": 3358527
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=174> (Table 8.11)

## 104. [by Marital Status, Age Group, and Sex, 2024](data/final-report-tables/chapter-9/9.1-by-Marital-Status,-Age-Group,-and-Sex,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 | Col 13 | Col 14 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  |  |  |  |  | Marital status |  |  |  |  |  |  |
| Age Group | Population |  |  |  |  |  |  |  |  |  | Separated |  | Separated |  |
|  |  |  | Never married |  | Married |  | Widowed |  | Divorced |  | (Legally) |  | (Not legally) |  |
|  | Male | Female | Male | Female | Male | Female | Male | Female | Male | Female | Male | Female | Male | Female |
| Total | 10,512,344 | 11,269,456 | 4,808,324 | 4,291,826 | 5,417,431 | 5,743,647 | 175,421 | 1,058,997 | 28,952 | 45,403 | 17,047 | 27,857 | 65,169 | 101,726 |
| Less than 15 | 2,280,530 | 2,226,309 | 2,280,530 | 2226291 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|  | 100.0 | 100.0 | 100.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 15-19 | 907,739 | 887,299 | 899,119 | 856,574 | 8,458 | 30,199 | 69 | 78 | 15 | 106 | 10 | 31 | 68 | 311 |
|  | 100.0 | 100.0 | 99.1 | 96.6 | 0.9 | 3.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 20-24 | 790,215 | 818,391 | 703,705 | 613,975 | 84,787 | 198,888 | 166 | 697 | 341 | 1,082 | 210 | 660 | 1,006 | 3,089 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=176> (Table 9.1)

## 105. [Marital Status by Ethnic group and Sex,](data/final-report-tables/chapter-9/9.2-Marital-Status-by-Ethnic-group-and-Sex,)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Marital Status by Ethnic Group |  |  |  |  |  |  |  |  |
| Table 9.2 shows the distribution of the population by ethnic group, sex, and marital status. |  |  |  |  |  |  |  |  |
|  |  | Table 9.2 : Marital Status by Ethnic group and Sex, 2024 |  |  |  |  |  |  |
| Ethnic group | Male/ 
Female | Total | Never 
Married | Married | Widowed | Divorced | Separated 
(Legally) | Separated  
(Not legally) |
|  | Grand | 21,781,800 | 9,100,150 | 11,161,078 | 1,234,418 | 74,355 | 44,904 | 166,895 |
|  | Total | 100.0 | 41.8 | 51.2 | 5.7 | 0.3 | 0.2 | 0.8 |
| Sri Lanka | Male | 10,512,344 | 4,808,324 | 5,417,431 | 175,421 | 28,952 | 17,047 | 65,169 |
|  |  | 100.0 | 45.7 | 51.5 | 1.7 | 0.3 | 0.2 | 0.6 |
|  | Female | 11,269,456 | 4,291,826 | 5,743,647 | 1,058,997 | 45,403 | 27,857 | 101,726 |
|  |  | 100.0 | 38.1 | 51.0 | 9.4 | 0.4 | 0.2 | 0.9 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=177> (Table 9.2)

## 106. [Population Aged 15 Years and Over by Marital Status and Sex, 2012 and 2024](data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Marital Status | 2012 Male | P 2012 Male | 2012 Female | P 2012 Female | 2024 Male | P 2024 Male | 2024 Female | P 2024 Female |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Married | 4921044 | 0.677 | 5401061 | 0.679 | 5417431 | 0.658 | 5743629 | 0.636 |
| Widow | 97532 | 0.013 | 695415 | 0.087 | 175421 | 0.021 | 1058997 | 0.117 |
| Divorced | 14847 | 0.002 | 26328 | 0.003 | 28952 | 0.004 | 45403 | 0.005 |
| Legal separated | 11135 | 0.002 | 19778 | 0.002 | 17047 | 0.002 | 27857 | 0.003 |
| Separated (not legally) | 42577 | 0.006 | 70454 | 0.009 | 65169 | 0.008 | 101726 | 0.011 |

### Example Data Row (JSON)

```json
{
    "Marital Status": "Married",
    "2012 Male": 4921044,
    "P 2012 Male": 0.677,
    "2012 Female": 5401061,
    "P 2012 Female": 0.679,
    "2024 Male": 5417431,
    "P 2024 Male": 0.658,
    "2024 Female": 5743629,
    "P 2024 Female": 0.636
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=178> (Table 9.3)

## 107. [Percentage of Never-Married Persons within the Age Group by Sex, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.4-Percentage-of-Never-Married-Persons-within-the-Age-Group-by-Sex,-1981,-2012,-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 12 rows)

| Age Group | P Never Married Male 1981 | P Never Married Male 2012 | P Never Married Male 2024 | P Never Married Female 1981 | P Never Married Female 2012 | P Never Married Female 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Population 15 Years and Over | 0.425 | 0.3 | 0.307 | 0.324 | 0.22 | 0.228 |
| 15-19 | 0.99 | 0.977 | 0.991 | 0.901 | 0.894 | 0.965 |
| 20-24 | 0.835 | 0.813 | 0.891 | 0.553 | 0.568 | 0.75 |
| 25-29 | 0.515 | 0.479 | 0.606 | 0.304 | 0.244 | 0.363 |
| 30-34 | 0.249 | 0.203 | 0.28 | 0.158 | 0.102 | 0.1 |
| 35-39 | 0.126 | 0.095 | 0.139 | 0.089 | 0.067 | 0.046 |
| 40-44 | 0.083 | 0.067 | 0.086 | 0.059 | 0.057 | 0.034 |
| 45-49 | 0.069 | 0.058 | 0.058 | 0.045 | 0.054 | 0.036 |
| 50-54 | 0.064 | 0.054 | 0.047 | 0.042 | 0.058 | 0.04 |
| 55-59 | 0.061 | 0.049 | 0.044 | 0.038 | 0.063 | 0.044 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Population 15 Years and Over",
    "P Never Married Male 1981": 0.425,
    "P Never Married Male 2012": 0.3,
    "P Never Married Male 2024": 0.307,
    "P Never Married Female 1981": 0.324,
    "P Never Married Female 2012": 0.22,
    "P Never Married Female 2024": 0.228
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=179> (Table 9.4)

## 108. [Percentage of Married Population Aged 15 Years and Over by Age Group, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.5-Percentage-of-Married-Population-Aged-15-Years-and-Over-by-Age-Group,-1981,-2012,-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 12 rows)

| Age Group | P Married Male 1981 | P Married Male 2012 | P Married Male 2024 | P Married Female 1981 | P Married Female 2012 | P Married Female 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Population 15 Years and Over | 0.552 | 0.677 | 0.658 | 0.59 | 0.678 | 0.635 |
| 15-19 | 0.009 | 0.023 | 0.009 | 0.097 | 0.104 | 0.034 |
| 20-24 | 0.162 | 0.185 | 0.107 | 0.437 | 0.424 | 0.243 |
| 25-29 | 0.48 | 0.514 | 0.384 | 0.679 | 0.739 | 0.618 |
| 30-34 | 0.743 | 0.786 | 0.702 | 0.812 | 0.872 | 0.869 |
| 35-39 | 0.862 | 0.891 | 0.837 | 0.861 | 0.895 | 0.913 |
| 40-44 | 0.899 | 0.914 | 0.887 | 0.861 | 0.885 | 0.908 |
| 45-49 | 0.905 | 0.92 | 0.912 | 0.836 | 0.86 | 0.884 |
| 50-54 | 0.9 | 0.92 | 0.92 | 0.786 | 0.82 | 0.846 |
| 55-59 | 0.891 | 0.92 | 0.917 | 0.727 | 0.769 | 0.788 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Population 15 Years and Over",
    "P Married Male 1981": 0.552,
    "P Married Male 2012": 0.677,
    "P Married Male 2024": 0.658,
    "P Married Female 1981": 0.59,
    "P Married Female 2012": 0.678,
    "P Married Female 2024": 0.635
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=179> (Table 9.5)

## 109. [Percentage of Widowed Population Aged 15 Years and over, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 12 rows)

| Age Group | P Widowed Male 1981 | P Widowed Male 2012 | P Widowed Male 2024 | P Widowed Female 1981 | P Widowed Female 2012 | P Widowed Female 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Population 15 years and over | 0.012 | 0.013 | 0.021 | 0.052 | 0.087 | 0.117 |
| 15-19 | 0.0 | 0.0 | 0.0 | 0.001 | 0.001 | 0.0 |
| 20-24 | 0.001 | 0.0 | 0.0 | 0.005 | 0.002 | 0.001 |
| 25-29 | 0.002 | 0.001 | 0.001 | 0.011 | 0.005 | 0.003 |
| 30-34 | 0.003 | 0.001 | 0.002 | 0.02 | 0.01 | 0.007 |
| 35-39 | 0.006 | 0.002 | 0.003 | 0.039 | 0.019 | 0.013 |
| 40-44 | 0.01 | 0.004 | 0.004 | 0.07 | 0.035 | 0.025 |
| 45-49 | 0.018 | 0.006 | 0.007 | 0.111 | 0.062 | 0.047 |
| 50-54 | 0.029 | 0.011 | 0.012 | 0.164 | 0.1 | 0.083 |
| 55-59 | 0.042 | 0.018 | 0.021 | 0.228 | 0.148 | 0.142 |

### Example Data Row (JSON)

```json
{
    "Age Group": "Population 15 years and over",
    "P Widowed Male 1981": 0.012,
    "P Widowed Male 2012": 0.013,
    "P Widowed Male 2024": 0.021,
    "P Widowed Female 1981": 0.052,
    "P Widowed Female 2012": 0.087,
    "P Widowed Female 2024": 0.117
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=181> (Table 9.6)

## 110. [Number of Divorced or Separated Persons per 10,000 Population Aged 15 Years and Over, 1981, 2012, and](data/final-report-tables/chapter-9/9.7-Number-of-Divorced-or-Separated-Persons-per-10,000-Population-Aged-15-Years-and-Over,-1981,-2012,-and)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Marital Status | Male 1981 Per 10K | Male 2012 Per 10K | Male 2024 Per 10K | Female 1981 Per 10K | Female 2012 Per 10K | Female 2024 Per 10K |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Divorced | 23 | 37 | 20 | 33 | 35 | 50 |
| Legal  Separated | 19 | 26 | 15 | 25 | 21 | 31 |
| Not legal | 0 | 0 | 59 | 88 | 79 | 112 |

### Example Data Row (JSON)

```json
{
    "Marital Status": "Divorced",
    "Male 1981 Per 10K": 23,
    "Male 2012 Per 10K": 37,
    "Male 2024 Per 10K": 20,
    "Female 1981 Per 10K": 33,
    "Female 2012 Per 10K": 35,
    "Female 2024 Per 10K": 50
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=181> (Table 9.7)

## 111. [Mean Age at Marriage, 1953–2024](data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage,-1953–2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Census Year | Mean Age Of Marriage Male | Mean Age Of Marriage Female | Mean Diff |
| :-- | :-- | :-- | :-- |
| 1953 | 27.2 | 20.9 | 6.3 |
| 1963 | 27.9 | 22.1 | 5.8 |
| 1971 | 28.0 | 23.5 | 4.5 |
| 1981 | 27.9 | 24.4 | 3.5 |
| 2012 | 27.2 | 23.4 | 3.8 |
| 2024 | 29.2 | 25.6 | 3.6 |

### Example Data Row (JSON)

```json
{
    "Census Year": "1953",
    "Mean Age Of Marriage Male": 27.2,
    "Mean Age Of Marriage Female": 20.9,
    "Mean Diff": 6.3
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=182> (Table 9.8)

## 112. [Mean Age at Marriage by Sector, 2024](data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Mean Age Of Marriage Male | Mean Age Of Marriage Female | Mean Diff |
| :-- | :-- | :-- | :-- |
| Sri Lanka | 29.2 | 25.6 | 3.6 |
| Urban * | 29.8 | 26.6 | 3.2 |
| Rural | 29.0 | 25.4 | 3.6 |
| Estate Rural ** | 28.4 | 24.5 | 3.9 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "Mean Age Of Marriage Male": 29.2,
    "Mean Age Of Marriage Female": 25.6,
    "Mean Diff": 3.6
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=182> (Table 9.9)

## 113. [Mean Age at Marriage by District of Usual Residence, 2012 and 2024](data/final-report-tables/chapter-9/9.10-Mean-Age-at-Marriage-by-District-of-Usual-Residence,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Avg Age Male 2012 | Avg Age Female 2012 | Avg Age Male 2024 | Avg Age Female 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 28.0 | 24.9 | 30.1 | 27.2 |
| LK-12 | Gampaha | district | 27.5 | 24.3 | 29.7 | 26.5 |
| LK-13 | Kalutara | district | 27.2 | 23.7 | 29.4 | 26.0 |
| LK-21 | Kandy | district | 27.8 | 23.9 | 29.8 | 26.1 |
| LK-22 | Matale | district | 27.0 | 22.5 | 28.8 | 24.9 |
| LK-23 | Nuwara Eliya | district | 27.2 | 23.2 | 29.2 | 25.0 |
| LK-31 | Galle | district | 27.3 | 23.5 | 29.7 | 26.0 |
| LK-32 | Matara | district | 27.6 | 23.5 | 29.8 | 26.0 |
| LK-33 | Hambantota | district | 26.9 | 22.6 | 29.1 | 25.4 |
| LK-41 | Jaffna | district | 28.8 | 26.4 | 30.8 | 26.6 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Avg Age Male 2012": 28.0,
    "Avg Age Female 2012": 24.9,
    "Avg Age Male 2024": 30.1,
    "Avg Age Female 2024": 27.2
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=183> (Table 9.10)

## 114. [Mean Age at Marriage by Ethnic Group, 2024](data/final-report-tables/chapter-9/9.11-Mean-Age-at-Marriage-by-Ethnic-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Ethnicity | Mean Age Of Marriage Male | Mean Age Of Marriage Female |
| :-- | :-- | :-- |
| Sinhalese | 29.5 | 26.1 |
| Sri Lanka Tamil | 29.0 | 25.1 |
| Indian Tamil/Malaiyaga Thamilar | 28.5 | 24.7 |
| Sri Lanka Moor/Muslim | 27.2 | 23.4 |
| Other* | 29.5 | 25.9 |

### Example Data Row (JSON)

```json
{
    "Ethnicity": "Sinhalese",
    "Mean Age Of Marriage Male": 29.5,
    "Mean Age Of Marriage Female": 26.1
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=184> (Table 9.11)

## 115. [Percentage Distribution of Ever-Married Women Aged 15 Years and Over by the Number of Live Births perWoman and Sector, 2024](data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Population Of Ever Married Women Aged 15 And Over | P 0 | P 1 | P 2 | P 3 | P 4 | P 5 | P 6 | P 7 Plus |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| All Sectors | 6977254 | 0.106 | 0.19 | 0.333 | 0.224 | 0.081 | 0.034 | 0.016 | 0.016 |
| Urban* | 1207941 | 0.129 | 0.213 | 0.34 | 0.199 | 0.069 | 0.027 | 0.012 | 0.011 |
| Rural | 5504477 | 0.1 | 0.187 | 0.334 | 0.226 | 0.082 | 0.035 | 0.016 | 0.018 |
| Estate Rural ** | 264836 | 0.124 | 0.16 | 0.262 | 0.283 | 0.107 | 0.038 | 0.014 | 0.012 |

### Example Data Row (JSON)

```json
{
    "Sector": "All Sectors",
    "Population Of Ever Married Women Aged 15 And Over": 6977254,
    "P 0": 0.106,
    "P 1": 0.19,
    "P 2": 0.333,
    "P 3": 0.224,
    "P 4": 0.081,
    "P 5": 0.034,
    "P 6": 0.016,
    "P 7 Plus": 0.016
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=184> (Table 9.12)

## 116. [Number and Percentage Distribution of Married Women Aged 15–49 Years by Age Group, 2012 and 2024](data/final-report-tables/chapter-9/9.13-Number-and-Percentage-Distribution-of-Married-Women-Aged-15–49-Years-by-Age-Group,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age Group | 2012 Population | 2024 Population |
| :-- | :-- | :-- |
| 15-19 | 85392 | 30199 |
| 20-24 | 335158 | 198888 |
| 25-29 | 598450 | 438683 |
| 30-34 | 734555 | 635307 |
| 35-39 | 646905 | 682347 |
| 40-44 | 617503 | 741533 |
| 45-49 | 574175 | 672196 |
| 15-49 years | 3592138 | 3399153 |

### Example Data Row (JSON)

```json
{
    "Age Group": "15-19",
    "2012 Population": 85392,
    "2024 Population": 30199
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=185> (Table 9.13)

## 117. [Age-Specific Fertility Rates (ASFR), 2012 and 2024](data/final-report-tables/chapter-9/9.14-Age-Specific-Fertility-Rates-(ASFR),-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age Group | 1981 Fertility Rate Per K | 2012 Fertility Rate Per K | 2024 Fertility Rate Per K |
| :-- | :-- | :-- | :-- |
| 15-19 | 38 | 36 | 7 |
| 20-24 | 177 | 107 | 41 |
| 25-29 | 226 | 147 | 86 |
| 30-34 | 204 | 118 | 83 |
| 35-39 | 90 | 58 | 38 |
| 40-44 | 28 | 16 | 9 |
| 45-49 | 4 | 2 | 1 |

### Example Data Row (JSON)

```json
{
    "Age Group": "15-19",
    "1981 Fertility Rate Per K": 38,
    "2012 Fertility Rate Per K": 36,
    "2024 Fertility Rate Per K": 7
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=186> (Table 9.14)

## 118. [Total Fertility Rate (TFR), 1981, 2012 and 2024](data/final-report-tables/chapter-9/9.15-Total-Fertility-Rate-(TFR),-1981,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Census Year | Total Fertility Rate |
| :-- | :-- |
| 1981 | 3.3 |
| 2012 | 2.4 |
| 2024 | 1.3 |

### Example Data Row (JSON)

```json
{
    "Census Year": "1981",
    "Total Fertility Rate": 3.3
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=187> (Table 9.15)

## 119. [Age-Specific Fertility Rate (ASFR), Age-Specific Marital Fertility Rate (ASMFR), Total Fertility Rate (TFR) andTotal Marital Fertility Rate (TMFR)](data/final-report-tables/chapter-9/9.16-Age-Specific-Fertility-Rate-(ASFR),-Age-Specific-Marital-Fertility-Rate-(ASMFR),-Total-Fertility-Rate-(TFR)-andTotal-Marital-Fertility-Rate-(TMFR))

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Age Group | Asfr Age Specific Fertility Rate Per K | Asmfr Age Specific Marital Fertility Rate Per K |
| :-- | :-- | :-- |
| 15-19 | 7.0 | 139.0 |
| 20-24 | 41.0 | 143.0 |
| 25-29 | 86.0 | 126.0 |
| 30-34 | 83.0 | 91.0 |
| 35-39 | 38.0 | 40.0 |
| 40-44 | 9.0 | 9.0 |
| 45-49 | 1.0 | 1.0 |

### Example Data Row (JSON)

```json
{
    "Age Group": "15-19",
    "Asfr Age Specific Fertility Rate Per K": 7.0,
    "Asmfr Age Specific Marital Fertility Rate Per K": 139.0
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=189> (Table 9.16)

## 120. [Gross Reproduction Rate Using TFR and TMFR](data/final-report-tables/chapter-9/9.17-Gross-Reproduction-Rate-Using-TFR-and-TMFR)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2.6 | -- | -- | -- | -- | -- | -- |
| 2.6 | -- | -- | -- | -- | -- | -- |
| 2.6 | -- | -- | -- | -- | -- | -- |
| 2.5 | -- | -- | -- | -- | -- | -- |
| 2.5 | -- | -- | -- | -- | -- | -- |
| 2.5 | -- | -- | -- | -- | -- | -- |
| 2.5 | -- | -- | -- | -- | -- | -- |
| 2.4 | -- | -- | -- | -- | -- | -- |
| Differences in Total Marital Fertility Rate (TMFR) among Districts |  |  |  |  |  |  |
| Figure 9.7 shows a comparison of Total Marital Fertility Rates (TMFR) by district of usual residence. |  |  |  |  |  |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=190> (Table 9.17)

## 121. [Percentage Distribution of Household Size by Sector, 2024](data/final-report-tables/chapter-10/10.1-Percentage-Distribution-of-Household-Size-by-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Households | P 1 | P 2 | P 3 | P 4 | P 5 | P 6 | P 7 Or Over |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Urban* | 1045665 | 0.106 | 0.177 | 0.205 | 0.258 | 0.151 | 0.064 | 0.039 |
| Rural | 4827055 | 0.104 | 0.182 | 0.213 | 0.25 | 0.159 | 0.063 | 0.029 |
| Estate Rural** | 238595 | 0.114 | 0.178 | 0.19 | 0.216 | 0.183 | 0.075 | 0.044 |

### Example Data Row (JSON)

```json
{
    "Sector": "Urban*",
    "Households": 1045665,
    "P 1": 0.106,
    "P 2": 0.177,
    "P 3": 0.205,
    "P 4": 0.258,
    "P 5": 0.151,
    "P 6": 0.064,
    "P 7 Or Over": 0.039
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=192> (Table 10.1)

## 122. [Percentage Distribution of the Number and of Households by Sector, District and Household Type, 2024](data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | One Person | Nuclear | Extended | Composite | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 69392 | 368810 | 204760 | 18860 | 661822 |
| LK-12 | Gampaha | district | 79204 | 378791 | 220914 | 9726 | 688635 |
| LK-13 | Kalutara | district | 30146 | 200277 | 119953 | 2587 | 352963 |
| LK-21 | Kandy | district | 37663 | 227856 | 128989 | 3118 | 397626 |
| LK-22 | Matale | district | 16281 | 88182 | 45750 | 919 | 151132 |
| LK-23 | Nuwara Eliya | district | 21435 | 111832 | 66308 | 686 | 200261 |
| LK-31 | Galle | district | 31145 | 179230 | 95257 | 2072 | 307704 |
| LK-32 | Matara | district | 21716 | 137577 | 71010 | 1643 | 231946 |
| LK-33 | Hambantota | district | 19492 | 120108 | 48267 | 771 | 188638 |
| LK-41 | Jaffna | district | 17874 | 92908 | 48086 | 885 | 159753 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "One Person": 69392,
    "Nuclear": 368810,
    "Extended": 204760,
    "Composite": 18860,
    "Total Value": 661822
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=193> (Table 10.2)

## 123. [Percentage Distribution of the Number of Household Heads by Ethnic group of the Head of Household and typeof Household, 2024](data/final-report-tables/chapter-10/10.3-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Ethnic-group-of-the-Head-of-Household-and-typeof-Household,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Census of Population and Housing  - 2024 | -- | -- | -- | -- | -- | -- |
| Gampaha  District,  reported  as  the  most  populous  district,  shows  the  highest  number  of  households, | -- | -- | -- | -- | -- | -- |
| followed by Colombo District, which has the second-highest number of households. The lowest number of | -- | -- | -- | -- | -- | -- |
| households is reported from Mannar district, while the second lowest number of  households is reported | -- | -- | -- | -- | -- | -- |
| from Mullaitivu district. | -- | -- | -- | -- | -- | -- |
| Further Mullaitivu (12.4%) shows the highest percentage of one person households. Trincomalee (68.1%) | -- | -- | -- | -- | -- | -- |
| shows the highest percentage of nuclear households, and Kegalle (34.1%) reports the highest percentage | -- | -- | -- | -- | -- | -- |
| of  extended  households.  The  highest  percentage  of  composite  households  (2.8%)  is  reported  from | -- | -- | -- | -- | -- | -- |
| Colombo district. | -- | -- | -- | -- | -- | -- |
|  |  | One-person | Nuclear | Extended | Composite |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=194> (Table 10.3)

## 124. [Percentage Distribution of the Number of Household Heads by Sex, Age Group, and Sector, 2024](data/final-report-tables/chapter-10/10.4-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sex,-Age-Group,-and-Sector,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | Total Number | Sex of the Head of Household |  |  | Age Group of the Head of Household |  |
| Sector | of Household 
Heads |  |  | Aged below |  | Aged 65 & |
|  |  | Male | Female | 20 | Age 20-64 | over |
| Sri Lanka | 6,111,315 | 4,489,242 | 1,622,073 | 8,709 | 4,581,256 | 1,521,350 |
|  | 100.0 | 73.5 | 26.5 | 0.1 | 75.0 | 24.9 |
| U
rban | 1,042,557 | 736,435 | 306,122 | 1,838 | 782,406 | 258,313 |
|  | 100.0 | 70.6 | 29.4 | 0.2 | 75.0 | 24.8 |
| Estate Urban | 3,108 | 2,263 | 845 | 7 | 2,427 | 674 |
|  | 100.0 | 72.8 | 27.2 | 0.2 | 78.1 | 21.7 |
| Rural | 4,827,055 | 3,577,499 | 1,249,556 | 6,224 | 3,612,403 | 1,208,428 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=195> (Table 10.4)

## 125. [Percentage Distribution of the Number of Household Heads by District, Sex, and Age Group, 2024](data/final-report-tables/chapter-10/10.5-Percentage-Distribution-of-the-Number-of-Household-Heads-by-District,-Sex,-and-Age-Group,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 58 rows)

| Region Id | Region Name | Region Ent Type | Total Households | Male | Female | Age Below 20 | Age 20 64 | Age 65 Above |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 661822 | 478413 | 183409 | 1038 | 494815 | 165969 |
| LK-12 | Gampaha | district | 688635 | 514672 | 173963 | 1361 | 521172 | 166102 |
| LK-13 | Kalutara | district | 352963 | 268885 | 84078 | 259 | 259458 | 93246 |
| LK-21 | Kandy | district | 397626 | 290101 | 107525 | 413 | 283723 | 113490 |
| LK-22 | Matale | district | 151132 | 111566 | 39566 | 212 | 112855 | 38065 |
| LK-23 | Nuwara Eliya | district | 200261 | 144240 | 56021 | 405 | 151486 | 48370 |
| LK-31 | Galle | district | 307704 | 225961 | 81743 | 313 | 218546 | 88845 |
| LK-32 | Matara | district | 231946 | 173237 | 58709 | 206 | 161530 | 70210 |
| LK-33 | Hambantota | district | 188638 | 143131 | 45507 | 168 | 136687 | 51783 |
| LK-41 | Jaffna | district | 159753 | 114699 | 45054 | 73 | 111663 | 48017 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total Households": 661822,
    "Male": 478413,
    "Female": 183409,
    "Age Below 20": 1038,
    "Age 20 64": 494815,
    "Age 65 Above": 165969
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=196> (Table 10.5)

## 126. [Percentage Distribution of the Number of Household Heads by Sector and Marital Status, 2024](data/final-report-tables/chapter-10/10.6-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sector-and-Marital-Status,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 | Col 9 | Col 10 | Col 11 | Col 12 | Col 13 | Col 14 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  |  |  | Census of Population and Housing  - 2024 |  |  |  |  |  |  |  |  |
| 45.0 |  |  |  |  |  |  |  |  |  | 41.3 |  |  |  |  |
| 40.0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35.0 |  |  |  |  |  |  |  |  | 30.431.2 | 32.9 |  |  |  |  |
| 30.0 | 26.5 | 27.7 | 25.3 | 27.026.2 | 28.0 | 26.6 | 25.3 | 28.2 | 26.7 |  | 26.626.3 | 27.4 | 28.4 | 27.0 |
| 25.0 |  |  | 23.8 |  |  |  | 24.1 | 22.8 |  |  |  | 25.0 | 24.2 |  |
| Percentage |  |  |  |  |  |  |  |  |  |  |  |  |  | 21.221.8 |
| 20.0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15.0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10.0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=197> (Table 10.6)

## 127. [Percentage Distribution of the Number of Household Heads by Sex and Marital Status, 2024](data/final-report-tables/chapter-10/10.7-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sex-and-Marital-Status,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  | Table 10.6 : Percentage Distribution of the Number of Household Heads by Sector and Marital Status, 2024 |  |  |  |  |  |  |
|  | Total |  |  |  | Marital Status |  |  |
| Sector | Number of 
Household | Never |  |  |  | Legally | Separated |
|  | heads | Married | Married | Widowed | Divorced | Separated | (not Legally) |
| Sri Lanka | 6,111,315 | 226,061 | 4,938,928 | 791,122 | 36,116 | 23,176 | 95,912 |
|  | 100.0 | 3.7 | 80.8 | 12.9 | 0.6 | 0.4 | 1.6 |
| U
rban* | 1,045,665 | 53,728 | 847,598 | 122,157 | 7,926 | 3,516 | 10,740 |
|  | 100.0 | 5.1 | 81.1 | 11.7 | 0.8 | 0.3 | 1.0 |
| Rural | 4,827,055 | 164,609 | 3,899,676 | 634,181 | 27,535 | 19,238 | 81,816 |
|  | 100.0 | 3.4 | 80.8 | 13.1 | 0.6 | 0.4 | 1.7 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=197> (Table 10.7)

## 128. [Percentage Distribution of Household Heads by Highest Educational Qualification Obtained and Sector, 2024](data/final-report-tables/chapter-10/10.8-Percentage-Distribution-of-Household-Heads-by-Highest-Educational-Qualification-Obtained-and-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | No Schooling | Passed 1 5 Years | Passed 6 10 Years | Gce Ol | Gce Al | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 174144 | 933438 | 2443894 | 1310679 | 1249160 | 6111315 |
| Urban | 16211 | 87831 | 313916 | 263964 | 360635 | 1042557 |
| Estate Urban | 329 | 833 | 1353 | 317 | 276 | 3108 |
| Rural | 127933 | 761530 | 2037293 | 1023234 | 877065 | 4827055 |
| Estate Rural | 29671 | 83244 | 91332 | 23164 | 11184 | 238595 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "No Schooling": 174144,
    "Passed 1 5 Years": 933438,
    "Passed 6 10 Years": 2443894,
    "Gce Ol": 1310679,
    "Gce Al": 1249160,
    "Total Value": 6111315
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=198> (Table 10.8)

## 129. [Percentage Distribution of Household Heads by District and Highest Educational Qualification Obtained,](data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | No Schooling | Passed 1 5 Years | Passed 6 10 Years | Gce Ol | Gce Al | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 9113 | 41277 | 189119 | 178500 | 243813 | 661822 |
| LK-12 | Gampaha | district | 6336 | 45940 | 254321 | 194820 | 187218 | 688635 |
| LK-13 | Kalutara | district | 6052 | 40233 | 144218 | 84890 | 77570 | 352963 |
| LK-21 | Kandy | district | 11896 | 54250 | 144659 | 91921 | 94900 | 397626 |
| LK-22 | Matale | district | 5233 | 28015 | 66546 | 27846 | 23492 | 151132 |
| LK-23 | Nuwara Eliya | district | 15552 | 52077 | 78455 | 32977 | 21200 | 200261 |
| LK-31 | Galle | district | 7209 | 45798 | 130111 | 63383 | 61203 | 307704 |
| LK-32 | Matara | district | 7407 | 38150 | 98413 | 45960 | 42016 | 231946 |
| LK-33 | Hambantota | district | 6415 | 36354 | 82320 | 36996 | 26553 | 188638 |
| LK-41 | Jaffna | district | 865 | 26992 | 74540 | 29740 | 27616 | 159753 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "No Schooling": 9113,
    "Passed 1 5 Years": 41277,
    "Passed 6 10 Years": 189119,
    "Gce Ol": 178500,
    "Gce Al": 243813,
    "Total Value": 661822
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=199> (Table 10.9)

## 130. [and Percentage Distribution of Individuals in One Person Households Aged 60 Years and Over, by Sexand Age Group, 2024](data/final-report-tables/chapter-10/10.10-and-Percentage-Distribution-of-Individuals-in-One-Person-Households-Aged-60-Years-and-Over,-by-Sexand-Age-Group,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 |
| :-- | :-- | :-- | :-- |
| Census of Population and Housing  - 2024 | -- | -- | -- |
| 10.7 Characteristics of Household Heads who Lives in One Person Households | -- | -- | -- |
| In Sri Lanka, there are 640,704 one-person households (Table 10.3). Among the household heads living | -- | -- | -- |
| in such households, 370,229 are aged 60 years and over. Of these elderly household heads, 71.3 percent | -- | -- | -- |
| are female, while 28.7 percent are male. As indicated in Table 10.9, within the population aged 60 years | -- | -- | -- |
| and over, the number of female household heads living alone exceeds that of males across all age groups. | -- | -- | -- |
| Notably, in the age group of 70 years and over, the number of males living alone is approximately one- | -- | -- | -- |
| third of the corresponding number of females. | -- | -- | -- |
| Table 10.10: Number and Percentage Distribution of Individuals in One Person Households Aged 60 Years and Over, by Sex and |  |  |  |
|  |  | Age Group, 2024 |  |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=200> (Table 10.10)

## 131. [Number of Occupied Housing Units by Sector, 2012 and 2024](data/final-report-tables/chapter-11/11.1-Number-of-Occupied-Housing-Units-by-Sector,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | Households 2012 | Households 2024 |
| :-- | :-- | :-- |
| Sri Lanka | 5207740 | 6030541 |
| Urban* | 891103 | 1028363 |
| Rural | 4092252 | 4773336 |
| Estate-Rural** | 224385 | 228842 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "Households 2012": 5207740,
    "Households 2024": 6030541
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=201> (Table 11.1)

## 132. [Number of Occupied Housing Units & Permanently Closed/Vacant Housing Units by District, 2012 and 2024](data/final-report-tables/chapter-11/11.2-Number-of-Occupied-Housing-Units-&-Permanently-Closed/Vacant-Housing-Units-by-District,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Occupied 2012 | Permanently Closed Or Vacant 2012 | Occupied 2024 | Permanently Closed Or Vacant 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 562550 | 78052 | 654051 | 113837 |
| LK-12 | Gampaha | district | 598674 | 65355 | 683025 | 102557 |
| LK-13 | Kalutara | district | 302371 | 35199 | 349430 | 45678 |
| LK-21 | Kandy | district | 342911 | 41803 | 389826 | 53787 |
| LK-22 | Matale | district | 128090 | 16001 | 148184 | 21617 |
| LK-23 | Nuwara Eliya | district | 178440 | 21627 | 192915 | 28387 |
| LK-31 | Galle | district | 271236 | 42176 | 305379 | 43462 |
| LK-32 | Matara | district | 205153 | 29209 | 230034 | 33039 |
| LK-33 | Hambantota | district | 155716 | 24223 | 187558 | 29971 |
| LK-41 | Jaffna | district | 136969 | 21364 | 156797 | 34718 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Occupied 2012": 562550,
    "Permanently Closed Or Vacant 2012": 78052,
    "Occupied 2024": 654051,
    "Permanently Closed Or Vacant 2024": 113837
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=202> (Table 11.2)

## 133. [Number of Housing Units by the Year of Construction, 2024](data/final-report-tables/chapter-11/11.3-Number-of-Housing-Units-by-the-Year-of-Construction,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 14 rows)

| Construction Year | Housing Units |
| :-- | :-- |
| Total* | 6029330 |
| 2024 | 107031 |
| 2023 | 117352 |
| 2022 | 152976 |
| 2021 | 144164 |
| 2020 | 216142 |
| 2019 | 199745 |
| 2018 | 323965 |
| 2017 -2013 | 780280 |
| 2012-2008 | 669943 |

### Example Data Row (JSON)

```json
{
    "Construction Year": "Total*",
    "Housing Units": 6029330
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=203> (Table 11.3)

## 134. [Tenure of Housing Units by Sector and District, 2024](data/final-report-tables/chapter-11/11.4-Tenure-of-Housing-Units-by-Sector-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | P Owned By A Household Member | P Rent Or Lease Government Owned | P Rent Or Lease Privately Owned | P Rent Or Lease Free Of Rent | P Encroached | P Other |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 0.76 | 0.035 | 0.166 | 0.024 | 0.01 | 0.005 |
| LK-12 | Gampaha | district | 0.816 | 0.022 | 0.125 | 0.022 | 0.008 | 0.007 |
| LK-13 | Kalutara | district | 0.868 | 0.019 | 0.059 | 0.041 | 0.005 | 0.008 |
| LK-21 | Kandy | district | 0.846 | 0.03 | 0.053 | 0.05 | 0.007 | 0.014 |
| LK-22 | Matale | district | 0.867 | 0.017 | 0.038 | 0.059 | 0.007 | 0.012 |
| LK-23 | Nuwara Eliya | district | 0.522 | 0.021 | 0.044 | 0.398 | 0.007 | 0.008 |
| LK-31 | Galle | district | 0.895 | 0.014 | 0.041 | 0.032 | 0.005 | 0.013 |
| LK-32 | Matara | district | 0.888 | 0.015 | 0.037 | 0.04 | 0.004 | 0.016 |
| LK-33 | Hambantota | district | 0.933 | 0.013 | 0.022 | 0.015 | 0.008 | 0.009 |
| LK-41 | Jaffna | district | 0.744 | 0.021 | 0.087 | 0.138 | 0.003 | 0.007 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "P Owned By A Household Member": 0.76,
    "P Rent Or Lease Government Owned": 0.035,
    "P Rent Or Lease Privately Owned": 0.166,
    "P Rent Or Lease Free Of Rent": 0.024,
    "P Encroached": 0.01,
    "P Other": 0.005
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=204> (Table 11.4)

## 135. [Percentage of Housing Units Owned by Household Members and Sector, 2012 and 2024](data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | P Households Owned By Members 2012 | P Households Owned By Members 2024 |
| :-- | :-- | :-- |
| Sri Lanka | 0.829 | 0.846 |
| Urban* | 0.75 | 0.769 |
| Rural | 0.88 | 0.89 |
| Estate- Rural** | 0.222 | 0.295 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "P Households Owned By Members 2012": 0.829,
    "P Households Owned By Members 2024": 0.846
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=205> (Table 11.5)

## 136. [Percentage of Housing units by Materials Used to Construct Walls, Roofs and Floors,](data/final-report-tables/chapter-11/11.6-Percentage-of-Housing-units-by-Materials-Used-to-Construct-Walls,-Roofs-and-Floors,)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 |
| :-- | :-- |
| Materials Used for Construction | Housing Units |
| Sri Lanka | 100.0 |
| Wall |  |
| Bricks | 46.4 |
| Cement block | 46.9 |
| Granite/Cube stones | 1.6 |
| Cabook | 1.1 |
| Pressed soil bricks | 1.8 |
| Mud/Warichchi | 1.2 |
| Cadjan/Palmyra | 0.1 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=205> (Table 11.6)

## 137. [of Housing Units and Status of Housing Units, by Sector and District, 2024](data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Permanent | Semi Permanent | Improvised | Not Permanent | Total Value |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 645260 | 8256 | 195 | 340 | 654051 |
| LK-12 | Gampaha | district | 673967 | 8381 | 404 | 273 | 683025 |
| LK-13 | Kalutara | district | 341868 | 7237 | 156 | 169 | 349430 |
| LK-21 | Kandy | district | 369080 | 20395 | 216 | 135 | 389826 |
| LK-22 | Matale | district | 139556 | 8492 | 75 | 61 | 148184 |
| LK-23 | Nuwara Eliya | district | 179664 | 12472 | 344 | 435 | 192915 |
| LK-31 | Galle | district | 298982 | 6129 | 138 | 130 | 305379 |
| LK-32 | Matara | district | 223653 | 6193 | 113 | 75 | 230034 |
| LK-33 | Hambantota | district | 183050 | 4364 | 84 | 60 | 187558 |
| LK-41 | Jaffna | district | 151345 | 4360 | 681 | 411 | 156797 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Permanent": 645260,
    "Semi Permanent": 8256,
    "Improvised": 195,
    "Not Permanent": 340,
    "Total Value": 654051
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=207> (Table 11.7)

## 138. [in Housing Units by Sector, 2024](data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | With Only One Room | With Only More Than One Room | Total Value |
| :-- | :-- | :-- | :-- |
| Sri Lanka | 358358 | 5672183 | 6030541 |
| Urban | 80249 | 945081 | 1025330 |
| Estate- Urban | 377 | 2656 | 3033 |
| Rural | 251344 | 4521992 | 4773336 |
| Estate- Rural | 26388 | 202454 | 228842 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "With Only One Room": 358358,
    "With Only More Than One Room": 5672183,
    "Total Value": 6030541
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=208> (Table 11.8)

## 139. [Distribution of Households by Main Source of Drinking Water, 2024](data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 16 rows)

| Source Drinking Water | Households |
| :-- | :-- |
| Sri Lanka | 6111315 |
| Protected well | 1624506 |
| Semi protected well | 267327 |
| Unprotected well | 77806 |
| Tube well | 270401 |
| Spring/Fountain | 230268 |
| Pipe borne water - National water supply & drainage board | 2374349 |
| Pipe borne water - Local Authority | 100764 |
| Pipe borne water - Community based organization | 419247 |
| Pipe borne water - Private water supply project | 130394 |

### Example Data Row (JSON)

```json
{
    "Source Drinking Water": "Sri Lanka",
    "Households": 6111315
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=208> (Table 11.9)

## 140. [Percentage Distribution of Households by Availability of Drinking Water Facility, by Sector and District,](data/final-report-tables/chapter-11/11.10-Percentage-Distribution-of-Households-by-Availability-of-Drinking-Water-Facility,-by-Sector-and-District,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 57 rows)

| Region Id | Region Name | Region Ent Type | Total Value | P Within Housing Unit | P Within Premises | P Outside Premises |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 661823.0 | 0.972 | 0.021 | 0.007 |
| LK-12 | Gampaha | district | 688636.0 | 0.896 | 0.073 | 0.031 |
| LK-13 | Kalutara | district | 352964.0 | 0.898 | 0.064 | 0.038 |
| LK-21 | Kandy | district | 397627.0 | 0.864 | 0.089 | 0.047 |
| LK-22 | Matale | district | 151132.999 | 0.766 | 0.127 | 0.106 |
| LK-23 | Nuwara Eliya | district | 200262.0 | 0.605 | 0.258 | 0.137 |
| LK-31 | Galle | district | 307704.999 | 0.852 | 0.093 | 0.054 |
| LK-32 | Matara | district | 231947.0 | 0.832 | 0.124 | 0.044 |
| LK-33 | Hambantota | district | 188639.0 | 0.778 | 0.158 | 0.064 |
| LK-41 | Jaffna | district | 159754.0 | 0.305 | 0.401 | 0.294 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Total Value": 661823.0,
    "P Within Housing Unit": 0.972,
    "P Within Premises": 0.021,
    "P Outside Premises": 0.007
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=209> (Table 11.10)

## 141. [Distribution of Households in Sri Lanka's ability to Obtain Drinking Water Throughout the Year, 2024](data/final-report-tables/chapter-11/11.11-Distribution-of-Households-in-Sri-Lanka's-ability-to-Obtain-Drinking-Water-Throughout-the-Year,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Source Of Drinking Water | Households With Water Supply Throughout The Year | Households With No Water Suppply For At Least One Month |
| :-- | :-- | :-- |
| Total* | 5374541 | 184964 |
| Ground water | 2361822 | 108486 |
| Pipe borne water | 2959509 | 65245 |
| Other | 53210 | 11233 |

### Example Data Row (JSON)

```json
{
    "Source Of Drinking Water": "Total*",
    "Households With Water Supply Throughout The Year": 5374541,
    "Households With No Water Suppply For At Least One Month": 184964
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=210> (Table 11.11)

## 142. [Percentage of households Using Firewood and gas, by Sector and District,](data/final-report-tables/chapter-11/11.12-Percentage-of-households-Using-Firewood-and-gas,-by-Sector-and-District,)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | P Firewood 2012 | P Firewood 2024 | P Gas 2012 | P Gas 2024 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 0.288 | 0.099 | 0.605 | 0.855 |
| LK-12 | Gampaha | district | 0.625 | 0.318 | 0.31 | 0.639 |
| LK-13 | Kalutara | district | 0.771 | 0.424 | 0.212 | 0.559 |
| LK-21 | Kandy | district | 0.808 | 0.583 | 0.178 | 0.403 |
| LK-22 | Matale | district | 0.909 | 0.755 | 0.084 | 0.235 |
| LK-23 | Nuwara Eliya | district | 0.865 | 0.719 | 0.112 | 0.266 |
| LK-31 | Galle | district | 0.836 | 0.521 | 0.154 | 0.461 |
| LK-32 | Matara | district | 0.867 | 0.61 | 0.126 | 0.374 |
| LK-33 | Hambantota | district | 0.93 | 0.724 | 0.065 | 0.263 |
| LK-41 | Jaffna | district | 0.907 | 0.547 | 0.052 | 0.423 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "P Firewood 2012": 0.288,
    "P Firewood 2024": 0.099,
    "P Gas 2012": 0.605,
    "P Gas 2024": 0.855
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=211> (Table 11.12)

## 143. [Household Numbers and Percentages by Main and Secondary Energy/Fuel Type for Lighting, 2024](data/final-report-tables/chapter-11/11.13-Household-Numbers-and-Percentages-by-Main-and-Secondary-Energy/Fuel-Type-for-Lighting,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Energy Or Fuel Type | Primary Source | Secondary Source |
| :-- | :-- | :-- |
| Electricity - National grid/Rural hydro power project | 5987585 | 7323 |
| Kerosene lamp | 95150 | 2789215 |
| Solar power (grid connected) | 8093 | 23548 |
| Solar power (standalone) | 5817 | 27598 |
| Other* | 14670 | 40628 |
| No secondary source | 0 | 3223003 |

### Example Data Row (JSON)

```json
{
    "Energy Or Fuel Type": "Electricity - National grid/Rural hydro power project",
    "Primary Source": 5987585,
    "Secondary Source": 7323
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=212> (Table 11.13)

## 144. [Percentage of Households Using Electricity and Kerosene as the Main Sources of Lighting, by ResidentialSector, 2012 and 2024](data/final-report-tables/chapter-11/11.14-Percentage-of-Households-Using-Electricity-and-Kerosene-as-the-Main-Sources-of-Lighting,-by-ResidentialSector,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | P Electricity 2012 | P Electricity 2024 | P Kerosene 2012 | P Kerosene 2024 |
| :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 0.87 | 0.98 | 0.122 | 0.016 |
| Urban* | 0.968 | 0.986 | 0.031 | 0.007 |
| Rural | 0.852 | 0.979 | 0.138 | 0.017 |
| Estate- Rural ** | 0.799 | 0.966 | 0.192 | 0.029 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "P Electricity 2012": 0.87,
    "P Electricity 2024": 0.98,
    "P Kerosene 2012": 0.122,
    "P Kerosene 2024": 0.016
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=212> (Table 11.14)

## 145. [Percentage Distribution of Households by Type of Toilet Facilities, 2012 and 2024](data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Toilet Facilities | Units 2012 | Units 2024 |
| :-- | :-- | :-- |
| Toilet facilities | 2012 | 2024 |
| Within the housing unit - Exclusively for the household | 1748249 | 3798777 |
| Within the housing unit - Sharing with another household | 82078 | 157456 |
| Within Premises - Exclusively for the household | 2817362 | 1832587 |
| Within Premises - Sharing with another household | 358453 | 197678 |
| No toilet but sharing with another housing unit/units | 133772 | 101924 |
| Common/ Public toilet | 36088 | 9567 |
| Not using a toilet (use jungle, beach and open ground) | 88280 | 13326 |

### Example Data Row (JSON)

```json
{
    "Toilet Facilities": "Toilet facilities",
    "Units 2012": 2012,
    "Units 2024": 2024
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=213> (Table 11.15)

## 146. [Percentage Distribution of Type of Toilet Used by households by Sector and District, 2024](data/final-report-tables/chapter-11/11.16-Percentage-Distribution-of-Type-of-Toilet-Used-by-households-by-Sector-and-District,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | P Water Sealed | P Not Water Sealed | P Other |
| :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 0.999 | 0.001 | 0.0 |
| LK-12 | Gampaha | district | 0.998 | 0.002 | 0.0 |
| LK-13 | Kalutara | district | 0.997 | 0.003 | 0.0 |
| LK-21 | Kandy | district | 0.994 | 0.006 | 0.0 |
| LK-22 | Matale | district | 0.988 | 0.011 | 0.001 |
| LK-23 | Nuwara Eliya | district | 0.992 | 0.008 | 0.0 |
| LK-31 | Galle | district | 0.995 | 0.004 | 0.001 |
| LK-32 | Matara | district | 0.997 | 0.002 | 0.001 |
| LK-33 | Hambantota | district | 0.996 | 0.003 | 0.001 |
| LK-41 | Jaffna | district | 0.999 | 0.001 | 0.0 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "P Water Sealed": 0.999,
    "P Not Water Sealed": 0.001,
    "P Other": 0.0
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=214> (Table 11.16)

## 147. [Distribution of Households by the Main Method of Disposing Solid Waste, 2024](data/final-report-tables/chapter-11/11.17-Distribution-of-Households-by-the-Main-Method-of-Disposing-Solid-Waste,-2024)

*Build Status (**2**/5) 🔴 Raw data is difficult to parse*

### Raw Data (first 10 rows)

| Col 0 | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
| :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  | Sector |  |
| Method of disposing solid waste | Sri Lanka | Urban | Estate- | Rural | Estate- |
|  |  |  | Urban |  | Rural |
| Total number of households | 6,111,315 | 1,042,557 | 3,108 | 4,827,055 | 238,595 |
|  |  | Disposal of easy decaying waste |  |  |  |
| Total | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| By the local authority | 23.9 | 81.9 | 43.0 | 12.4 | 2.7 |
| Occupants burn | 34.2 | 8.4 | 28.2 | 39.7 | 35.7 |
| Occupants dispose within the premises | 34.5 | 6.3 | 13.4 | 40.4 | 38.0 |
| Composing solid waste | 5.6 | 2.5 | 6.0 | 6.1 | 7.8 |

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=215> (Table 11.17)

## 148. [Percentage Distribution of Households by the Main Method of Disposing Liquid Waste, 2024](data/final-report-tables/chapter-11/11.18-Percentage-Distribution-of-Households-by-the-Main-Method-of-Disposing-Liquid-Waste,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sector | P To A Properly Closed Pit | P Open Pit | P Within The Premises | P Connected To A Piped Sewer | P To A Stream Or Spring Or River Or Sea | P To A Drain On Road | P Other |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Sri Lanka | 0.267 | 0.071 | 0.573 | 0.015 | 0.011 | 0.061 | 0.002 |
| Urban | 0.462 | 0.025 | 0.237 | 0.085 | 0.015 | 0.173 | 0.003 |
| Estate- Urban | 0.11 | 0.059 | 0.413 | 0.0 | 0.025 | 0.393 | 0.0 |
| Rural | 0.234 | 0.08 | 0.646 | 0.001 | 0.007 | 0.03 | 0.002 |
| Estate- Rural | 0.094 | 0.09 | 0.555 | 0.0 | 0.073 | 0.181 | 0.007 |

### Example Data Row (JSON)

```json
{
    "Sector": "Sri Lanka",
    "P To A Properly Closed Pit": 0.267,
    "P Open Pit": 0.071,
    "P Within The Premises": 0.573,
    "P Connected To A Piped Sewer": 0.015,
    "P To A Stream Or Spring Or River Or Sea": 0.011,
    "P To A Drain On Road": 0.061,
    "P Other": 0.002
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=216> (Table 11.18)

## 149. [Percentage Distribution of Households Using Communication Technology Equipment and Vehicles by Sector,2024](data/final-report-tables/chapter-11/11.19-Percentage-Distribution-of-Households-Using-Communication-Technology-Equipment-and-Vehicles-by-Sector,2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

|  | P Radio | P Television | P Fixed Line Telephone | P Smart Mobile Phone | P Normal Mobile Phone | P Desktop Computer | P Laptop Computer | P Tablet Computer | P Internet Facilities | P Bicycle | P Motorcycle Or Scooter | P Three Wheeler | P Other |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Urban | 0.485 | 0.821 | 0.257 | 0.86 | 0.55 | 0.116 | 0.33 | 0.107 | 0.492 | 0.232 | 0.386 | 0.119 | 0.242 |
| Estate- Urban | 0.495 | 0.78 | 0.054 | 0.782 | 0.638 | 0.048 | 0.106 | 0.032 | 0.21 | 0.076 | 0.169 | 0.153 | 0.074 |
| Rural | 0.529 | 0.792 | 0.106 | 0.782 | 0.697 | 0.067 | 0.175 | 0.04 | 0.401 | 0.265 | 0.497 | 0.149 | 0.147 |
| Estate- Rural | 0.497 | 0.762 | 0.033 | 0.645 | 0.68 | 0.023 | 0.047 | 0.013 | 0.208 | 0.033 | 0.115 | 0.115 | 0.035 |

### Example Data Row (JSON)

```json
{
    "": "Urban",
    "P Radio": 0.485,
    "P Television": 0.821,
    "P Fixed Line Telephone": 0.257,
    "P Smart Mobile Phone": 0.86,
    "P Normal Mobile Phone": 0.55,
    "P Desktop Computer": 0.116,
    "P Laptop Computer": 0.33,
    "P Tablet Computer": 0.107,
    "P Internet Facilities": 0.492,
    "P Bicycle": 0.232,
    "P Motorcycle Or Scooter": 0.386,
    "P Three Wheeler": 0.119,
    "P Other": 0.242
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=216> (Table 11.19)

## 150. [Myer’s Index by Sex, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-12/12.1-Myer’s-Index-by-Sex,-1981,-2001,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sex | Myers Index 1981 | Myers Index 2001 | Myers Index 2012 | Myers Index 2024 |
| :-- | :-- | :-- | :-- | :-- |
| Both sexes | 9.7 | 2.7 | 1.7 | 1.2 |
| Male | 8.7 | 2.7 | 1.8 | 1.2 |
| Female | 11.2 | 3.0 | 1.7 | 1.1 |

### Example Data Row (JSON)

```json
{
    "Sex": "Both sexes",
    "Myers Index 1981": 9.7,
    "Myers Index 2001": 2.7,
    "Myers Index 2012": 1.7,
    "Myers Index 2024": 1.2
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=218> (Table 12.1)

## 151. [Deviations of Terminal Digits of Reported Age, 2012 and](data/final-report-tables/chapter-12/12.2-Deviations-of-Terminal-Digits-of-Reported-Age,-2012-and)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 11 rows)

| Terminal Digit | Both Sexes 2012 Myers Index | Male 2012 Myers Index | Female 2012 Myers Index | Both Sexes 2024 Myers Index | Male 2024 Myers Index | Female 2024 Myers Index |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 0 | 0.2 | 0.2 | 0.1 | -0.2 | -0.2 | -0.1 |
| 1 | 0.1 | 0.2 | 0.1 | -0.1 | -0.1 | -0.1 |
| 2 | 0.2 | 0.2 | 0.1 | 0.2 | 0.2 | 0.3 |
| 3 | -0.1 | -0.1 | -0.1 | 0.1 | 0.1 | 0.0 |
| 4 | 0.0 | 0.0 | 0.0 | 0.2 | 0.2 | 0.2 |
| 5 | -0.1 | -0.1 | -0.1 | 0.0 | 0.0 | 0.0 |
| 6 | -0.3 | -0.3 | -0.3 | 0.1 | 0.1 | 0.1 |
| 7 | 0.0 | -0.1 | 0.0 | -0.1 | -0.1 | -0.1 |
| 8 | -0.2 | -0.2 | -0.2 | -0.2 | -0.2 | -0.2 |
| 9 | 0.4 | 0.3 | 0.4 | 0.0 | 0.0 | -0.1 |

### Example Data Row (JSON)

```json
{
    "Terminal Digit": "0",
    "Both Sexes 2012 Myers Index": 0.2,
    "Male 2012 Myers Index": 0.2,
    "Female 2012 Myers Index": 0.1,
    "Both Sexes 2024 Myers Index": -0.2,
    "Male 2024 Myers Index": -0.2,
    "Female 2024 Myers Index": -0.1
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=219> (Table 12.2)

## 152. [Myers' Index by District and Sex, 2012, 2024](data/final-report-tables/chapter-12/12.3-Myers'-Index-by-District-and-Sex,-2012,-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Index Both Sexes 2012 | Index Male 2012 | Index Female 2012 | Index Both Sexes 2024 | Index Male 2024 | Index Female 2024 | P Change |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 2.2 | 2.5 | 2.0 | 1.6 | 1.9 | 1.5 | -0.273 |
| LK-12 | Gampaha | district | 2.2 | 2.3 | 2.2 | 1.3 | 1.3 | 1.4 | -0.409 |
| LK-13 | Kalutara | district | 2.2 | 2.2 | 2.2 | 1.1 | 1.1 | 1.1 | -0.5 |
| LK-21 | Kandy | district | 1.6 | 1.6 | 1.5 | 1.3 | 1.2 | 1.3 | -0.188 |
| LK-22 | Matale | district | 1.8 | 1.7 | 2.0 | 1.4 | 1.5 | 1.4 | -0.222 |
| LK-23 | Nuwara Eliya | district | 0.9 | 1.6 | 0.8 | 1.1 | 1.6 | 1.0 | 0.222 |
| LK-31 | Galle | district | 1.6 | 1.8 | 1.6 | 0.9 | 1.0 | 1.0 | -0.438 |
| LK-32 | Matara | district | 1.4 | 1.3 | 1.6 | 1.1 | 1.0 | 1.1 | -0.214 |
| LK-33 | Hambantota | district | 2.3 | 2.4 | 2.2 | 1.4 | 1.6 | 1.3 | -0.391 |
| LK-41 | Jaffna | district | 2.3 | 2.1 | 2.4 | 2.9 | 2.8 | 2.9 | 0.261 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Index Both Sexes 2012": 2.2,
    "Index Male 2012": 2.5,
    "Index Female 2012": 2.0,
    "Index Both Sexes 2024": 1.6,
    "Index Male 2024": 1.9,
    "Index Female 2024": 1.5,
    "P Change": -0.273
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=220> (Table 12.3)

## 153. [Whipple’s Index by Sex, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-12/12.4-Whipple’s-Index-by-Sex,-1981,-2001,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table

| Sex | Whipple Index 1981 | Whipple Index 2001 | Whipple Index 2012 | Whipple Index 2024 |
| :-- | :-- | :-- | :-- | :-- |
| Both sexes | 118.6 | 97.0 | 100.2 | 99.2 |
| Male | 116.7 | 97.5 | 100.3 | 99.1 |
| Female | 120.5 | 96.4 | 100.0 | 99.2 |

### Example Data Row (JSON)

```json
{
    "Sex": "Both sexes",
    "Whipple Index 1981": 118.6,
    "Whipple Index 2001": 97.0,
    "Whipple Index 2012": 100.2,
    "Whipple Index 2024": 99.2
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=221> (Table 12.4)

## 154. [Whipple's Index by District and Sex, 2012 and 2024](data/final-report-tables/chapter-12/12.5-Whipple's-Index-by-District-and-Sex,-2012-and-2024)

*Build Status (**4**/5) 🟡 Lanka data is missing*

### Data Table (first 10 of 25 rows)

| Region Id | Region Name | Region Ent Type | Index Both Sexes 2012 | Index Male 2012 | Index Female 2012 | Index Both Sexes 2024 | Index Male 2024 | Index Female 2024 | P Change |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| LK-11 | Colombo | district | 100.4 | 100.5 | 100.3 | 98.4 | 98.4 | 98.3 | -0.02 |
| LK-12 | Gampaha | district | 100.2 | 100.6 | 99.9 | 99.0 | 98.7 | 99.3 | -0.012 |
| LK-13 | Kalutara | district | 100.8 | 100.8 | 100.9 | 99.1 | 99.4 | 98.8 | -0.017 |
| LK-21 | Kandy | district | 99.6 | 99.5 | 99.8 | 98.4 | 98.6 | 98.3 | -0.012 |
| LK-22 | Matale | district | 100.2 | 99.5 | 100.9 | 98.4 | 98.3 | 98.6 | -0.018 |
| LK-23 | Nuwara Eliya | district | 99.4 | 99.3 | 99.6 | 98.0 | 97.9 | 98.1 | -0.014 |
| LK-31 | Galle | district | 101.0 | 101.1 | 100.9 | 99.6 | 99.5 | 99.7 | -0.014 |
| LK-32 | Matara | district | 100.0 | 100.3 | 99.8 | 99.9 | 99.1 | 100.7 | -0.001 |
| LK-33 | Hambantota | district | 99.5 | 99.4 | 99.7 | 100.5 | 100.0 | 101.0 | 0.01 |
| LK-41 | Jaffna | district | 100.3 | 100.6 | 100.0 | 101.6 | 101.8 | 101.4 | 0.013 |

### Example Data Row (JSON)

```json
{
    "Region Id": "LK-11",
    "Region Name": "Colombo",
    "Region Ent Type": "district",
    "Index Both Sexes 2012": 100.4,
    "Index Male 2012": 100.5,
    "Index Female 2012": 100.3,
    "Index Both Sexes 2024": 98.4,
    "Index Male 2024": 98.4,
    "Index Female 2024": 98.3,
    "P Change": -0.02
}
```

### Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=222> (Table 12.5)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
