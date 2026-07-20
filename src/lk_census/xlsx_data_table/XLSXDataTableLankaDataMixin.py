import os

from utils_future import JSONFile


class XLSXDataTableLankaDataMixin:
    @property
    def lanka_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "lanka_data.json"))

    def build_lanka_data(self, force=False):
        if self.lanka_data_file.exists() and not force:
            return

        return
