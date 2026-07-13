import os

from lk_census.final_report.FinalReportConstants import FinalReportConstants
from lk_census.final_report.table.FinalReportTableBase import (
    FinalReportTableBase,
)
from lk_census.final_report.table.FinalReportTableDataMixin import (
    FinalReportTableDataMixin,
)
from lk_census.final_report.table.FinalReportTablePDFMixin import (
    FinalReportTablePDFMixin,
)
from lk_census.final_report.table.FinalReportTableRawDataMixin import (
    FinalReportTableRawDataMixin,
)
from utils_future import Log

log = Log("FinalReportTable")


class FinalReportTable(
    FinalReportTableBase,
    FinalReportTablePDFMixin,
    FinalReportTableRawDataMixin,
    FinalReportTableDataMixin,
):

    @property
    def dir_data(self):
        dir_data = os.path.join(
            "data",
            "final-report-tables",
            f"chapter-{self.chapter_num}",
            self.table_id,
        )
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @classmethod
    def from_dict(cls, d):
        return cls(
            table_num=d["table_num"],
            table_name=d["table_name"],
            page_num=int(d["page_num"]),
            i_table_on_page=int(d["i_table_on_page"]),
            total_tables_on_page=int(d["total_tables_on_page"]),
            has_page_multiple_tables=bool(d["has_page_multiple_tables"]),
        )

    @classmethod
    def list(cls):
        d_list = FinalReportConstants.TABLE_METADATA_FILE.read()
        return [cls.from_dict(d) for d in d_list]

    def build(self):
        self.build_original_pdf()
        self.build_raw_data()
        self.build_data()

    def _build_status_from_files(self):
        files = [
            self.original_pdf_file,
            self.raw_data_file,
            self.data_file,
        ]
        for i, f in enumerate(files):
            if not f.exists:
                return i
        return len(files)

    @property
    def build_status(self):
        return self._build_status_from_files()
