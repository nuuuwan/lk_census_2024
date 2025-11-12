import os
import re

import camelot
import pandas as pd
from pypdf import PdfReader, PdfWriter
from utils import JSONFile, Log, PDFFile

from lk_census.OriginalDoc import OriginalDoc

log = Log("DataTable")


class DataTablePDFMixin:
    @property
    def pdf_path(self):
        return os.path.join(
            OriginalDoc.DIR_ORIGINAL_DOCS,
            self.doc_name + ".pdf",
        )

    @property
    def subset_pdf_path(self):
        return os.path.join(
            self.dir_table,
            "table.pdf",
        )

    def save_subset_pdf(self):
        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        for page_num in range(self.page_start - 1, self.page_end):
            if page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])

        with open(self.subset_pdf_path, "wb") as output_file:
            writer.write(output_file)

        log.debug(
            f"Wrote pages {self.page_start}-{self.page_end} "
            + f"to {PDFFile(self.subset_pdf_path)}"
        )
        return self.subset_pdf_path

    @staticmethod
    def __parse_int__(x: str) -> int | str:
        try:
            return int(x)
        except ValueError:
            return x

    @staticmethod
    def __flatten__(table_data):
        arr_of_arr = []
        for row_data in table_data:
            arr = []
            for cell_original in row_data.values():
                cell = str(cell_original)
                if cell in ["", "nan"]:
                    continue
                cell = cell.replace("‐", "-")
                cell = cell.replace("- - ", "")
                cell = cell.replace("- - ", "")
                cell = re.sub(r"[^A-Za-z0-9\s\-]", "", cell)
                cell = re.sub(r"\s+", " ", cell).strip()
                cell = DataTablePDFMixin.__parse_int__(cell)

                arr.append(cell)
            arr_of_arr.append(arr)
        return arr_of_arr

    def extract_raw_table(self):
        tables = camelot.read_pdf(
            self.subset_pdf_path,
            pages="all",
            flavor="stream",
            strip_text="\n",
            row_tol=20,
            edge_tol=300,
        )
        df = pd.concat([t.df for t in tables], ignore_index=True)
        table_data = df.to_dict(orient="records")
        arr_of_arr = self.__flatten__(table_data)

        json_file = JSONFile(os.path.join(self.dir_table, "raw-table.json"))
        json_file.write(arr_of_arr)
        log.debug(f"Wrote {len(arr_of_arr)} raw rows to {json_file}")
        assert len(arr_of_arr) > 0, "No raw table extracted"
        return arr_of_arr
