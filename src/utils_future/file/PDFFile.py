import warnings

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

    def extract_table_data(
        self, i_table_on_page, total_tables_on_page, raw_table_index_list
    ):

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            tables = camelot.read_pdf(
                self.path,
                flavor="stream",
                row_tol=10,
            )

        if total_tables_on_page != 1:
            log.debug(f"{total_tables_on_page=}")
            log.debug(f"len(tables)={len(tables)}")

            if len(raw_table_index_list) > 0:
                actual_tables = []
                for raw_table_index in raw_table_index_list:
                    actual_tables.append(tables[raw_table_index])
                tables = actual_tables

            elif total_tables_on_page != len(tables):
                for i_table, table in enumerate(tables):
                    log.warning("-" * 40)
                    log.warning(f"Table {i_table}")
                    log.warning("-" * 40)
                    log.warning(f"{table.df.values.tolist()}")

                raise ValueError(
                    f"Expected {total_tables_on_page} tables on page,"
                    + f" but found {len(tables)}"
                )
            else:
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
