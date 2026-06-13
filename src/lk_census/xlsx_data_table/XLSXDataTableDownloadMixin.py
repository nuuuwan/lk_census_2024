import os

from utils_future import WWW, File, Log

log = Log("XLSXDataTableDownloadMixin")


class XLSXDataTableDownloadMixin:
    DIR_DATA = "data"
    DIR_ORIGINAL_DOCS = "original_docs"
    MIN_ORIGINAL_DOC_SIZE_KB = 500

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
