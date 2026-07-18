import os

from ds import RegionValueAdapter
from utils_future import JSONFile, Log, Parse, String

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
        d_list = self.data_list
        RegionValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            year=self.year,
            measurement_class_name=self.measurement_class_name,
        )

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
