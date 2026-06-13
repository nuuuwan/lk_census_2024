import os
from dataclasses import dataclass

from lk_census.xlsx_data_table.XLSXDataTableExtractDataMixin import \
    XLSXDataTableExtractDataMixin
from lk_census.xlsx_data_table.XLSXDataTableLoaderMixin import \
    XLSXDataTableLoaderMixin
from utils_future import WWW, File, Log

log = Log("XLSXDataTable")


@dataclass
class XLSXDataTable(
    XLSXDataTableLoaderMixin,
    XLSXDataTableExtractDataMixin,
):
    data_table_id: str
    remote_file_name: str
    column_offset: int
    field_list: list[str]
    has_province_info: bool

    DIR_DATA = "data"
    DIR_ORIGINAL_DOCS = "original_docs"
    MIN_ORIGINAL_DOC_SIZE_KB = 500

    @property
    def n_fields(self) -> int:
        return len(self.field_list)

    @property
    def dir_table(self):
        return os.path.join(
            self.DIR_DATA,
            self.data_table_id,
        )

    @property
    def url_remote(self):
        return (
            "https://www.statistics.gov.lk"
            + "/Population/StaticalInformation/CPH2024"
            + f"/{self.remote_file_name}"
        )

    @property
    def xlsx_path(self):
        original_doc_id = self.remote_file_name.replace("/", "-")
        return os.path.join(self.DIR_ORIGINAL_DOCS, f"{original_doc_id}.xlsx")

    def download_original_doc(self):
        local_path = self.xlsx_path
        if os.path.exists(local_path):
            log.debug(f"{File(local_path)} exists")
            return
        os.makedirs(self.DIR_ORIGINAL_DOCS, exist_ok=True)
        log.debug(f"Downloading {self.url_remote}...")
        WWW(self.url_remote).download_binary(local_path)
        local_file = File(local_path)
        if local_file.size < self.MIN_ORIGINAL_DOC_SIZE_KB:
            os.remove(local_path)
            raise ValueError(f"Downloaded file {local_file} is too small.")

        log.info(f"Wrote {local_file}")

    def build(self):
        self.download_original_doc()
        self.extract_data()

    @classmethod
    def build_all(cls):
        n = len(cls.list_all())
        data_tables = cls.list_all()
        for i_data_table, data_table in enumerate(data_tables, start=1):
            log.debug("-" * 20)
            log.info(f"{i_data_table + 1}/{n}: {data_table.data_table_id}")
            log.debug("-" * 20)
            data_table.build()
