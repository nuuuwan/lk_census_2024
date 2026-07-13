import os

from utils_future import JSONFile, PDFFile


class FinalReportConstants:
    MIN_VALID_TABLE_PAGE_NUM, MAX_VALID_TABLE_PAGE_NUM = 6, 205
    PAGE_OFFSET = 17

    PDF_FILE = PDFFile(os.path.join("original_docs", "CPH2024_Final_Eng.pdf"))

    TABLE_METADATA_FILE = JSONFile(
        os.path.join("derived_docs", "final-report-index.metadata.json")
    )

    TABLE_INDEX_START_PAGE, TABLE_INDEX_END_PAGE = 11, 13
    TABLE_INDEX_PDF_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.pdf")
    )
    TABLE_INDEX_TXT_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.txt")
    )
