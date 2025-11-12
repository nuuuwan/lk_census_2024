import os

from utils import File, Log

log = Log("DataTable")


class DataTableReadMeMixin:
    DIR_DATA = "data"
    README_PATH = os.path.join(DIR_DATA, "README.md")

    @classmethod
    def build_readme(cls):
        lines = ["# Data Tables", ""]
        for i_table, data_table in enumerate(cls.list_all(), start=1):
            line = (
                f"{i_table}. [{data_table.table_title}]"
                + f"({data_table.dir_table.replace('data/', '')})"
            )
            lines.append(line)
        readme_file = File(cls.README_PATH)
        readme_file.write_lines(lines)
        log.info(f" Wrote {readme_file}")
