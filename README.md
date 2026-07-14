# 🇱🇰 Sri Lanka - Census of Population and Housing 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_15:26:51-green)

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


## Datasets from Final Report (**142**)

### Chapter 1

- Table 1.1.1 - [Officers who have  Assigned for Census of Population and Housing 2024 Activities](data/final-report-tables/chapter-1/1.1.1-Officers-who-have--Assigned-for-Census-of-Population-and-Housing-2024-Activities)
- Table 1.1.2 - [The Questions and Topics Included in the Censuses of Sri Lanka 1871 - 2024](data/final-report-tables/chapter-1/1.1.2-The-Questions-and-Topics-Included-in-the-Censuses-of-Sri-Lanka-1871---2024)

### Chapter 2

- Table 2.1 - [Evolution of the Number of Administrative Districts In Sri Lanka from 1871 to 2024](data/final-report-tables/chapter-2/2.1-Evolution-of-the-Number-of-Administrative-Districts-In-Sri-Lanka-from-1871-to-2024)
- Table 2.2 - [Administrative Structure by District, 1981](data/final-report-tables/chapter-2/2.2-Administrative-Structure-by-District,-1981)
- Table 2.3 - [Administrative Structure by District, 2012](data/final-report-tables/chapter-2/2.3-Administrative-Structure-by-District,-2012)
- Table 2.4 - [Administrative Structure by District, 2024](data/final-report-tables/chapter-2/2.4-Administrative-Structure-by-District,-2024)

### Chapter 3

- Table 3.1 - [Total Population, Intercensal Increase and Average Annual Growth Rate by Census Year, 1871 - 2024](data/final-report-tables/chapter-3/3.1-Total-Population,-Intercensal-Increase-and-Average-Annual-Growth-Rate-by-Census-Year,-1871---2024)
- Table 3.2 - [Distribution of Population by Province and District, 2024](data/final-report-tables/chapter-3/3.2-Distribution-of-Population-by-Province-and-District,-2024)
- Table 3.3 - [Population and Average Annual Growth Rate by District, Census Years 1981- 2024](data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District,-Census-Years-1981--2024)
- Table 3.4 - [Population Density by District, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-3/3.4-Population-Density-by-District,-1981,-2001,-2012-and-2024)
- Table 3.5 - [Distribution of Population by Sector, 2012 and 2024](data/final-report-tables/chapter-3/3.5-Distribution-of-Population-by-Sector,-2012-and-2024)
- Table 3.6 - [Population Distribution by District and Sector, 2024](data/final-report-tables/chapter-3/3.6-Population-Distribution-by-District-and-Sector,-2024)

### Chapter 5

