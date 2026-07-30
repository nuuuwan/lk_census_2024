# Population and Average Annual Growth Rate by District, Census Years 1981- 2024

![CPH](https://img.shields.io/badge/CPH-2024-blue)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30-green)

*Table 3.3, Final Report, 2024 Census of Population and Housing, Department of Census and Statistics, Sri Lanka*

## Structured Data formatted for [Lanka Data API](https://github.com/nuuuwan/lanka_data)

```json
{
    "Person": {
        "Time:1981": {
            "District:colombo": {
                "Count": "Int:1675847"
            },
            "District:gampaha": {
                "Count": "Int:1367813"
            },
            "District:kalutara": {
                "Count": "Int:823964"
            },
            "District:kandy": {
                "Count": "Int:1032335"
            },
            "District:matale": {
                "Count": "Int:352860"
            },
            "District:nuwara_eliya": {
                "Count": "Int:583716"
            },
            "District:galle": {
                "Count": "Int:805403"
            },
            "District:matara": {
                "Count": "Int:642235"
            },
            "District:hambantota": {
                "Count": "Int:421277"
            },
...
```

- Source File: [lanka_data.json (6.8 KB)](../../../../data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District-Census-Years-1981-2024/lanka_data.json)

## Structured Data (similar to original layout)

```json
[
    {
        "region_id": "LK-11",
        "region_name": "Colombo",
        "region_ent_type": "district",
        "values": {
            "population_1981": 1675847,
            "population_2001": 2239696,
            "population_2012": 2324349,
            "population_2024": 2375415
        }
    },
    {
        "region_id": "LK-12",
        "region_name": "Gampaha",
        "region_ent_type": "district",
        "values": {
            "population_1981": 1367813,
            "population_2001": 2060470,
            "population_2012": 2304833,
            "population_2024": 2436142
        }
    },
    {
        "region_id": "LK-13",
        "region_name": "Kalutara",
        "region_ent_type": "district",
        "values": {
            "population_1981": 823964,
            "population_2001": 1065635,
...
```

- Source File: [data.json (14.0 KB)](../../../../data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District-Census-Years-1981-2024/data.json)

## Raw Data (directly scraped from PDF)

```json
[
    [
        "Sri Lanka",
        "19812 \n14,846,274",
        "20013 \n18,797,257",
        "2012 \n   20,359,439    21,781,800",
        "2024",
        "1981-2001 \n1.2",
        "1981-2012 \n1.0",
        "2001-2012 \n0.7",
        "2012-2024 \n0.5"
    ],
    [
        "Colombo",
        "1,675,847",
        "2,239,696",
        "2,324,349",
        "2,375,415",
        "1.4",
        "1.1",
        "0.3",
        "0.2"
    ],
    [
        "Gampaha",
        "1,367,813",
        "2,060,470",
        "2,304,833",
        "2,436,142",
        "2.0",
...
```
- Source File: [raw_data.json (3.3 KB)](../../../../data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District-Census-Years-1981-2024/raw_data.json)

## Original PDF Page

![Download the original PDF](../../../../data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District-Census-Years-1981-2024/original.png)

- Source File: [original.pdf (121.6 KB)](../../../../data/final-report-tables/chapter-3/3.3-Population-and-Average-Annual-Growth-Rate-by-District-Census-Years-1981-2024/original.pdf)

## Source

- <https://www.statistics.gov.lk/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf#page=69>

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
