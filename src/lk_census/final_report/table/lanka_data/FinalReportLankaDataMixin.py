import os

from ds import (
    DimToTimeToValueAdapter,
    DimToValueAdapter,
    GenericValueAdapter,
    RegionValueAdapter,
)
from utils_future import JSONFile, Log

from lk_census.final_report.table.lanka_data.FinalReportLankaMetaDataMixin import (
    FinalReportLankaMetaDataMixin,
)

log = Log("FinalReportLankaDataMixin")


class FinalReportLankaDataMixin(FinalReportLankaMetaDataMixin):
    @property
    def lanka_data_file(self) -> JSONFile:
        return JSONFile(
            os.path.join(
                self.dir_data,
                "lanka_data.json",
            )
        )

    def build_lanka_data(self, force=False):
        pass

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
