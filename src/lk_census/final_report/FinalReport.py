from utils_future import Log

from lk_census.final_report.FinalReportMetadataMixin import (
    FinalReportMetadataMixin,
)
from lk_census.final_report.table import FinalReportTable

log = Log("FinalReport")


class FinalReport(FinalReportMetadataMixin):

    @staticmethod
    def parse_tables(force):
        tables = FinalReportTable.list()
        for table in tables:
            table.build(force)

    @staticmethod
    def clean_all():
        for table in FinalReportTable.list():
            table.clean()

    @staticmethod
    def build_all(force=False):
        FinalReport.extract_table_index()
        FinalReport.build_table_metadata()
        FinalReport.parse_tables(force)
