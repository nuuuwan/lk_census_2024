import os
from functools import cached_property

from gig_future import Ent, EntType
from utils_future import JSONFile, Log, Parse

log = Log("FinalReportTableDataMixin")


class FinalReportTableDataMixin:
    MIN_N_DATA_LIST = 10

    @property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    @property
    def fields_file(self):
        return JSONFile(os.path.join(self.dir_data, "fields.json"))

    @cached_property
    def is_summable(self):
        if not self.fields_file.exists:
            return False
        return self.fields.get("is_summable", "true").lower() == "true"

    @cached_property
    def is_expandable(self):
        if not self.fields_file.exists:
            return False
        return self.fields.get("is_expandable", "true").lower() == "true"

    @cached_property
    def fields(self):
        if not self.fields_file.exists:
            return {}
        return self.fields_file.read()

    @cached_property
    def primary_keys(self):
        return self.fields.get("primary_keys", ["district_name"])

    @cached_property
    def other_keys(self):
        return self.fields.get("other_keys", [])

    @cached_property
    def error_key(self):
        return self.fields.get("error_key", "error")

    @staticmethod
    def _get_region(region_name):

        regions = Ent.list_from_name_fuzzy(
            name_fuzzy=region_name,
            filter_ent_type=EntType.DISTRICT,
        )
        if len(regions) != 1:
            raise ValueError(
                f"Expected exactly one region for '{region_name}',"
                + f" found {str(regions)}"
            )
        return regions[0]

    def _build_data_item(self, raw_data):
        if not raw_data[0] or raw_data[0].startswith("*"):
            return None

        for keyword in [
            "accounting",
            "census",
            "district",
            "family",
            "note",
            "number",
            "over",
            "person",
            "province",
            "residence",
            "sri lanka",
            "term",
            "total",
            "usual",
            "year",
        ]:
            if keyword in raw_data[0].lower():
                return None

        if "\n" in raw_data[0]:
            words = raw_data[0].strip().split("\n")
            raw_data = [words[0].strip(), words[-1].strip()] + raw_data[1:]
        elif " " * 4 in raw_data[0]:
            words = raw_data[0].strip().split(" ")
            raw_data[0] = words[0].strip()
            raw_data[1] = words[-1]

        fields = self.fields
        assert fields != {}
        n_fields = len(self.primary_keys) + len(self.other_keys)
        if len(raw_data) != n_fields:
            return None

        d = {}

        primary_key_value = raw_data[0]
        region = FinalReportTableDataMixin._get_region(primary_key_value)

        d = dict(
            region_id=region.id,
            region_name=region.name,
            region_ent_type=EntType.DISTRICT.name,
        )

        values = {}
        total_value = None
        for i_key, key in enumerate(self.other_keys, start=1):
            region_id = None
            if key.startswith("_"):
                continue
            value = raw_data[i_key]
            if key.startswith("p_"):
                value = Parse.percent(value)
            elif key.startswith("is_"):
                value = Parse.boolean(value)
            elif key.endswith("_district_name"):
                name = str(value).strip()
                regions = Ent.list_from_name_fuzzy(
                    name, filter_ent_type=EntType.DISTRICT
                )
                region = regions[0]
                region_id = region.id
            elif key == "total_value":
                total_value = Parse.int(value)
            else:
                value = Parse.int(value)
            if key.startswith("p_") and total_value is not None:
                value = int(round(value * total_value, 0))
                values[key[2:]] = value
            elif key not in ["total_value"]:
                values[key] = value

            if region_id:
                values[key[:-5] + "_id"] = region_id
        d["values"] = values

        if self.is_summable:
            if total_value:
                total_value_from_values = sum(values.values())
                error = total_value - total_value_from_values
                values[self.error_key] = error

            d["total_value"] = (
                sum(values.values()) if not total_value else total_value
            )
        return d

    def _aggregate(self, parent_id, d_list_for_parent):
        parent = Ent.from_id(parent_id)
        d_parent = dict(
            region_id=parent_id,
            region_name=parent.name,
            region_ent_type=EntType.from_id(parent_id).name,
        )
        parent_values = {}
        for d in d_list_for_parent:
            for k, v in d["values"].items():
                if k not in parent_values:
                    parent_values[k] = 0
                parent_values[k] += v

        d_parent["values"] = parent_values
        if self.is_summable:
            d_parent["total_value"] = sum(parent_values.values())
        return d_parent

    def _expand_to_parent_types(self, d_list):
        # Map
        parent_id_to_d_list = {}
        for ent_type in [EntType.COUNTRY, EntType.PROVINCE, EntType.ED]:
            parent_id_key = ent_type.name.lower() + "_id"
            for d in d_list:
                child_region_id = d["region_id"]
                child_region = Ent.from_id(child_region_id)
                if ent_type == EntType.COUNTRY:
                    parent_id = "LK"
                else:
                    parent_id = child_region.d[parent_id_key]
                if parent_id not in parent_id_to_d_list:
                    parent_id_to_d_list[parent_id] = []
                parent_id_to_d_list[parent_id].append(d)

        # Reduce
        for parent_id, d_list_for_parent in parent_id_to_d_list.items():
            d = self._aggregate(parent_id, d_list_for_parent)
            d_list.append(d)

        return d_list

    def build_data(self, force=False):
        if self.data_file.exists and not force:
            return

        raw_data_list = self.raw_data_list
        if not raw_data_list:
            return

        fields = self.fields
        if not fields:
            return

        d_list = []
        for raw_data in raw_data_list:
            d = self._build_data_item(raw_data)
            if d:
                d_list.append(d)
        d_list.sort(key=lambda x: x["region_id"])

        if len(d_list) < self.MIN_N_DATA_LIST:
            raise ValueError(
                f"[{self}] Expected >={self.MIN_N_DATA_LIST} data items,"
                + f" found only {len(d_list)}"
            )

        if self.is_expandable:
            d_list = self._expand_to_parent_types(d_list)

        self.data_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.data_file}")

    @property
    def data_list(self):
        if not self.data_file.exists:
            return None
        return self.data_file.read()
