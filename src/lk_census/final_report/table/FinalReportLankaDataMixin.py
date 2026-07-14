import os

from utils_future import JSONFile


class FinalReportLankaDataMixin:
    @property
    def lanka_data_file(self) -> JSONFile:
        return JSONFile(
            os.path.join(
                self.dir_data,
                "lanka_data.json",
            )
        )

    def build_lanka_data(self):
        pass
