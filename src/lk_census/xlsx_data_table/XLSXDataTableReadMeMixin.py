import os

from utils_future import File, Log

log = Log("XLSXDataTableReadMeMixin")


class XLSXDataTableReadMeMixin:
    @property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    def build_readme(self):
        lines = []
        self.readme_file.write_lines(lines)
        log.info(f"Wrote {self.readme_file}")