- Table 5.1.1 - [Lifetime Migrants by District of Dirth and District of Usual Residence,](data/final-report-tables/chapter-5/5.1.1-Lifetime-Migrants-by-District-of-Dirth-and-District-of-Usual-Residence,)
- Table 5.1.2 - [In, Out and Net Lifetime Migrants by District, 2024](data/final-report-tables/chapter-5/5.1.2-In,-Out-and-Net-Lifetime-Migrants-by-District,-2024)
- Table 5.1.3 - [Largest Migration Flows of Lifetime Migrants by District of Usual Residence, 2024](data/final-report-tables/chapter-5/5.1.3-Largest-Migration-Flows-of-Lifetime-Migrants-by-District-of-Usual-Residence,-2024)
- Table 5.1.4 - [Largest Migration Flows of Lifetime Migrants who have Migrated Out of their District of Birth, 2024](data/final-report-tables/chapter-5/5.1.4-Largest-Migration-Flows-of-Lifetime-Migrants-who-have-Migrated-Out-of-their-District-of-Birth,-2024)
- Table 5.1.5 - [In-migration, Out-migration, and Net Migration by District,](data/final-report-tables/chapter-5/5.1.5-In-migration,-Out-migration,-and-Net-Migration-by-District,)
- Table 5.1.6 - [In-migrants by District of Usual Residence and Duration of Residence, 2024](data/final-report-tables/chapter-5/5.1.6-In-migrants-by-District-of-Usual-Residence-and-Duration-of-Residence,-2024)
- Table 5.1.7 - [Reasons for Migration from District of Previous Residence to District of Usual Residence, 2024](data/final-report-tables/chapter-5/5.1.7-Reasons-for-Migration-from-District-of-Previous-Residence-to-District-of-Usual-Residence,-2024)
- Table 5.1.8 - [Distribution of the Usually Resident Population of a District by their Permanent Residence, 2024](data/final-report-tables/chapter-5/5.1.8-Distribution-of-the-Usually-Resident-Population-of-a-District-by-their-Permanent-Residence,-2024)
- Table 5.2.1 - [Population Temporarily Living Abroad by District and Sex, 2024](data/final-report-tables/chapter-5/5.2.1-Population-Temporarily-Living-Abroad-by-District-and-Sex,-2024)
- Table 5.2.2 - [Population Temporarily Living Abroad by Sector, Sex and Age Group, 2024](data/final-report-tables/chapter-5/5.2.2-Population-Temporarily-Living-Abroad-by-Sector,-Sex-and-Age-Group,-2024)
- Table 5.2.3 - [Population Temporarily Living Abroad by District and Main Reason for Living in Abroad, 2024](data/final-report-tables/chapter-5/5.2.3-Population-Temporarily-Living-Abroad-by-District-and-Main-Reason-for-Living-in-Abroad,-2024)
- Table 5.2.4 - [Population Temporarily Living Abroad by Main Reason for Living Abroad and Age Group, 2024](data/final-report-tables/chapter-5/5.2.4-Population-Temporarily-Living-Abroad-by-Main-Reason-for-Living-Abroad-and-Age-Group,-2024)
- Table 5.2.5 - [Population Temporarily Living Abroad, by Main Reason for Living Abroad, Country of Residence and Sex,](data/final-report-tables/chapter-5/5.2.5-Population-Temporarily-Living-Abroad,-by-Main-Reason-for-Living-Abroad,-Country-of-Residence-and-Sex,)

### Chapter 6

