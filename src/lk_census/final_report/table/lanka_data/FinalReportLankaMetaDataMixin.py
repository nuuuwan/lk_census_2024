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
    def dim_class_name(self):
        return self.lanka_data_metadata.get("dim_class_name")

    @cached_property
    def dim_class_key(self):
        return self.lanka_data_metadata.get("dim_class_key")

    @cached_property
    def value_label(self):
        return self.lanka_data_metadata.get("value_label")

    @cached_property
    def is_lanka_data_metadata_complete_for_dim1_etc(
        self,
    ):
        return (
            self.entity_class_name is not None
            and self.dim_class_name is not None
            and self.dim_class_key is not None
            and self.value_label is not None
            and self.adapter_class_name is not None
        )

    # A3) DimToValue
    @cached_property
    def value_class_name(self):
        return self.lanka_data_metadata.get("value_class_name")

    @cached_property
    def is_lanka_data_metadata_complete_for_dim_to_value(
        self,
    ):
        return (
            self.entity_class_name is not None
            and self.dim_class_name is not None
            and self.dim_class_key is not None
            and self.value_label is not None
            and self.value_class_name is not None
            and self.adapter_class_name is not None
        )

    # ---

    @cached_property
    def is_lanka_data_metadata_complete(self):

        _value = {
            "RegionValueAdapter": self.is_lanka_data_metadata_complete_for_region_value_adapter,
            "DimToTimeToValueAdapter": self.is_lanka_data_metadata_complete_for_dim1_etc,
            "DimToValueAdapter": self.is_lanka_data_metadata_complete_for_dim_to_value,
        }.get(self.adapter_class_name)

        if _value is not None:
            return _value

        raise ValueError(
            f"Unknown adapter_class_name: {self.adapter_class_name}"
        )
