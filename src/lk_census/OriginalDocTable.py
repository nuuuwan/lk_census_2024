import os
import re
from dataclasses import dataclass

import camelot
from pypdf import PdfReader, PdfWriter
from utils import JSONFile, Log, PDFFile

log = Log("OriginalDocTable")


@dataclass
class OriginalDocTable:
    doc_name: str
    table_title: str
    pages: tuple[int, int]

    DIR_DATA = "data"

    @property
    def pdf_file(self):
        return PDFFile(
            os.path.join(
                "original_docs",
                f"{self.doc_name}.pdf",
            )
        )

    @property
    def page_start(self):
        return self.pages[0]

    @property
    def page_end(self):
        return self.pages[1]

    @property
    def pdf_path(self):
        return os.path.join(
            "original_docs",
            f"{self.doc_name}.pdf",
        )

    @property
    def name_safe(self):
        name_safe = re.sub(r"\s+", " ", self.table_title)
        name_safe = name_safe.replace(" ", "-")
        name_safe = "".join(
            char for char in name_safe if char.isalnum() or char == "-"
        )
        return name_safe

    @property
    def dir_table(self):
        return os.path.join(
            self.DIR_DATA,
            self.doc_name,
            self.name_safe,
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

        os.makedirs(self.dir_table, exist_ok=True)
        with open(self.subset_pdf_path, "wb") as output_file:
            writer.write(output_file)

        log.debug(
            f"Wrote {self.page_start}-{self.page_end} "
            + f"to {PDFFile(self.subset_pdf_path)}"
        )
        return self.subset_pdf_path

    def extract_tables(self):
        pages = f"{self.page_start}-{self.page_end}"
        for flavor in ["lattice", "stream"]:
            tables = camelot.read_pdf(
                self.pdf_path,
                pages=pages,
                flavor=flavor,
                strip_text="\n",
            )
            for i_table, table in enumerate(tables, start=1):
                table_id = f"{flavor}-{i_table}"
                os.makedirs(self.dir_table, exist_ok=True)

                plot_path = os.path.join(
                    self.dir_table, f"{table_id}.camelot.plot.png"
                )
                camelot.plot(table, kind="contour").savefig(
                    plot_path, dpi=300
                )
                log.debug(f"Saved plot to {plot_path}")

                # Save table as JSON
                table_data = table.df.to_dict(orient="records")

                json_file = JSONFile(
                    os.path.join(self.dir_table, f"{table_id}.subtable.json")
                )
                json_file.write(table_data)
                log.debug(f"Wrote {len(table_data)} rows to {json_file}")

    def get_fields(self):
        lattice_subtable_1 = JSONFile(
            os.path.join(self.dir_table, "lattice-1.subtable.json")
        )
        field_groups = {}
        subtable = lattice_subtable_1.read()
        log.debug(f"{subtable=}")
        for cells in subtable:
            cur_cell = None
            for i_cell, cell in enumerate(cells.values()):
                cell = cell.replace("‐", "-")
                cell_en_only = re.sub(r"[^A-Za-z0-9\s\-]", "", cell)
                cell_en_only = re.sub(r"\s+", " ", cell_en_only).strip()
                if i_cell not in field_groups:
                    field_groups[i_cell] = []

                if cell_en_only:
                    cur_cell = cell_en_only
                elif cur_cell:
                    cell_en_only = cur_cell

                field_groups[i_cell].append(cell_en_only)
        fields = []
        for field_group in field_groups.values():
            field = "-".join([item for item in field_group if item.strip()])
            for replace_text in [
                "15 15 ",
                "15-59 15-59 ",
                "60-64 60-64 ",
                "65 65 ",
            ]:
                field = field.replace(replace_text, "")
            fields.append(field)
        log.info(f"{fields=}")
        return fields

    def extract_data(self):
        fields = self.get_fields()
        return fields

    @classmethod
    def list_all(cls) -> list["OriginalDocTable"]:
        return [
            # OriginalDocTable(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A4. Migrant population"
            #     + " by reason for migrating according to districts",
            #     (110, 111),
            # ),
            OriginalDocTable(
                "Basic-Population-Information"
                + "-by-Districts-and-Divisional-Secretary-Divisions",
                "A5. Population by sex, age and district according to DSD",
                (112, 136),
            ),
            OriginalDocTable(
                "Basic-Population-Information"
                + "-by-Districts-and-Divisional-Secretary-Divisions",
                "A6. Population by ethnicity and district according to DSD",
                (137, 161),
            ),
            OriginalDocTable(
                "Basic-Population-Information"
                + "-by-Districts-and-Divisional-Secretary-Divisions",
                "A7. Population by religion and district according to DSD",
                (162, 185),
            ),
        ]

    @classmethod
    def extract_all(cls):
        for original_doc_table in cls.list_all():
            # original_doc_table.save_subset_pdf()
            # original_doc_table.extract_tables()
            original_doc_table.extract_data()
