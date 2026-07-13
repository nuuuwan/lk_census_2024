import os

from lk_census.final_report.FinalReportConstants import FinalReportConstants
from lk_census.final_report.FinalReportMetadataMixin import (
    FinalReportMetadataMixin,
)
from lk_census.final_report.FinalReportTable import FinalReportTable
from utils_future import Log, PDFFile

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