- Table 6.1.1 - [Total Population, Sex ratio and the Percentage of Male and Female, 1946-2024](data/final-report-tables/chapter-6/6.1.1-Total-Population,-Sex-ratio-and-the-Percentage-of-Male-and-Female,-1946-2024)
- Table 6.1.2 - [Sex Ratio by Sector, 2024](data/final-report-tables/chapter-6/6.1.2-Sex-Ratio-by-Sector,-2024)
- Table 6.1.3 - [Population by Age Groups and Sex, 2012 and](data/final-report-tables/chapter-6/6.1.3-Population-by-Age-Groups-and-Sex,-2012-and)
- Table 6.1.4 - [Percentage Distribution of Population by Age Group, 1946–2024](data/final-report-tables/chapter-6/6.1.4-Percentage-Distribution-of-Population-by-Age-Group,-1946–2024)
- Table 6.1.5 - [Population Over and Below 18 Years of Age by Sector and District, 2024](data/final-report-tables/chapter-6/6.1.5-Population-Over-and-Below-18-Years-of-Age-by-Sector-and-District,-2024)
- Table 6.1.6 - [Elderly Population and Sex Ratio by Age Groups, 2012 and 2024](data/final-report-tables/chapter-6/6.1.6-Elderly-Population-and-Sex-Ratio-by-Age-Groups,-2012-and-2024)
- Table 6.1.7 - [Median Age of the Population, 1946-2024](data/final-report-tables/chapter-6/6.1.7-Median-Age-of-the-Population,-1946-2024)
- Table 6.1.8 - [Population Distribution by Ethnic Group, 2024](data/final-report-tables/chapter-6/6.1.8-Population-Distribution-by-Ethnic-Group,-2024)
- Table 6.1.9 - [Percentage Distribution of the Population by Ethnic Group and Province, 2024](data/final-report-tables/chapter-6/6.1.9-Percentage-Distribution-of-the-Population-by-Ethnic-Group-and-Province,-2024)
- Table 6.1.10 - [Population by Ethnic Group, 1911 - 2024 (in](data/final-report-tables/chapter-6/6.1.10-Population-by-Ethnic-Group,-1911---2024-(in)
- Table 6.1.11 - [Distribution of Population by Ethnic Group and District, 2012 and 2024](data/final-report-tables/chapter-6/6.1.11-Distribution-of-Population-by-Ethnic-Group-and-District,-2012-and-2024)
- Table 6.1.12 - [Percentage Distribution of Population by Ethnic Group and District, 2012 and 2024](data/final-report-tables/chapter-6/6.1.12-Percentage-Distribution-of-Population-by-Ethnic-Group-and-District,-2012-and-2024)
- Table 6.1.13 - [Population and Percentage Distribution by Sector and Religion, 2024](data/final-report-tables/chapter-6/6.1.13-Population-and-Percentage-Distribution-by-Sector-and-Religion,-2024)
- Table 6.1.14 - [Distribution of Population by Religion and District, 2012](data/final-report-tables/chapter-6/6.1.14-Distribution-of-Population-by-Religion-and-District,-2012)
- Table 6.1.15 - [Distribution of Population by Religion and District, 2024](data/final-report-tables/chapter-6/6.1.15-Distribution-of-Population-by-Religion-and-District,-2024)
- Table 6.2.1 - [Distribution of the Population Aged 5 Years and Over by Level of Physical and Mental Difficulties for EachFunctional Domain, 2024](data/final-report-tables/chapter-6/6.2.1-Distribution-of-the-Population-Aged-5-Years-and-Over-by-Level-of-Physical-and-Mental-Difficulties-for-EachFunctional-Domain,-2024)
- Table 6.2.2 - [Distribution of Persons Aged 5 Years and Over with Physical and Mental Difficulties by District and Difficulties,2024](data/final-report-tables/chapter-6/6.2.2-Distribution-of-Persons-Aged-5-Years-and-Over-with-Physical-and-Mental-Difficulties-by-District-and-Difficulties,2024)
- Table 6.2.3 - [Distribution of Persons Aged 5 Years and Over with Physical and Mental Difficulties by Age Group andDifficulties, 2024](data/final-report-tables/chapter-6/6.2.3-Distribution-of-Persons-Aged-5-Years-and-Over-with-Physical-and-Mental-Difficulties-by-Age-Group-andDifficulties,-2024)
- Table 6.2.4 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Sex and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.4-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Sex-and-Domain-of-Disability,-2024)
- Table 6.2.5 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Sector and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.5-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Sector-and-Domain-of-Disability,-2024)
- Table 6.2.6 - [Distribution of Persons Aged 5 Years and Over with Disabilities by District and Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.6-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-District-and-Domain-of-Disability,-2024)
- Table 6.2.7 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Age Group and Domain of Disability,](data/final-report-tables/chapter-6/6.2.7-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Age-Group-and-Domain-of-Disability,)
- Table 6.2.8 - [Distribution of Persons with a Single Disability and with Multiple Disabilities by Age Group, 2024](data/final-report-tables/chapter-6/6.2.8-Distribution-of-Persons-with-a-Single-Disability-and-with-Multiple-Disabilities-by-Age-Group,-2024)
- Table 6.2.9 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Marital Status and Sex, 2024](data/final-report-tables/chapter-6/6.2.9-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Sex,-2024)
- Table 6.2.10 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Highest Educational Qualification and Sex,2024](data/final-report-tables/chapter-6/6.2.10-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-and-Sex,2024)
- Table 6.2.11 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Marital Status and Domain of Disability,2024](data/final-report-tables/chapter-6/6.2.11-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Marital-Status-and-Domain-of-Disability,2024)
- Table 6.2.12 - [Distribution of Persons Aged 5 Years and Over with Disabilities by Highest Educational Qualification andDomain of Disability, 2024](data/final-report-tables/chapter-6/6.2.12-Distribution-of-Persons-Aged-5-Years-and-Over-with-Disabilities-by-Highest-Educational-Qualification-andDomain-of-Disability,-2024)
- Table 6.2.13 - [Economic Activities of Persons Aged 15 Years and Over with Disabilities, 2024](data/final-report-tables/chapter-6/6.2.13-Economic-Activities-of-Persons-Aged-15-Years-and-Over-with-Disabilities,-2024)
- Table 6.2.14 - [Economic Activity of Persons Aged 15 Years and Over with Disabilities by Domain of Disability, 2024](data/final-report-tables/chapter-6/6.2.14-Economic-Activity-of-Persons-Aged-15-Years-and-Over-with-Disabilities-by-Domain-of-Disability,-2024)
- Table 6.3.1 - [Number of Persons Reporting and Not Reporting Diseases, 2024](data/final-report-tables/chapter-6/6.3.1-Number-of-Persons-Reporting-and-Not-Reporting-Diseases,-2024)
- Table 6.3.2 - [Prevalence Rates of the Population with at Least One Non-Communicable Disease by Age Group and Sex,](data/final-report-tables/chapter-6/6.3.2-Prevalence-Rates-of-the-Population-with-at-Least-One-Non-Communicable-Disease-by-Age-Group-and-Sex,)
- Table 6.3.3 - [Number of Individuals Living with Non-Communicable Diseases and Prevalence Rates, 2024](data/final-report-tables/chapter-6/6.3.3-Number-of-Individuals-Living-with-Non-Communicable-Diseases-and-Prevalence-Rates,-2024)
- Table 6.3.4 - [Prevalence Rates of Non-Communicable Diseases by District, 2024](data/final-report-tables/chapter-6/6.3.4-Prevalence-Rates-of-Non-Communicable-Diseases-by-District,-2024)
- Table 6.3.5 - [Prevalence Rates of Self-Reported Illnesses by Sector, 2024](data/final-report-tables/chapter-6/6.3.5-Prevalence-Rates-of-Self-Reported-Illnesses-by-Sector,-2024)
- Table 6.3.6 - [Prevalence Rates of Non-Communicable Diseases by Sex, 2024](data/final-report-tables/chapter-6/6.3.6-Prevalence-Rates-of-Non-Communicable-Diseases-by-Sex,-2024)
- Table 6.3.7 - [Prevalence Rates of Non-Communicable Diseases by Age Group, 2024](data/final-report-tables/chapter-6/6.3.7-Prevalence-Rates-of-Non-Communicable-Diseases-by-Age-Group,-2024)
- Table 6.3.8 - [Prevalence Rates of Non-Communicable Diseases by Broad Age Groups, 2024](data/final-report-tables/chapter-6/6.3.8-Prevalence-Rates-of-Non-Communicable-Diseases-by-Broad-Age-Groups,-2024)
- Table 6.3.9 - [Prevalence Rates of Non-Communicable Diseases by Marital Status, 2024](data/final-report-tables/chapter-6/6.3.9-Prevalence-Rates-of-Non-Communicable-Diseases-by-Marital-Status,-2024)
- Table 6.3.10 - [Prevalence Rates of Non-Communicable Diseases by Ethnic Group, 2024](data/final-report-tables/chapter-6/6.3.10-Prevalence-Rates-of-Non-Communicable-Diseases-by-Ethnic-Group,-2024)
- Table 6.3.11 - [Prevalence Rates for the Population Aged 25 and Over by Highest Educational Qualification, 2024](data/final-report-tables/chapter-6/6.3.11-Prevalence-Rates-for-the-Population-Aged-25-and-Over-by-Highest-Educational-Qualification,-2024)
- Table 6.3.12 - [Prevalence Rates of NCDs by Employment Status, 2024](data/final-report-tables/chapter-6/6.3.12-Prevalence-Rates-of-NCDs-by-Employment-Status,-2024)

