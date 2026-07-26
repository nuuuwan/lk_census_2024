import re
from dataclasses import dataclass

from lk_census.final_report.FinalReportConstants import FinalReportConstants


@dataclass
class FinalReportTableBase:
    table_num: str
    table_name: str
    page_num: int
    i_table_on_page: int
    total_tables_on_page: int
    has_page_multiple_tables: bool

    @property
    def chapter_num(self):
        return int(self.table_num.split(".")[0])

    @property
    def table_name_cleaned(self):
        x = self.table_name
        # replace all non alpha numeric or '-' with '-'
        x = re.sub(r"[^a-zA-Z0-9-]", "-", x)
        x = re.sub(r"-+", "-", x)
        return x

    @property
    def table_id(self):
        return f"{self.table_num}-{self.table_name_cleaned}"

    def __str__(self):
        return f"FinalReportTable({self.table_id})"

    def __repr__(self):
        return str(self)

    URL_FINAL_REPORT = (
        "https://www.statistics.gov.lk"
        + "/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf"
    )

    @property
    def actual_page_num(self):
        return self.page_num + FinalReportConstants.PAGE_OFFSET

    @property
    def source_url(self):
        return f"{self.URL_FINAL_REPORT}#page={self.actual_page_num}"

    @property
    def source_description(self):
        return ", ".join(
            [
                f"Table {self.table_num}",
                "Final Report",
                "2024 Census of Population and Housing",
                "Department of Census and Statistics, Sri Lanka",
            ]
        )
