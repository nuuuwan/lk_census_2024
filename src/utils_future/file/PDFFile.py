import camelot
import fitz
from pypdf import PdfReader, PdfWriter

from utils_future.console.Log import Log
from utils_future.file.File import File

log = Log("PDFFile")


class PDFFile(File):
    def extract_subset(
        self, start_page, end_page, output_pdf_file, drop_images=False
    ):
        reader = PdfReader(self.path)
        writer = PdfWriter()
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        if drop_images:
            writer.remove_images()

        for page in writer.pages:
            page.compress_content_streams()

        writer.compress_identical_objects()  # dedup shared resources

        with open(output_pdf_file.path, "wb") as fout:
            writer.write(fout)

        n_pages = end_page - start_page + 1
        log.debug(
            f"Extracted {n_pages} pages ({start_page} to {end_page})"
            f" from {self} to {output_pdf_file}"
        )
        return output_pdf_file

    def to_text_file(self, output_text_file):
        reader = PdfReader(self.path)
        with open(output_text_file.path, "w", encoding="utf-8") as fout:
            for page in reader.pages:
                text = page.extract_text() or ""
                fout.write(text)
                fout.write("\n")
        log.debug(f"Converted {self} to text file {output_text_file}")
        return output_text_file

    def extract_table_data(self, i_table_on_page, total_tables_on_page):
        tables = camelot.read_pdf(
            self.path,
            flavor="stream",
            row_tol=10,
        )

        if total_tables_on_page != len(tables):
            raise ValueError(
                f"Expected {total_tables_on_page} tables on page,"
                + f" but found {len(tables)}"
            )

        if total_tables_on_page != 1:
            tables = [tables[i_table_on_page]]

        d_list = []
        for table in tables:
            d_list.extend(table.df.values.tolist())
        return d_list

    def to_image(self, output_image_file):
        doc = fitz.open(self.path)
        page = doc[0]
        pix = page.get_pixmap(dpi=75)
        pix.save(output_image_file.path)