### Chapter 7

- Table 7.1 - [Population Aged 3 Years and Over by Sex and Educational Activity During the Census Reference Period,](data/final-report-tables/chapter-7/7.1-Population-Aged-3-Years-and-Over-by-Sex-and-Educational-Activity-During-the-Census-Reference-Period,)
- Table 7.2 - [Percentage Pistribution of Population Aged 03 Years and Over by Educational Activity and Age Group, 2024](data/final-report-tables/chapter-7/7.2-Percentage-Pistribution-of-Population-Aged-03-Years-and-Over-by-Educational-Activity-and-Age-Group,-2024)
- Table 7.3 - [Children Enrolled in Pre-school Education During the Reference Period by Age, 2024](data/final-report-tables/chapter-7/7.3-Children-Enrolled-in-Pre-school-Education-During-the-Reference-Period-by-Age,-2024)
- Table 7.4 - [Percentage of Children Receiving Preschool Education by Age Group and District, 2024](data/final-report-tables/chapter-7/7.4-Percentage-of-Children-Receiving-Preschool-Education-by-Age-Group-and-District,-2024)
- Table 7.5 - [Population Engaged in School Education During the Reference Period by Age Group and Sex,](data/final-report-tables/chapter-7/7.5-Population-Engaged-in-School-Education-During-the-Reference-Period-by-Age-Group-and-Sex,)
- Table 7.6 - [The Educational Level of the Population Age 25 Years and Over by Sex, 2012 and 2024](data/final-report-tables/chapter-7/7.6-The-Educational-Level-of-the-Population-Age-25-Years-and-Over-by-Sex,-2012-and-2024)
- Table 7.7 - [Percentage Distribution of Population Aged 25 and Over by Educational Level and District, 2012 and 2024](data/final-report-tables/chapter-7/7.7-Percentage-Distribution-of-Population-Aged-25-and-Over-by-Educational-Level-and-District,-2012-and-2024)
- Table 7.8 - [Language Literacy Rate by Census Year and Sex, 2024](data/final-report-tables/chapter-7/7.8-Language-Literacy-Rate-by-Census-Year-and-Sex,-2024)
- Table 7.9 - [Language Literacy Rate by Language and Age Group, 2024](data/final-report-tables/chapter-7/7.9-Language-Literacy-Rate-by-Language-and-Age-Group,-2024)
- Table 7.10 - [Language Literacy Rate by Language and District, 2024](data/final-report-tables/chapter-7/7.10-Language-Literacy-Rate-by-Language-and-District,-2024)
- Table 7.11 - [Language Literacy Rate by Language and Ethnic Group, 2012 and 2024](data/final-report-tables/chapter-7/7.11-Language-Literacy-Rate-by-Language-and-Ethnic-Group,-2012-and-2024)
- Table 7.12 - [Computer and Digital Literacy Rate by Sector,2024](data/final-report-tables/chapter-7/7.12-Computer-and-Digital-Literacy-Rate-by-Sector,2024)
- Table 7.13 - [Computer and Digital Literacy Rate by District, 2024](data/final-report-tables/chapter-7/7.13-Computer-and-Digital-Literacy-Rate-by-District,-2024)
- Table 7.14 - [Computer and Digital Literacy Rate by Age Group,](data/final-report-tables/chapter-7/7.14-Computer-and-Digital-Literacy-Rate-by-Age-Group,)

