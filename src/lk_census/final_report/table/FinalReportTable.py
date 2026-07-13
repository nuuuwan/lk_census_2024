import os
from functools import cached_property

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

    @cached_property
    def is_complicated(self):
        return self.table_num in [
            "5.2.2",  # Triple Row
            "5.2.5",  # Col Sum
            "6.1.6",  # Data error?
            "6.1.13",  # Double Row
            "6.2.1",  # Double Row
            "6.2.4",  # Double Row
            "6.2.5",  # Double Row
            "6.2.13",  # Double Row
            "6.2.14",  # Double Row
        ]

    STATUS_LABELS = {
        0: "⚫️ Original PDF is missing",
        1: "🔴 Raw data is missing",
        2: "🟠 Raw data is difficult to parse",
        3: "🟡 Data is missing",
        4: "✅ Complete",
    }

    # flake8: noqa: C901
    @cached_property
    def build_status(self):
        if not self.original_pdf_file.exists:
            return 0

        if not self.raw_data_file.exists:
            return 1

        if self.is_complicated:
            return 2

        if not self.data_file.exists:
            return 3

        return 4
