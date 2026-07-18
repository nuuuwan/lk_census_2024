import os

from ds import RegionValueAdapter
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
        if self.lanka_data_file.exists() and not force:
            return

        d_list = self.data_list
        datumset = RegionValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            time_str=self.time_str,
            measurement_class_name=self.measurement_class_name,
        )
        self.lanka_data_file.write(datumset.to_data())
        log.info(f"Wrote {self.lanka_data_file}")

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