### Chapter 8

- Table 8.1 - [Economically Active and Inactive Population by Sex, 2024](data/final-report-tables/chapter-8/8.1-Economically-Active-and-Inactive-Population-by-Sex,-2024)
- Table 8.2 - [Economically Active Population, by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.2-Economically-Active-Population,-by-Sector-and-Sex,-2024)
- Table 8.3 - [Economically Active Population by Sex and Age Group, 2024](data/final-report-tables/chapter-8/8.3-Economically-Active-Population-by-Sex-and-Age-Group,-2024)
- Table 8.4 - [Labour Force Participation Rate by Age Group and Sex, 2024](data/final-report-tables/chapter-8/8.4-Labour-Force-Participation-Rate-by-Age-Group-and-Sex,-2024)
- Table 8.5 - [Labour Force Participation Rate, by Highest Educational Qualification Attained and Sex, 2024](data/final-report-tables/chapter-8/8.5-Labour-Force-Participation-Rate,-by-Highest-Educational-Qualification-Attained-and-Sex,-2024)
- Table 8.6 - [Employed Population by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.6-Employed-Population-by-Sector-and-Sex,-2024)
- Table 8.7 - [Employed Population, by Highest Educational Attainment and Sex, 2024](data/final-report-tables/chapter-8/8.7-Employed-Population,-by-Highest-Educational-Attainment-and-Sex,-2024)
- Table 8.8 - [Employed Population by Employment Status and Sex, 2024](data/final-report-tables/chapter-8/8.8-Employed-Population-by-Employment-Status-and-Sex,-2024)
- Table 8.9 - [Unemployed Population by Sector and Sex, 2024](data/final-report-tables/chapter-8/8.9-Unemployed-Population-by-Sector-and-Sex,-2024)
- Table 8.10 - [Employment Rate and Unemployment Rate by District, 2024](data/final-report-tables/chapter-8/8.10-Employment-Rate-and-Unemployment-Rate-by-District,-2024)
- Table 8.11 - [Economically Inactive Population by Main Reason for Inactivity, 2024](data/final-report-tables/chapter-8/8.11-Economically-Inactive-Population-by-Main-Reason-for-Inactivity,-2024)

### Chapter 9

