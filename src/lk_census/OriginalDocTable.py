import os
import re
from dataclasses import dataclass

from utils import Log

from lk_census.OriginalDocTableExtractDataMixin import (
    OriginalDocTableExtractDataMixin,
)
from lk_census.OriginalDocTableLoaderMixin import OriginalDocTableLoaderMixin
from lk_census.OriginalDocTablePDFMixin import OriginalDocTablePDFMixin

log = Log("OriginalDocTable")


@dataclass
class OriginalDocTable(
    OriginalDocTableLoaderMixin,
    OriginalDocTablePDFMixin,
    OriginalDocTableExtractDataMixin,
):
    doc_name: str
    table_title: str
    pages: tuple[int, int]
    field_list: list[str]

    DIR_DATA = "data"

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
            self.doc_name,
            self.name_safe,
        )

    @classmethod
    def extract_all(cls):

        for original_doc_table in cls.list_all():
            os.makedirs(original_doc_table.dir_table, exist_ok=True)
            original_doc_table.save_subset_pdf()
            original_doc_table.extract_data()
