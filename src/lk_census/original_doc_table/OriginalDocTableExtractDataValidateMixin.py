from gig import Ent, EntType
from utils import Log

log = Log("OriginalDocTable")


class OriginalDocTableExtractDataValidateMixin:
    @staticmethod
    def validate(d_list: list[dict]):
        d_list_without_ents = [
            ent for ent in d_list if ent.get("region_id", "").endswith("XX")
        ]

        if not d_list_without_ents:
            log.debug("✅ All region names mapped to Ents successfully.")
        else:
            log.error(
                f"⁉️ {len(d_list_without_ents)} region names"
                + " could not be mapped to Ents:"
            )
            for d in d_list_without_ents:
                log.error(f" - {d['region_id']} {d['region_name']}")

        parsed_id_set = set([d["region_id"] for d in d_list])
        for ent_type in [EntType.COUNTRY, EntType.DISTRICT, EntType.DSD]:
            ent_id_set = set([ent.id for ent in Ent.list_from_type(ent_type)])
            non_parsed_district_set = ent_id_set - parsed_id_set
            if non_parsed_district_set:
                log.error(
                    f"⁉️ {len(non_parsed_district_set)}"
                    + f" {ent_type.name}s not parsed:"
                )
                for ent_id in non_parsed_district_set:
                    ent = Ent.from_id(ent_id)
                    log.error(f" - {ent.id} {ent.name}")
            else:
                log.debug(f"✅All {ent_type.name}s parsed successfully.")

        total_mismatch_d_list = []
        for d in d_list:
            total = d["total"]
            total_from_fields = sum([v for v in list(d.values())[5:]])
            if total != total_from_fields and 2 * total != total_from_fields:
                total_mismatch_d_list.append(
                    d | dict(total_from_fields=total_from_fields)
                )

        if not total_mismatch_d_list:
            log.debug("✅ All totals match sum of fields.")
        else:
            log.error(
                f"⁉️ {len(total_mismatch_d_list)} rows with"
                + " total mismatch errors:"
            )
            for d in total_mismatch_d_list:
                log.error(
                    f" - {d['region_id']} {d['region_name']}:"
                    + f" {d['total']} != {d['total_from_fields']}"
                )

        d_list_population_mismatch = []
        MAX_POPULATION_CHANGE_RATIO = 1.5
        for d in d_list:
            if "XX" in d["region_id"]:
                continue
            ent = Ent.from_id(d["region_id"])
            total = d["total"]
            total_from_ent_2012 = ent.population
            population_change_ratio = total / total_from_ent_2012

            if (
                population_change_ratio > MAX_POPULATION_CHANGE_RATIO
                or population_change_ratio < 1 / MAX_POPULATION_CHANGE_RATIO
            ):
                d_list_population_mismatch.append(
                    d
                    | dict(
                        total_from_ent_2012=total_from_ent_2012,
                        population_change_ratio=population_change_ratio,
                    )
                )

        if len(d_list_population_mismatch) == 0:
            log.debug("✅ All population changes within expected range.")
        else:
            log.error(
                f"⚠️ {len(d_list_population_mismatch)} rows with"
                + " large population changes:"
            )
            for d in d_list_population_mismatch:
                population_change_ratio = d["population_change_ratio"]
                log.error(
                    f" - {d['region_id']} {d['region_name']}:"
                    + f" {d['total_from_ent_2012']:,} -> {d['total']:,}"
                    + f" ({population_change_ratio:.2}x)"
                )