- Table 9.1 - [by Marital Status, Age Group, and Sex, 2024](data/final-report-tables/chapter-9/9.1-by-Marital-Status,-Age-Group,-and-Sex,-2024)
- Table 9.2 - [Marital Status by Ethnic group and Sex,](data/final-report-tables/chapter-9/9.2-Marital-Status-by-Ethnic-group-and-Sex,)
- Table 9.3 - [Population Aged 15 Years and Over by Marital Status and Sex, 2012 and 2024](data/final-report-tables/chapter-9/9.3-Population-Aged-15-Years-and-Over-by-Marital-Status-and-Sex,-2012-and-2024)
- Table 9.4 - [Percentage of Never-Married Persons within the Age Group by Sex, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.4-Percentage-of-Never-Married-Persons-within-the-Age-Group-by-Sex,-1981,-2012,-and-2024)
- Table 9.5 - [Percentage of Married Population Aged 15 Years and Over by Age Group, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.5-Percentage-of-Married-Population-Aged-15-Years-and-Over-by-Age-Group,-1981,-2012,-and-2024)
- Table 9.6 - [Percentage of Widowed Population Aged 15 Years and over, 1981, 2012, and 2024](data/final-report-tables/chapter-9/9.6-Percentage-of-Widowed-Population-Aged-15-Years-and-over,-1981,-2012,-and-2024)
- Table 9.7 - [Number of Divorced or Separated Persons per 10,000 Population Aged 15 Years and Over, 1981, 2012, and](data/final-report-tables/chapter-9/9.7-Number-of-Divorced-or-Separated-Persons-per-10,000-Population-Aged-15-Years-and-Over,-1981,-2012,-and)
- Table 9.8 - [Mean Age at Marriage, 1953–2024](data/final-report-tables/chapter-9/9.8-Mean-Age-at-Marriage,-1953–2024)
- Table 9.9 - [Mean Age at Marriage by Sector, 2024](data/final-report-tables/chapter-9/9.9-Mean-Age-at-Marriage-by-Sector,-2024)
- Table 9.10 - [Mean Age at Marriage by District of Usual Residence, 2012 and 2024](data/final-report-tables/chapter-9/9.10-Mean-Age-at-Marriage-by-District-of-Usual-Residence,-2012-and-2024)
- Table 9.11 - [Mean Age at Marriage by Ethnic Group, 2024](data/final-report-tables/chapter-9/9.11-Mean-Age-at-Marriage-by-Ethnic-Group,-2024)
- Table 9.12 - [Percentage Distribution of Ever-Married Women Aged 15 Years and Over by the Number of Live Births perWoman and Sector, 2024](data/final-report-tables/chapter-9/9.12-Percentage-Distribution-of-Ever-Married-Women-Aged-15-Years-and-Over-by-the-Number-of-Live-Births-perWoman-and-Sector,-2024)
- Table 9.13 - [Number and Percentage Distribution of Married Women Aged 15–49 Years by Age Group, 2012 and 2024](data/final-report-tables/chapter-9/9.13-Number-and-Percentage-Distribution-of-Married-Women-Aged-15–49-Years-by-Age-Group,-2012-and-2024)
- Table 9.14 - [Age-Specific Fertility Rates (ASFR), 2012 and 2024](data/final-report-tables/chapter-9/9.14-Age-Specific-Fertility-Rates-(ASFR),-2012-and-2024)
- Table 9.15 - [Total Fertility Rate (TFR), 1981, 2012 and 2024](data/final-report-tables/chapter-9/9.15-Total-Fertility-Rate-(TFR),-1981,-2012-and-2024)
- Table 9.16 - [Age-Specific Fertility Rate (ASFR), Age-Specific Marital Fertility Rate (ASMFR), Total Fertility Rate (TFR) andTotal Marital Fertility Rate (TMFR)](data/final-report-tables/chapter-9/9.16-Age-Specific-Fertility-Rate-(ASFR),-Age-Specific-Marital-Fertility-Rate-(ASMFR),-Total-Fertility-Rate-(TFR)-andTotal-Marital-Fertility-Rate-(TMFR))
- Table 9.17 - [Gross Reproduction Rate Using TFR and TMFR](data/final-report-tables/chapter-9/9.17-Gross-Reproduction-Rate-Using-TFR-and-TMFR)

### Chapter 10

