import os
from functools import cached_property

from gig_future import Ent, EntType
from utils_future import JSONFile, Log, Parse

log = Log("FinalReportTableDataMixin")


class FinalReportTableDataMixin:
    @property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    @property
    def fields_file(self):
        return JSONFile(os.path.join(self.dir_data, "fields.json"))

    @cached_property
    def fields(self):
        if not self.fields_file.exists:
            return {}
        return self.fields_file.read()

    @cached_property
    def primary_keys(self):
        return self.fields.get("primary_keys", [])

    @cached_property
    def other_keys(self):
        return self.fields.get("other_keys", [])

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
        if "total" in raw_data[0].lower():
            return None

        fields = self.fields
        assert fields != {}
        n_fields = len(self.primary_keys) + len(self.other_keys)
        if len(raw_data) != n_fields:
            log.debug(f"{raw_data=}")
            raise ValueError(f"[{self}] {n_fields} != {len(raw_data)} Fields")

        d = {}

        primary_key_value = raw_data[0]
        region = FinalReportTableDataMixin._get_region(primary_key_value)
        d = dict(
            region_id=region.id,
            region_name=region.name,
            region_ent_type=EntType.DISTRICT.name,
        )

        values = {}
        for i_key, key in enumerate(self.other_keys, start=1):
            value = raw_data[i_key]
            value = Parse.int(value)
            key = key.replace("-", " ").replace(" ", "_").lower()
            values[key] = value
        d["values"] = values
        d["total_value"] = sum(values.values())
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
            for other_key in self.other_keys:
                if other_key not in parent_values:
                    parent_values[other_key] = 0
                value = d["values"][other_key]
                parent_values[other_key] += value

        d_parent["values"] = parent_values
        d_parent["total"] = sum(parent_values.values())
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

    def build_data(self):
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
        d_list = self._expand_to_parent_types(d_list)

        self.data_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.data_file}")

    @property
    def data_list(self):
        if not self.data_file.exists:
            return None
        return self.data_file.read()
