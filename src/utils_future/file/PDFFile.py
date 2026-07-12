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

    def extract_table_data(self):
        tables = camelot.read_pdf(
            self.path,
            flavor="stream",
        )

        if len(tables) != 1:
            raise ValueError(
                f"[{self}] Expected exactly one table. Found {len(tables)}"
            )

        first_table = tables[0]
        data = first_table.df.values.tolist()
        n_rows, n_cols = first_table.shape

        if n_rows < 2 or n_cols < 2:
            raise ValueError(
                f"[{self}] Expected at least 2x2 table."
                + f" Found {n_rows}x{n_cols} table"
            )
        return data

    def to_image(self, output_image_file):
        doc = fitz.open(self.path)
        page = doc[0]
        pix = page.get_pixmap(dpi=75)
        pix.save(output_image_file.path)
