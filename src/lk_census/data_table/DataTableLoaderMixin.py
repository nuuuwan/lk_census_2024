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

    HOUSING_A9 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A9. Number of housing units by main material"
        + " used for walls construction"
        + " at district level and DSDs",
        (128, 143),
        [
            "brick",
            "cement_block",
            "granite_or_cube_stones",
            "cabook",
            "pressed_soil_bricks",
            "mud_or_warichchi",
            "kadjan_or_palmyrah",
            "plank_or_metal_sheet_or_asbestos",
            "zinc_aluminium_sheets",
            "other",
            "not_relevant",
        ],
    )

    HOUSING_A10 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A10. Number of housing units by main material"
        + " used for roof construction"
        + " at district level and DSDs",
        (144, 161),
        [
            "tile",
            "asbestos",
            "concrete",
            "zinc_aluminium_sheets",
            "metal_sheets",
            "kadjan_or_palmyrah_or_straw",
            "other",
            "not_relevant",
        ],
    )

    HOUSING_A11 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A11. Number of households"
        + " by main material"
        + " used for floor construction"
        + " at district level and DSDs",
        (162, 181),
        [
            "cement",
            "terrazzo_or_tile_or_granite_or_wood_or_titanium",
            "concrete",
            "mud",
            "wood",
            "sand",
            "other",
            "not_relevant",
        ],
    )

    HOUSING_A12 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A12. Number of households by main source of drinking water"
        + " at district level and DSDs",
        (182, 200),
        [
            # ground_water (5)
            "ground_water-_protected_well",
            "ground_water-semi_protected_well",
            "ground_water-unprotected_well",
            "ground_water-tube_well",
            "ground_water-spring_or_fountain",
            # pipe_borne_water (4)
            "pipe_borne_water-national_water_supply_and_drainage_board",
            "pipe_borne_water-local_authority",
            "pipe_borne_water-community_based_organizations",
            "pipe_borne_water-private_water_supply_project",
            # other_sources (6)
            "other-tank_or_river_or_stream",
            "other-rain_water",
            "other-bottled_water",
            "other-filter_water",
            "other-bowser",
            "other-other",
        ],
    )

    HOUSING_A13 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A13. Number of households by source of lighting"
        + " at district level and DSDs",
        (201, 222),
        [
            "electricity-from_national_grid",
            "electricity-from_rural_hydro_power_project",
            "other-kerosene_lamp",
            "other-solar_power_grid_connected",
            "other-solar_power_standalone",
            "other-bio_gas",
            "other-generator",
            "other-other",
        ],
    )

    HOUSING_A14 = (
        "Basic-Housing-Information"
        + "-by-Districts-and-Divisional-Secretary-Divisions",
        "A14. Number of households using toilet facilities"
        + " at district level and DSDs",
        (223, 247),
        [
            "within_the_unit-exclusively_for_the_household",
            "within_the_unit-sharing_with_another_household",
            "outside_the_unit-exclusively_for_the_household",
            "outside_the_unit-sharing_with_another_household",
            "other-no_toilet_but_sharing_with_another_household",
            "other-common_or_public_toilet",
            "other-not_using_a_toilet",
        ],
    )

    @classmethod
    def list_all(cls):
        for t in [
            cls.POPULATION_A4,
            cls.POPULATION_A5,
            cls.POPULATION_A6,
            cls.POPULATION_A7,
            cls.HOUSING_A8,
            cls.HOUSING_A9,
            cls.HOUSING_A10,
            cls.HOUSING_A11,
            cls.HOUSING_A12,
            cls.HOUSING_A13,
            cls.HOUSING_A14,
        ]:
            yield cls(*t)
