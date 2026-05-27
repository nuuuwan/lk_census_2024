import os
import re
from dataclasses import dataclass

from lk_census.xlsx_data_table.XLSXDataTableExtractDataMixin import \
    XLSXDataTableExtractDataMixin
from lk_census.xlsx_data_table.XLSXDataTableLoaderMixin import \
    XLSXDataTableLoaderMixin
from utils_future import Log

log = Log("XLSXDataTable")


@dataclass
class XLSXDataTable(
    XLSXDataTableLoaderMixin,
    XLSXDataTableExtractDataMixin,
):
    doc_name: str
    table_title: str
    column_offset: int
    field_list: list[str]

    DIR_DATA = "data"

    @property
    def n_fields(self) -> int:
        return len(self.field_list)

    @property
    def name_safe(self):
        name_safe = re.sub(r"\s+", " ", self.table_title)
        name_safe = name_safe.replace(" ", "-")
        name_safe = "".join(
            char for char in name_safe if char.isalnum() or char == "-"
        )
        return name_safe

    @property
    def dir_table(self):
        return os.path.join(
            self.DIR_DATA,
            self.doc_name,
            self.name_safe,
        )

    @classmethod
    def extract_all(cls):
        for data_table in cls.list_all():
            data_table.extract_data()
