import os
from functools import cached_property

from utils_future import JSONFile, Log

log = Log("FinalReportLankaMetaDataMixin")


class FinalReportLankaMetaDataMixin:
    @cached_property
    def lanka_data_pass(self):
        return self.fields.get("lanka_data_pass", False)

    # Fields

    @cached_property
    def entity_class_name(self):
        return self.fields.get("entity_class_name", None)

    @cached_property
    def time_value(self):
        return self.fields.get("time_value", None)

    @cached_property
    def row_dim_class_name(self):
        return self.fields.get("row_dim_class_name", None)

    @cached_property
    def row_dim_key(self):
        return self.fields.get("row_dim_key", None)

    @cached_property
    def col_dim_class_name(self):
        return self.fields.get("col_dim_class_name", None)

    @cached_property
    def cell_class_name(self):
        return self.fields.get("cell_class_name", None)

    @cached_property
    def cell_label(self):
        return self.fields.get("cell_label", None)

    @cached_property
    def is_lanka_data_fields_complete(self):
        return bool(
            self.entity_class_name
            and self.time_value
            and self.row_dim_class_name
            and self.row_dim_key
            and self.col_dim_class_name
            and self.cell_label
            and self.cell_class_name
        )
