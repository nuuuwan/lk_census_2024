import os

from ds import StandardTableAdapter
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
        if not self.data_list:
            return
        if not self.is_lanka_data_fields_complete:
            return
        if self.lanka_data_pass:
            return

        datumset = StandardTableAdapter.build_datumset(
            d_list=self.data_list,
            entity_class_name=self.entity_class_name,
            time_value=self.time_value,
            row_dim_class_name=self.row_dim_class_name,
            row_dim_key=self.row_dim_key,
            col_dim_class_name=self.col_dim_class_name,
            cell_label=self.cell_label,
            cell_class_name=self.cell_class_name,
        )
        lanka_data = datumset.to_data()
        if lanka_data != {}:
            self.lanka_data_file.write(lanka_data)
            log.info(f"Wrote {self.lanka_data_file}")
        else:
            log.error(f"Empty Lankadata for {self}")

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
