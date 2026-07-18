import os
from functools import cached_property

from utils_future import JSONFile, Log

log = Log("FinalReportLankaMetaDataMixin")


class FinalReportLankaMetaDataMixin:
    @property
    def lanka_data_metadata_file(self) -> JSONFile:
        return JSONFile(
            os.path.join(
                self.dir_data,
                "lanka_data_metadata.json",
            )
        )

    @cached_property
    def lanka_data_metadata(self):
        if not self.lanka_data_metadata_file.exists():
            return {}
        return self.lanka_data_metadata_file.read()

    # Common to all Adapters
    @cached_property
    def entity_class_name(self):
        return self.lanka_data_metadata.get("entity_class_name")

    @cached_property
    def adapter_class_name(self):
        return self.lanka_data_metadata.get(
            "adapter_class_name", "RegionValueAdapter"
        )

    # A1) RegionValueAdapter

    @cached_property
    def measurement_class_name(self):
        return self.lanka_data_metadata.get("measurement_class_name")

    @cached_property
    def time_str(self):
        return self.lanka_data_metadata.get("time_str")

    @cached_property
    def is_lanka_data_metadata_complete_for_region_value_adapter(self):
        return (
            self.entity_class_name is not None
            and self.measurement_class_name is not None
            and self.time_str is not None
        )

    # A2) DimToTimeToValueAdapter

    @cached_property
    def dim1_class_name(self):
        return self.lanka_data_metadata.get("dim1_class_name")

    @cached_property
    def dim1_class_key(self):
        return self.lanka_data_metadata.get("dim1_class_key")

    @cached_property
    def value_label(self):
        return self.lanka_data_metadata.get("value_label")

    @cached_property
    def is_lanka_data_metadata_complete_for_dim1_etc(
        self,
    ):
        return (
            self.entity_class_name is not None
            and self.dim1_class_name is not None
            and self.dim1_class_key is not None
            and self.value_label is not None
            and self.adapter_class_name is not None
        )

    # ---

    @cached_property
    def is_lanka_data_metadata_complete(self):
        if self.adapter_class_name == "RegionValueAdapter":
            return (
                self.is_lanka_data_metadata_complete_for_region_value_adapter
            )
        if self.adapter_class_name == "DimToTimeToValueAdapter":
            return self.is_lanka_data_metadata_complete_for_dim1_etc
        raise ValueError(
            f"Unknown adapter_class_name: {self.adapter_class_name}"
        )
