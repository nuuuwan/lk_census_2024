import os

from utils_future import PDFFile

from lk_census.final_report.FinalReportConstants import FinalReportConstants


class FinalReportTablePDFMixin:
    @property
    def original_pdf_file(self):
        return PDFFile(os.path.join(self.dir_data, "original.pdf"))

    @property
    def original_pdf_image_file(self):
        return PDFFile(os.path.join(self.dir_data, "original.png"))

    def build_original_pdf(self, force=False):
        if not self.original_pdf_file.exists() or force:
            FinalReportConstants.PDF_FILE.extract_subset(
                self.page_num + FinalReportConstants.PAGE_OFFSET,
                self.page_num + FinalReportConstants.PAGE_OFFSET,
                self.original_pdf_file,
            )

        if self.original_pdf_file.exists() and (
            not self.original_pdf_image_file.exists() or force
        ):
            self.original_pdf_file.to_image(self.original_pdf_image_file)
