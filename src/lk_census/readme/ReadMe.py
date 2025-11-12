import os

from utils import File, Log

from lk_census.data_table import DataTable
from lk_census.original_doc import OriginalDoc

log = Log("ReadMe")


class ReadMe:
    PATH = "README.md"

    def get_lines_for_header(self) -> list[str]:
        return [
            "# 🇱🇰 Sri Lanka - "
            + "Census of Population and Housing 2024 (CPH-2024)",
            "",
        ]

    def get_lines_for_original_docs(self) -> list[str]:
        lines = [
            "## Original Source Documents",
            "",
            "The following original documents have been downloaded from"
            + f" [{OriginalDoc.URL_BASE}]({OriginalDoc.URL_BASE})",
            "",
        ]
        for i_doc, original_doc in enumerate(OriginalDoc.list_all(), start=1):
            lines.append(
                f"{i_doc}. [{original_doc.title}]"
                + f"({os.path.basename(original_doc.pdf_path)})"
            )
        lines.append("")
        return lines

    def get_lines_for_data_tables(self) -> list[str]:
        lines = ["## Data Tables", ""]
        for i_table, data_table in enumerate(DataTable.list_all(), start=1):
            line = (
                f"{i_table}. [{data_table.table_title}]"
                + f"({data_table.dir_table.replace('data/', '')})"
            )
            lines.append(line)
        lines.append("")
        return lines

    def get_lines_for_footer(self) -> list[str]:
        return []

    def get_lines(self) -> list[str]:
        return (
            self.get_lines_for_header()
            + self.get_lines_for_original_docs()
            + self.get_lines_for_data_tables()
            + self.get_lines_for_footer()
        )

    def build(self):
        readme_file = File(self.PATH)
        readme_file.write_lines(self.get_lines())
        log.info(f"Wrote {readme_file}")
