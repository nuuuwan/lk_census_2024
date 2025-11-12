class DataTableLoaderMixin:
    POPULATION_A4 = (
        "Basic-Population-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A4. Migrant population"
        + " by reason for migrating according to districts",
        (110, 111),
        [],
    )
    POPULATION_A5 = (
        "Basic-Population-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A5. Population by sex, age and district according to DSD",
        (112, 136),
        [
            "sex-male",
            "sex-female",
            "age-under-15",
            "age-15-to-59",
            "age-60-to-64",
            "age-65-and-over",
        ],
    )
    POPULATION_A6 = (
        "Basic-Population-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A6. Population by ethnicity and district according to DSD",
        (137, 161),
        [
            "sinhalese",
            "sri_lanka_tamil",
            "indian_tamil_or_malaiyaga_thamilar",
            "sri_lanka_moor_or_muslim",
            "burgher",
            "malay",
            "sri_lanka_chetty",
            "bharatha",
            "veddhas",
            "other",
        ],
    )
    POPULATION_A7 = (
        "Basic-Population-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A7. Population by religion and district according to DSD",
        (162, 185),
        [
            "buddhist",
            "hindu",
            "islam",
            "roman_catholic",
            "other_christian",
            "other",
        ],
    )

    HOUSING_A8 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A8. Number of housing units by housing unit structure"
        + " at district level and DSDs",
        (109, 127),
        [
            "single_house_single_storeyed",
            "single_house_two_storeyed",
            "single_house_more_than_two_storeyed",
            "attached_house_1st_floor",
            "attached_house_2nd_floor",
            "attached_house_3rd_or_4th_floor",
            "attached_house_5th_to_10th_floor",
            "attached_house_11th_to_19th_floor",
            "attached_house_from_20th_floor_or_more",
            "other",
        ],
    )

    @classmethod
    def list_all(cls):
        for t in [
            # cls.POPULATION_A4,
            # cls.POPULATION_A5,
            # cls.POPULATION_A6,
            # cls.POPULATION_A7,
            cls.HOUSING_A8,
        ]:
            yield cls(*t)
