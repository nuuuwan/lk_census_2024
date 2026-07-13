from gig_future import Ent, EntType
from utils_future import Log

log = Log("FinalReportTableDataRowMixin")


class FinalReportTableDataRowMixin:

    @staticmethod
    def _get_region(region_name):
        regions = Ent.list_from_name_fuzzy(
            name_fuzzy=region_name,
            filter_ent_type=EntType.DISTRICT,
            min_fuzz_ratio=80,
        )
        if len(regions) != 1:
            log.error(
                f"Expected exactly one region for '{region_name}',"
                + f" found {str(regions)}"
            )
            return None
        return regions[0]

    def _normalize_raw_data(self, raw_data):
        if "\n" in raw_data[0]:
            words = raw_data[0].strip().split("\n")
            return [words[0].strip(), words[-1].strip()] + raw_data[1:]
        if " " * 4 in raw_data[0]:
            words = raw_data[0].strip().split(" ")
            raw_data[0] = words[0].strip()
            raw_data[1] = words[-1]

        if len(raw_data) != self.n_fields:
            log.warning(
                "Wrong number of fields:"
                + f" {self.n_fields} != {len(raw_data)}: {raw_data}"
            )
            return None

        return raw_data

    def _build_primary_keys_for_district(self, first_cell):
        region = self._get_region(first_cell)
        if region is None:
            log.warning(f"No region for: {first_cell}")
            return None
        return dict(
            region_id=region.id,
            region_name=region.name,
            region_ent_type=EntType.DISTRICT.name,
        )

    def _build_primary_keys(self, first_cell):
        if self.primary_keys == ["district_name"]:
            return self._build_primary_keys_for_district(first_cell)

        first_primary_key = self.primary_keys[0]
        if first_cell.lower() in ["total", "", "ethnic group"]:
            return None
        return {first_primary_key: first_cell}

    # flake8: noqa: E501
    def _build_data_item(self, raw_data):
        raw_data = self._normalize_raw_data(raw_data)
        if raw_data is None:
            return None
        d_primary_part = self._build_primary_keys(raw_data[0])
        if d_primary_part is None:
            return None
        d_other_part = self._build_other_keys(raw_data[1:])
        if d_other_part is None:
            return None

        d = d_primary_part | d_other_part
        return d