- Table 10.1 - [Percentage Distribution of Household Size by Sector, 2024](data/final-report-tables/chapter-10/10.1-Percentage-Distribution-of-Household-Size-by-Sector,-2024)
- Table 10.2 - [Percentage Distribution of the Number and of Households by Sector, District and Household Type, 2024](data/final-report-tables/chapter-10/10.2-Percentage-Distribution-of-the-Number-and-of-Households-by-Sector,-District-and-Household-Type,-2024)
- Table 10.3 - [Percentage Distribution of the Number of Household Heads by Ethnic group of the Head of Household and typeof Household, 2024](data/final-report-tables/chapter-10/10.3-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Ethnic-group-of-the-Head-of-Household-and-typeof-Household,-2024)
- Table 10.4 - [Percentage Distribution of the Number of Household Heads by Sex, Age Group, and Sector, 2024](data/final-report-tables/chapter-10/10.4-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sex,-Age-Group,-and-Sector,-2024)
- Table 10.5 - [Percentage Distribution of the Number of Household Heads by District, Sex, and Age Group, 2024](data/final-report-tables/chapter-10/10.5-Percentage-Distribution-of-the-Number-of-Household-Heads-by-District,-Sex,-and-Age-Group,-2024)
- Table 10.6 - [Percentage Distribution of the Number of Household Heads by Sector and Marital Status, 2024](data/final-report-tables/chapter-10/10.6-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sector-and-Marital-Status,-2024)
- Table 10.7 - [Percentage Distribution of the Number of Household Heads by Sex and Marital Status, 2024](data/final-report-tables/chapter-10/10.7-Percentage-Distribution-of-the-Number-of-Household-Heads-by-Sex-and-Marital-Status,-2024)
- Table 10.8 - [Percentage Distribution of Household Heads by Highest Educational Qualification Obtained and Sector, 2024](data/final-report-tables/chapter-10/10.8-Percentage-Distribution-of-Household-Heads-by-Highest-Educational-Qualification-Obtained-and-Sector,-2024)
- Table 10.9 - [Percentage Distribution of Household Heads by District and Highest Educational Qualification Obtained,](data/final-report-tables/chapter-10/10.9-Percentage-Distribution-of-Household-Heads-by-District-and-Highest-Educational-Qualification-Obtained,)
- Table 10.10 - [and Percentage Distribution of Individuals in One Person Households Aged 60 Years and Over, by Sexand Age Group, 2024](data/final-report-tables/chapter-10/10.10-and-Percentage-Distribution-of-Individuals-in-One-Person-Households-Aged-60-Years-and-Over,-by-Sexand-Age-Group,-2024)

### Chapter 11

