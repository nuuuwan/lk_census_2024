import os
from dataclasses import dataclass

from utils_future import File, JSONFile, Log, PDFFile

log = Log("FinalReport")


@dataclass
class FinalReportTable:
    table_num: str
    table_name: str
    page_num: int

    @property
    def chapter_num(self):
        return int(self.table_num.split(".")[0])

    @property
    def table_id(self):
        return f"{self.table_num}-{self.table_name.replace(' ', '-')}"

    @property
    def dir_data(self):
        dir_data = os.path.join(
            "data",
            "final-report-tables",
            f"chapter-{self.chapter_num}",
            self.table_id,
        )
        os.makedirs(dir_data, exist_ok=True)
        return dir_data

    @classmethod
    def from_dict(cls, d):
        return cls(
            table_num=d["table_num"],
            table_name=d["table_name"],
            page_num=int(d["page_num"]),
        )

    @classmethod
    def list(cls):
        d_list = FinalReport.TABLE_METADATA_FILE.read()
        return [cls.from_dict(d) for d in d_list]

    @property
    def original_pdf_file(self):
        return PDFFile(os.path.join(self.dir_data, f"original.pdf"))

    def build_original_pdf(self):
        FinalReport.PDF_FILE.extract_subset(
            self.page_num + FinalReport.PAGE_OFFSET,
            self.page_num + FinalReport.PAGE_OFFSET,
            self.original_pdf_file,
        )

    def build(self):
        self.build_original_pdf()


class FinalReport:
    PDF_FILE = PDFFile(os.path.join("original_docs", "CPH2024_Final_Eng.pdf"))

    TABLE_INDEX_START_PAGE, TABLE_INDEX_END_PAGE = 11, 13
    TABLE_INDEX_PDF_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.pdf")
    )
    TABLE_INDEX_TXT_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.txt")
    )
    MIN_VALID_TABLE_PAGE_NUM, MAX_VALID_TABLE_PAGE_NUM = 6, 205

    PAGE_OFFSET = 17

    @staticmethod
    def extract_table_index():
        FinalReport.PDF_FILE.extract_subset(
            FinalReport.TABLE_INDEX_START_PAGE,
            FinalReport.TABLE_INDEX_END_PAGE,
            FinalReport.TABLE_INDEX_PDF_FILE,
        )
        FinalReport.TABLE_INDEX_PDF_FILE.to_text_file(
            FinalReport.TABLE_INDEX_TXT_FILE
        )

    TABLE_METADATA_FILE = JSONFile(
        os.path.join("derived_docs", "final-report-index.metadata.json")
    )

    @staticmethod
    def build_table_metadata():

        def clean(text):
            text = text.replace(".", "")
            return text.strip()

        def parse_int(text):
            try:
                return int(text)
            except ValueError:
                return None

        d_list = []
        lines = FinalReport.TABLE_INDEX_TXT_FILE.read_lines()
        for i_line, line in enumerate(lines, start=0):
            if not line.startswith("Table"):
                continue
            words = line.strip().split(" ")
            page_num = parse_int(words[-1])

            if page_num is None or not (
                FinalReport.MIN_VALID_TABLE_PAGE_NUM
                <= page_num
                <= FinalReport.MAX_VALID_TABLE_PAGE_NUM
            ):
                new_line = line.strip() + lines[i_line + 1].strip()
                words = new_line.strip().split(" ")

                page_num = parse_int(words[-1])
                assert (
                    page_num is not None
                ), f"Failed to parse page number from line: {new_line}"
                assert (
                    FinalReport.MIN_VALID_TABLE_PAGE_NUM
                    <= page_num
                    <= FinalReport.MAX_VALID_TABLE_PAGE_NUM
                ), f"Page number {page_num} out of valid range in line: {new_line}"

            table_num = words[1]
            table_name = clean(" ".join(words[3:-2]))
            d = dict(
                table_num=table_num, table_name=table_name, page_num=page_num
            )
            d_list.append(d)
        FinalReport.TABLE_METADATA_FILE.write(d_list)
        log.info(
            f"Wrote {len(d_list)} tables to {FinalReport.TABLE_METADATA_FILE}"
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
