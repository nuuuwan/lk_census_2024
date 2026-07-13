import os

from utils_future import JSONFile, Log

log = Log("FinalReportTableRawDataMixin")


class FinalReportTableRawDataMixin:
    @property
    def raw_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "raw_data.json"))

    def build_raw_data(self, force=False):
        if self.raw_data_file.exists and not force:
            return

        if self.has_page_multiple_tables:
            return
        try:
            raw_data = self.original_pdf_file.extract_table_data(
                self.i_table_on_page,
                self.total_tables_on_page,
            )
            self.raw_data_file.write(raw_data)
            log.info(f"Wrote {self.raw_data_file}")
        except Exception as e:
            log.error(f"Failed to build raw data for {self}: {e}")

    @property
    def raw_data_list(self):
        if not self.raw_data_file.exists:
            return None

        return self.raw_data_file.read()
