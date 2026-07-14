import os
from functools import cached_property

from utils_future import JSONFile


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
        if not self.lanka_data_metadata_file.exists:
            return {}
        return self.lanka_data_metadata_file.read()

    @cached_property
    def what_label(self):
        what_label = self.lanka_data_metadata.get("what_label")
        if not what_label or what_label.strip() == "":
            return None
        if " " in what_label or len(what_label) > 40:
            return None
        return what_label

    @cached_property
    def when_label(self):
        return self.lanka_data_metadata.get("when_label", "2024")

    @property
    def is_lanka_data_metadata_complete(self):
        return self.what_label is not None
