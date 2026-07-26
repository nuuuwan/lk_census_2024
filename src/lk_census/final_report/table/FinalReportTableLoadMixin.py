import os

from lk_census.final_report.FinalReportConstants import FinalReportConstants


class FinalReportTableLoadMixin:

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

    @property
    def dir_data2(self):
        dir_data2 = os.path.join(
            "data",
            "final-report-tables",
            f"chapter-{self.chapter_num}",
            self.table_id2,
        )
        os.makedirs(dir_data2, exist_ok=True)
        return dir_data2

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

    @classmethod
    def from_table_num(cls, table_num):
        tables = cls.list()
        for table in tables:
            if table.table_num == table_num:
                return table
        raise ValueError(f"Table with table_num {table_num} not found")
