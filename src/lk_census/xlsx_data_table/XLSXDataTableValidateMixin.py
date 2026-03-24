import os

from gig import Ent, EntType
from utils import JSONFile, Log

log = Log("XLSXDataTable")

_GIG_GND_IDS = {ent.id for ent in Ent.list_from_type(EntType.GND)}


def _get_parent_id(region_id: str) -> str | None:
    """Return the parent region_id in the hierarchy, or None for country."""
    if region_id == "LK":
        return None
    parts = region_id.split("-")
    if len(parts) != 2:
        return None
    suffix = parts[1]
    if len(suffix) == 7:  # GND → DSD
        return f"LK-{suffix[:4]}"
    if len(suffix) == 4:  # DSD → District
        return f"LK-{suffix[:2]}"
    if len(suffix) == 2:  # District → Province
        return f"LK-{suffix[0]}"
    if len(suffix) == 1:  # Province → Country
        return "LK"
    return None


class XLSXDataTableValidateMixin:

    def _validate_parent_child_totals(self, d_list: list[dict]) -> dict:
        """Validation 1: each non-GND region's field values equal the sum of
        its direct children's field values."""
        by_id = {d["region_id"]: d for d in d_list}
        children_map: dict[str, list[dict]] = {}
        for d in d_list:
            parent_id = _get_parent_id(d["region_id"])
            if parent_id and parent_id in by_id:
                children_map.setdefault(parent_id, []).append(d)

        errors = []
        for parent_id, children in children_map.items():
            parent = by_id[parent_id]
            for field in self.field_list:
                parent_val = parent.get(field, 0)
                child_sum = sum(c.get(field, 0) for c in children)
                if parent_val != child_sum:
                    errors.append(
                        dict(
                            region_id=parent_id,
                            field=field,
                            parent=parent_val,
                            sum_of_children=child_sum,
                        )
                    )
                    log.error(
                        f"⁉️ Parent-child mismatch for {parent_id} field={field}: "
                        f"parent={parent_val}, sum_of_children={child_sum}"
                    )
        if not errors:
            log.debug("✅ All parent-child field totals are consistent.")
        return dict(
            name="parent_child_totals",
            status="pass" if not errors else "fail",
            error_count=len(errors),
            errors=errors,
        )

    def _validate_all_gig_gnds_present(self, d_list: list[dict]) -> dict:
        """Validation 2: every GND in gig has a data row."""
        data_gnd_ids = {
            d["region_id"] for d in d_list if d["region_ent_type"] == "GND"
        }
        missing = sorted(_GIG_GND_IDS - data_gnd_ids)
        if not missing:
            log.debug(
                f"✅ All {len(_GIG_GND_IDS):,} gig GNDs are present in data."
            )
        else:
            log.error(f"⁉️ {len(missing):,} gig GNDs missing from data:")
            for gnd_id in missing[:10]:
                ent = Ent.from_id(gnd_id)
                log.error(f"   - {gnd_id} {ent.name}")
            if len(missing) > 10:
                log.error(f"   ... and {len(missing) - 10} more")
        errors = [
            dict(region_id=gnd_id, region_name=Ent.from_id(gnd_id).name)
            for gnd_id in missing
        ]
        return dict(
            name="all_gig_gnds_present",
            status="pass" if not errors else "fail",
            error_count=len(errors),
            errors=errors,
        )

    def _validate_gnds_are_valid(self, d_list: list[dict]) -> dict:
        """Validation 3: every GND row in data is a valid gig GND."""
        invalid = [
            d
            for d in d_list
            if d["region_ent_type"] == "GND"
            and d["region_id"] not in _GIG_GND_IDS
        ]
        if not invalid:
            log.debug("✅ All GND rows are valid gig GNDs.")
        else:
            log.error(f"⁉️ {len(invalid):,} GND rows not found in gig:")
            for d in invalid[:10]:
                log.error(f"   - {d['region_id']} {d['region_name_in_data']}")
            if len(invalid) > 10:
                log.error(f"   ... and {len(invalid) - 10} more")
        errors = [
            dict(
                region_id=d["region_id"],
                region_name_in_data=d["region_name_in_data"],
            )
            for d in invalid
        ]
        return dict(
            name="gnds_are_valid",
            status="pass" if not errors else "fail",
            error_count=len(errors),
            errors=errors,
        )

    def _validate_total_field(self, d_list: list[dict]) -> dict | None:
        """Validation 4: when field_list contains 'total', the sum of the
        remaining fields equals 'total' for every row."""
        if "total" not in self.field_list:
            return None
        other_fields = [f for f in self.field_list if f != "total"]
        if not other_fields:
            return None
        errors = []
        for d in d_list:
            total = d.get("total", 0)
            field_sum = sum(d.get(f, 0) for f in other_fields)
            if total != field_sum:
                errors.append(
                    dict(
                        region_id=d["region_id"],
                        region_name=d["region_name"],
                        total=total,
                        sum_of_fields=field_sum,
                    )
                )
                log.error(
                    f"⁉️ Total mismatch for {d['region_id']} "
                    f"{d['region_name']}: total={total}, "
                    f"sum_of_fields={field_sum}"
                )
        if not errors:
            log.debug("✅ All 'total' fields equal the sum of other fields.")
        return dict(
            name="total_field",
            status="pass" if not errors else "fail",
            error_count=len(errors),
            errors=errors,
        )

    def validate(self, d_list: list[dict]):
        log.debug(f"Validating {self.name_safe} ({len(d_list)} rows) ...")
        results = [
            self._validate_parent_child_totals(d_list),
            self._validate_all_gig_gnds_present(d_list),
            self._validate_gnds_are_valid(d_list),
            self._validate_total_field(d_list),
        ]
        results = [r for r in results if r is not None]
        validations_path = os.path.join(self.dir_table, "validations.json")
        os.makedirs(self.dir_table, exist_ok=True)
        JSONFile(validations_path).write(results)
        log.debug(f"Wrote validations to {validations_path}")
