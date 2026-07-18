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

    @cached_property
    def entity_class_name(self):
        return self.lanka_data_metadata.get("entity_class_name")

    @cached_property
    def measurement_class_name(self):
        return self.lanka_data_metadata.get("measurement_class_name")

    @cached_property
    def time_str(self):
        return self.lanka_data_metadata.get("time_str")

    @cached_property
    def is_lanka_data_metadata_complete(self):
        return (
            self.entity_class_name is not None
            and self.measurement_class_name is not None
            and self.time_str is not None
        )
