from pypdf import PdfReader, PdfWriter

from utils_future.console.Log import Log
from utils_future.file.File import File

log = Log("PDFFile")


class PDFFile(File):
    def extract_subset(self, start_page, end_page, output_file_path):
        reader = PdfReader(self.path)
        writer = PdfWriter()
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])
        with open(output_file_path, "wb") as fout:
            writer.write(fout)
        output_pdf_file = PDFFile(output_file_path)
        log.info(
            f"Extracted pages {start_page}-{end_page} from {self}"
            + f" into {output_pdf_file}"
        )
        return output_pdf_file
