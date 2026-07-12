from dataclasses import dataclass


@dataclass
class FinalReportTableBase:
    table_num: str
    table_name: str
    page_num: int

    @property
    def chapter_num(self):
        return int(self.table_num.split(".")[0])

    @property
    def table_id(self):
        return f"{self.table_num}-{self.table_name.replace(' ', '-')}"
