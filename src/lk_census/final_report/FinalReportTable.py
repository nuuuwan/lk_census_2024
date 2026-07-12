import os
from dataclasses import dataclass

from lk_census.final_report.FinalReportConstants import FinalReportConstants
from utils_future import JSONFile, Log, PDFFile

log = Log("FinalReportTable")


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
        d_list = FinalReportConstants.TABLE_METADATA_FILE.read()
        return [cls.from_dict(d) for d in d_list]

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

    @property
    def raw_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "raw_data.json"))

    def build_raw_data(self):
        try:
            raw_data = self.original_pdf_file.extract_table_data()
            self.raw_data_file.write(raw_data)
            log.info(f"Wrote {self.raw_data_file}")
        except Exception as e:
            log.error(f"Failed to build raw data for {self}: {e}")

    def build(self):
        self.build_original_pdf()
        self.build_raw_data()
