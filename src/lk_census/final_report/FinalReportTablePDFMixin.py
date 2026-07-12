import os

from lk_census.final_report.FinalReportConstants import FinalReportConstants
from utils_future import PDFFile


class FinalReportTablePDFMixin:
    @property
    def original_pdf_file(self):
        return PDFFile(os.path.join(self.dir_data, "original.pdf"))

    def build_original_pdf(self, force=False):
        if self.original_pdf_file.exists and not force:
            return
        FinalReportConstants.PDF_FILE.extract_subset(
            self.page_num + FinalReportConstants.PAGE_OFFSET,
            self.page_num + FinalReportConstants.PAGE_OFFSET,
            self.original_pdf_file,
        )
