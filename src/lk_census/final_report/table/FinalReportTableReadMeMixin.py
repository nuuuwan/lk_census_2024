import os

from utils import File


class FinalReportTableReadMeMixin:
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    def build_readme(self):
        pass
