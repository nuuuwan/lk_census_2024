import os
from functools import cached_property

from utils_future import JSONFile


class FinalReportTableDataFieldsMixin:
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
        return (
            self.fields.get("primary_keys")
            or [self.fields.get("primary_key")]
            or ["district_name"]
        )

    @cached_property
    def is_first_primary_key_expandable(self):
        first_primary_key = self.primary_keys[0]
        return first_primary_key in ["district_name"]

    @cached_property
    def other_keys(self):
        return self.fields.get("other_keys", [])

    @cached_property
    def error_key(self):
        return self.fields.get("error_key", "_rounding_error")

    @cached_property
    def n_fields(self) -> int:
        return len(self.primary_keys) + len(self.other_keys)

    @cached_property
    def is_summable(self):
        return self.fields.get("is_summable", True)

    @cached_property
    def is_expandable(self):
        return (
            self.fields.get("is_expandable", True)
            and self.is_first_primary_key_expandable
        )

    @cached_property
    def total_description(self):
        return self.fields.get("total_description")

    @cached_property
    def null_cols(self):
        return self.fields.get("null_cols", [])

    @cached_property
    def has_complete_fields(self):
        return len(self.other_keys) > 0

    @cached_property
    def raw_table_index_list(self):
        return self.fields.get("raw_table_index_list", [])
