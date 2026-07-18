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
    def lanka_data_pass(self):
        return self.lanka_data_metadata.get("lanka_data_pass", False)
