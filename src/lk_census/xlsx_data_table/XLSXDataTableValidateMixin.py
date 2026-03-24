from gig import Ent, EntType
from utils import Log

log = Log("XLSXDataTable")

_GIG_GND_IDS = {ent.id for ent in Ent.list_from_type(EntType.GND)}


class XLSXDataTableValidateMixin:

    def _validate_parent_child_totals(self, d_list: list[dict]):
        """Validation 1: each non-GND region's field values equal the sum of
        its direct children's field values."""
        by_id = {d["region_id"]: d for d in d_list}
        errors = 0
        for d in d_list:
            rid = d["region_id"]
            # Only check regions that have children in the dataset
            children = [
                x for x in d_list if _is_direct_child(x["region_id"], rid)
            ]
            if not children:
                continue
            for field in self.field_list:
                parent_val = d.get(field, 0)
                child_sum = sum(c.get(field, 0) for c in children)
                if parent_val != child_sum:
                    log.error(
                        f"⁉️ Parent-child mismatch for {rid} field={field}: "
                        f"parent={parent_val}, sum_of_children={child_sum}"
                    )
                    errors += 1
        if errors == 0:
            log.debug("✅ All parent-child field totals are consistent.")

    def _validate_all_gig_gnds_present(self, d_list: list[dict]):
        """Validation 2: every GND in gig has a data row."""
        data_gnd_ids = {
            d["region_id"] for d in d_list if d["region_ent_type"] == "GND"
        }
        missing = _GIG_GND_IDS - data_gnd_ids
        if not missing:
            log.debug(
                f"✅ All {len(_GIG_GND_IDS):,} gig GNDs are present in data."
            )
        else:
            log.error(f"⁉️ {len(missing):,} gig GNDs missing from data:")
            for gnd_id in sorted(missing)[:10]:
                ent = Ent.from_id(gnd_id)
                log.error(f"   - {gnd_id} {ent.name}")
            if len(missing) > 10:
                log.error(f"   ... and {len(missing) - 10} more")

    def _validate_gnds_are_valid(self, d_list: list[dict]):
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

    def _validate_total_field(self, d_list: list[dict]):
        """Validation 4: when field_list contains 'total', the sum of the
        remaining fields equals 'total' for every row."""
        if "total" not in self.field_list:
            return
        other_fields = [f for f in self.field_list if f != "total"]
        if not other_fields:
            return
        errors = 0
        for d in d_list:
            total = d.get("total", 0)
            field_sum = sum(d.get(f, 0) for f in other_fields)
            if total != field_sum:
                log.error(
                    f"⁉️ Total mismatch for {d['region_id']} "
                    f"{d['region_name']}: total={total}, "
                    f"sum_of_fields={field_sum}"
                )
                errors += 1
        if errors == 0:
            log.debug("✅ All 'total' fields equal the sum of other fields.")

    def validate(self, d_list: list[dict]):
        log.debug(f"Validating {self.name_safe} ({len(d_list)} rows) ...")
        self._validate_parent_child_totals(d_list)
        self._validate_all_gig_gnds_present(d_list)
        self._validate_gnds_are_valid(d_list)
        self._validate_total_field(d_list)


def _is_direct_child(child_id: str, parent_id: str) -> bool:
    """Return True if child_id is a direct child of parent_id in the
    administrative hierarchy."""
    if parent_id == "LK":
        # Direct children of country are provinces: "LK-1", "LK-2", ...
        parts = child_id.split("-")
        return len(parts) == 2 and len(parts[1]) == 1
    parts_p = parent_id.split("-")
    parts_c = child_id.split("-")
    if len(parts_p) != 2 or len(parts_c) != 2:
        return False
    suffix_p = parts_p[1]
    suffix_c = parts_c[1]
    if len(suffix_p) == 1:
        # Province → District: "LK-1" parent, "LK-11".."LK-19" children
        return suffix_c.startswith(suffix_p) and len(suffix_c) == 2
    if len(suffix_p) == 2:
        # District → DSD: "LK-11" parent, "LK-1103" children
        return suffix_c.startswith(suffix_p) and len(suffix_c) == 4
    if len(suffix_p) == 4:
        # DSD → GND: "LK-1103" parent, "LK-1103005" children
        return suffix_c.startswith(suffix_p) and len(suffix_c) == 7
    return False
