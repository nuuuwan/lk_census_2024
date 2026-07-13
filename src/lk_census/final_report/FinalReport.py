from lk_census.final_report.FinalReportMetadataMixin import (
    FinalReportMetadataMixin,
)
from lk_census.final_report.table import FinalReportTable
from utils_future import Log

log = Log("FinalReport")


class FinalReport(FinalReportMetadataMixin):

    @staticmethod
    def parse_tables():
        tables = FinalReportTable.list()
        for table in tables:
            table.build()

    @staticmethod
    def build():
        FinalReport.extract_table_index()
        FinalReport.build_table_metadata()
        FinalReport.parse_tables()
