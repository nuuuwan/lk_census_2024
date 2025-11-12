import os
import re
from dataclasses import dataclass

from utils import Log

from lk_census.data_table.DataTableExtractDataMixin import \
    DataTableExtractDataMixin
from lk_census.data_table.DataTableLoaderMixin import DataTableLoaderMixin
from lk_census.data_table.DataTablePDFMixin import DataTablePDFMixin
from lk_census.OriginalDoc import OriginalDoc

log = Log("DataTable")


@dataclass
class DataTable(
    DataTableLoaderMixin,
    DataTablePDFMixin,
    DataTableExtractDataMixin,
):
    original_doc: OriginalDoc
    table_title: str
    pages: tuple[int, int]
    field_list: list[str]

    DIR_DATA = "data"

    @property
    def is_population_table(self) -> bool:
        return self.original_doc.doc_name.startswith("Basic-Population")

    @property
    def n_fields(self) -> int:
        return len(self.field_list)

    @property
    def page_start(self):
        return self.pages[0]

    @property
    def page_end(self):
        return self.pages[1]

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
            self.original_doc.doc_name,
            self.name_safe,
        )

    @classmethod
    def extract_all(cls):

        for data_table in cls.list_all():
            os.makedirs(data_table.dir_table, exist_ok=True)
            data_table.save_subset_pdf()
            data_table.extract_data()
