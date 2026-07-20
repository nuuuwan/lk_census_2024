import os
from functools import cached_property

from ds import StandardTableAdapter
from utils_future import JSONFile, Log

log = Log("XLSXDataTableLankaDataMixin")


class XLSXDataTableLankaDataMixin:
    @cached_property
    def entity_class_name(self):
        return self.data_table_id.split("-")[0]

    @cached_property
    def col_dim_class_name(self):
        return self.data_table_id.split("-")[1]

    @property
    def lanka_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "lanka_data.json"))

    def build_lanka_data(self, force=False):
        if self.lanka_data_file.exists() and not force:
            return

        datumset = StandardTableAdapter.build_datumset(
            d_list=self.data_list,
            entity_class_name=self.entity_class_name,
            time_value="2024",
            row_dim_class_name="Province",
            row_dim_key="region_id",
            col_dim_class_name=self.col_dim_class_name,
            cell_label="Count",
            cell_class_name="Int",
        )

        data = datumset.to_data()
        self.lanka_data_file.write(data)
        log.info(f"Wrote {self.lanka_data_file}")

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return None
        return self.lanka_data_file.read()
