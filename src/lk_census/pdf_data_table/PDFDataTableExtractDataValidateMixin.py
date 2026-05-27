import os

from gig_future import Ent, EntType
from utils_future import JSONFile, Log

log = Log("PDFDataTable")


class PDFDataTableExtractDataValidateMixin:

    @staticmethod
    def __validate_ents_without_data__(d_list: list[dict]) -> list[dict]:
        parsed_id_set = set([d["region_id"] for d in d_list])
        errors = []
        for ent_type in [EntType.COUNTRY, EntType.DISTRICT, EntType.DSD]:
            ent_id_set = set([ent.id for ent in Ent.list_from_type(ent_type)])
            non_parsed = ent_id_set - parsed_id_set
            if not non_parsed:
                log.debug(f"✅All {ent_type.name}s parsed successfully.")
                continue
            log.error(
                f"⁉️ {len(non_parsed)}" + f" {ent_type.name}s not parsed:"
            )
            for ent_id in non_parsed:
                ent = Ent.from_id(ent_id)
                log.error(f" - {ent.id} {ent.name}")
                errors.append(
                    dict(
                        region_id=ent_id,
                        region_name=ent.name,
                        ent_type=ent_type.name,
                    )
                )
        return errors

    @staticmethod
    def __validate_data_without_ents__(d_list: list[dict]) -> list[dict]:
        d_list_without_ents = [
            d for d in d_list if d.get("region_id", "").endswith("XX")
        ]
        if not d_list_without_ents:
            log.debug("✅All region names mapped to Ents successfully.")
        else:
            log.error(
                f"⁉️ {len(d_list_without_ents)} region names"
                + " could not be mapped to Ents:"
            )
            for d in d_list_without_ents:
                log.error(f" - {d['region_id']} {d['region_name']}")
        return [
            dict(region_id=d["region_id"], region_name=d["region_name"])
            for d in d_list_without_ents
        ]

    @staticmethod
    def __validate_totals__(d_list: list[dict]) -> list[dict]:
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
        return [
            dict(
                region_id=d["region_id"],
                region_name=d["region_name"],
                total=d["total"],
                total_from_fields=d["total_from_fields"],
            )
            for d in total_mismatch_d_list
        ]

    def validate(self, d_list: list[dict]):
        d_list_with_ents = [
            d for d in d_list if not d.get("region_id", "").endswith("XX")
        ]
        errors_data_without_ents = self.__validate_data_without_ents__(d_list)
        errors_ents_without_data = self.__validate_ents_without_data__(
            d_list_with_ents
        )
        errors_totals = self.__validate_totals__(d_list)

        results = [
            dict(
                name="data_without_ents",
                status="pass" if not errors_data_without_ents else "fail",
                error_count=len(errors_data_without_ents),
                errors=errors_data_without_ents,
            ),
            dict(
                name="ents_without_data",
                status="pass" if not errors_ents_without_data else "fail",
                error_count=len(errors_ents_without_data),
                errors=errors_ents_without_data,
            ),
            dict(
                name="totals",
                status="pass" if not errors_totals else "fail",
                error_count=len(errors_totals),
                errors=errors_totals,
            ),
        ]
        validations_path = os.path.join(self.dir_table, "validations.json")
        os.makedirs(self.dir_table, exist_ok=True)
        JSONFile(validations_path).write(results)
        log.debug(f"Wrote validations to {validations_path}")
