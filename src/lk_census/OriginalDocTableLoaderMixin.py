class OriginalDocTableLoaderMixin:
    @classmethod
    def list_all(cls) -> list["OriginalDocTable"]:
        return [
            # cls(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A4. Migrant population"
            #     + " by reason for migrating according to districts",
            #     (110, 111),
            #     [],
            # ),
            # cls(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A5. Population by sex, age and district according to DSD",
            #     (112, 136),
            #     [
            #         "sex-male",
            #         "sex-female",
            #         "age-under-15",
            #         "age-15-to-59",
            #         "age-60-to-64",
            #         "age-65-and-over",
            #     ],
            # ),
            # cls(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A6. Population by ethnicity and district according to DSD",
            #     (137, 161),
            #     [
            #         "sinhalese",
            #         "sri_lanka_tamil",
            #         "indian_tamil_or_malaiyaga_thamilar",
            #         "sri_lanka_moor_or_muslim",
            #         "burgher",
            #         "malay",
            #         "sri_lanka_chetty",
            #         "bharatha",
            #         "veddhas",
            #         "other",
            #     ],
            # ),
            cls(
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
            ),
        ]
