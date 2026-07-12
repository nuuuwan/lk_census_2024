import os

from lk_census.final_report.FinalReportConstants import FinalReportConstants
from lk_census.final_report.FinalReportTable import FinalReportTable
from utils_future import Log, Parse, PDFFile

log = Log("FinalReport")


class FinalReport:

    TABLE_INDEX_START_PAGE, TABLE_INDEX_END_PAGE = 11, 13
    TABLE_INDEX_PDF_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.pdf")
    )
    TABLE_INDEX_TXT_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.txt")
    )

    @staticmethod
    def extract_table_index(force=False):
        if not FinalReport.TABLE_INDEX_PDF_FILE.exists or force:
            FinalReportConstants.PDF_FILE.extract_subset(
                FinalReport.TABLE_INDEX_START_PAGE,
                FinalReport.TABLE_INDEX_END_PAGE,
                FinalReport.TABLE_INDEX_PDF_FILE,
            )

        if not FinalReport.TABLE_INDEX_TXT_FILE.exists or force:
            FinalReport.TABLE_INDEX_PDF_FILE.to_text_file(
                FinalReport.TABLE_INDEX_TXT_FILE
            )

    @staticmethod
    def clean(text):
        text = text.replace(".", "")
        return text.strip()

    @staticmethod
    def build_table_metadata():

        d_list = []
        lines = FinalReport.TABLE_INDEX_TXT_FILE.read_lines()
        for i_line, line in enumerate(lines, start=0):
            if not line.startswith("Table"):
                continue
            words = line.strip().split(" ")
            page_num = Parse.int(words[-1])

            if page_num is None or not (
                FinalReportConstants.MIN_VALID_TABLE_PAGE_NUM
                <= page_num
                <= FinalReportConstants.MAX_VALID_TABLE_PAGE_NUM
            ):
                new_line = line.strip() + lines[i_line + 1].strip()
                words = new_line.strip().split(" ")
                page_num = Parse.int(words[-1])
                assert (
                    page_num is not None
                ), f"Failed to parse page number from line: {new_line}"
                assert (
                    FinalReportConstants.MIN_VALID_TABLE_PAGE_NUM
                    <= page_num
                    <= FinalReportConstants.MAX_VALID_TABLE_PAGE_NUM
                ), (
                    f"Page number {page_num}"
                    + f" out of valid range in line: {new_line}"
                )

            table_num = words[1]
            table_name = FinalReport.clean(" ".join(words[3:-2]))
            d = dict(
                table_num=table_num, table_name=table_name, page_num=page_num
            )
            d_list.append(d)
        FinalReportConstants.TABLE_METADATA_FILE.write(d_list)
        log.info(
            f"Wrote {
                len(d_list)} tables to {
                FinalReportConstants.TABLE_METADATA_FILE}"
        )

    @staticmethod
    def parse_tables():
        tables = FinalReportTable.list()
        for table in tables:
            table.build()

    @staticmethod
    def parse():
        FinalReport.extract_table_index()
        FinalReport.build_table_metadata()
        FinalReport.parse_tables()