- Table 11.1 - [Number of Occupied Housing Units by Sector, 2012 and 2024](data/final-report-tables/chapter-11/11.1-Number-of-Occupied-Housing-Units-by-Sector,-2012-and-2024)
- Table 11.2 - [Number of Occupied Housing Units & Permanently Closed/Vacant Housing Units by District, 2012 and 2024](data/final-report-tables/chapter-11/11.2-Number-of-Occupied-Housing-Units-&-Permanently-Closed/Vacant-Housing-Units-by-District,-2012-and-2024)
- Table 11.3 - [Number of Housing Units by the Year of Construction, 2024](data/final-report-tables/chapter-11/11.3-Number-of-Housing-Units-by-the-Year-of-Construction,-2024)
- Table 11.4 - [Tenure of Housing Units by Sector and District, 2024](data/final-report-tables/chapter-11/11.4-Tenure-of-Housing-Units-by-Sector-and-District,-2024)
- Table 11.5 - [Percentage of Housing Units Owned by Household Members and Sector, 2012 and 2024](data/final-report-tables/chapter-11/11.5-Percentage-of-Housing-Units-Owned-by-Household-Members-and-Sector,-2012-and-2024)
- Table 11.6 - [Percentage of Housing units by Materials Used to Construct Walls, Roofs and Floors,](data/final-report-tables/chapter-11/11.6-Percentage-of-Housing-units-by-Materials-Used-to-Construct-Walls,-Roofs-and-Floors,)
- Table 11.7 - [of Housing Units and Status of Housing Units, by Sector and District, 2024](data/final-report-tables/chapter-11/11.7-of-Housing-Units-and-Status-of-Housing-Units,-by-Sector-and-District,-2024)
- Table 11.8 - [in Housing Units by Sector, 2024](data/final-report-tables/chapter-11/11.8-in-Housing-Units-by-Sector,-2024)
- Table 11.9 - [Distribution of Households by Main Source of Drinking Water, 2024](data/final-report-tables/chapter-11/11.9-Distribution-of-Households-by-Main-Source-of-Drinking-Water,-2024)
- Table 11.10 - [Percentage Distribution of Households by Availability of Drinking Water Facility, by Sector and District,](data/final-report-tables/chapter-11/11.10-Percentage-Distribution-of-Households-by-Availability-of-Drinking-Water-Facility,-by-Sector-and-District,)
- Table 11.11 - [Distribution of Households in Sri Lanka's ability to Obtain Drinking Water Throughout the Year, 2024](data/final-report-tables/chapter-11/11.11-Distribution-of-Households-in-Sri-Lanka's-ability-to-Obtain-Drinking-Water-Throughout-the-Year,-2024)
- Table 11.12 - [Percentage of households Using Firewood and gas, by Sector and District,](data/final-report-tables/chapter-11/11.12-Percentage-of-households-Using-Firewood-and-gas,-by-Sector-and-District,)
- Table 11.13 - [Household Numbers and Percentages by Main and Secondary Energy/Fuel Type for Lighting, 2024](data/final-report-tables/chapter-11/11.13-Household-Numbers-and-Percentages-by-Main-and-Secondary-Energy/Fuel-Type-for-Lighting,-2024)
- Table 11.14 - [Percentage of Households Using Electricity and Kerosene as the Main Sources of Lighting, by ResidentialSector, 2012 and 2024](data/final-report-tables/chapter-11/11.14-Percentage-of-Households-Using-Electricity-and-Kerosene-as-the-Main-Sources-of-Lighting,-by-ResidentialSector,-2012-and-2024)
- Table 11.15 - [Percentage Distribution of Households by Type of Toilet Facilities, 2012 and 2024](data/final-report-tables/chapter-11/11.15-Percentage-Distribution-of-Households-by-Type-of-Toilet-Facilities,-2012-and-2024)
- Table 11.16 - [Percentage Distribution of Type of Toilet Used by households by Sector and District, 2024](data/final-report-tables/chapter-11/11.16-Percentage-Distribution-of-Type-of-Toilet-Used-by-households-by-Sector-and-District,-2024)
- Table 11.17 - [Distribution of Households by the Main Method of Disposing Solid Waste, 2024](data/final-report-tables/chapter-11/11.17-Distribution-of-Households-by-the-Main-Method-of-Disposing-Solid-Waste,-2024)
- Table 11.18 - [Percentage Distribution of Households by the Main Method of Disposing Liquid Waste, 2024](data/final-report-tables/chapter-11/11.18-Percentage-Distribution-of-Households-by-the-Main-Method-of-Disposing-Liquid-Waste,-2024)
- Table 11.19 - [Percentage Distribution of Households Using Communication Technology Equipment and Vehicles by Sector,2024](data/final-report-tables/chapter-11/11.19-Percentage-Distribution-of-Households-Using-Communication-Technology-Equipment-and-Vehicles-by-Sector,2024)

### Chapter 12

- Table 12.1 - [Myer’s Index by Sex, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-12/12.1-Myer’s-Index-by-Sex,-1981,-2001,-2012-and-2024)
- Table 12.2 - [Deviations of Terminal Digits of Reported Age, 2012 and](data/final-report-tables/chapter-12/12.2-Deviations-of-Terminal-Digits-of-Reported-Age,-2012-and)
- Table 12.3 - [Myers' Index by District and Sex, 2012, 2024](data/final-report-tables/chapter-12/12.3-Myers'-Index-by-District-and-Sex,-2012,-2024)
- Table 12.4 - [Whipple’s Index by Sex, 1981, 2001, 2012 and 2024](data/final-report-tables/chapter-12/12.4-Whipple’s-Index-by-Sex,-1981,-2001,-2012-and-2024)
- Table 12.5 - [Whipple's Index by District and Sex, 2012 and 2024](data/final-report-tables/chapter-12/12.5-Whipple's-Index-by-District-and-Sex,-2012-and-2024)



### Final Report Build Status

| status | status_label | n | p |
| :-- | :-- | --: | --: |
| **2**/5 | 🔴 Raw data is difficult to parse | **21** | **14.8%** |
| **4**/5 | 🟡 Lanka data is missing | **84** | **59.2%** |
| **5**/5 | ✅ All Stages Complete | **37** | **26.1%** |

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
