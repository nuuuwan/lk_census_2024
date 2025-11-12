import os
import re
from dataclasses import dataclass

from utils import File, Log

from lk_census.data_table.DataTableExtractDataMixin import (
    DataTableExtractDataMixin,
)
from lk_census.data_table.DataTableLoaderMixin import DataTableLoaderMixin
from lk_census.data_table.DataTablePDFMixin import DataTablePDFMixin
from lk_census.original_doc.OriginalDoc import OriginalDoc

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
    README_PATH = os.path.join(DIR_DATA, "README.md")

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
            data_table.save_subset_pdf()
            data_table.extract_data()
        cls.build_readme()

    @classmethod
    def build_readme(cls):
        lines = ["# Data Tables", ""]
        for data_table in cls.list_all():
            line = (
                f"- [{data_table.table_title}]"
                + f"({data_table.dir_table.replace('data/', '')})"
            )
            lines.append(line)
        readme_file = File(cls.README_PATH)
        readme_file.write_lines(lines)
        log.info(f" Wrote {readme_file}")
