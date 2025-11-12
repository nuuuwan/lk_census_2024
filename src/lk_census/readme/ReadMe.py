import os

from utils import File, Format, Log, Time, TimeFormat

from lk_census.data_table import DataTable
from lk_census.original_doc import OriginalDoc

log = Log("ReadMe")


class ReadMe:
    PATH = "README.md"

    def get_lines_for_header(self) -> list[str]:
        time_updated_for_badge = Format.badge(
            TimeFormat.TIME.format(Time.now())
        )
        return [
            "# 🇱🇰 Sri Lanka - " + "Census of Population and Housing 2024",
            "",
            "![CPH]" + "(https://img.shields.io/badge/CPH-2024-blue)",
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
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
        lines = [
            "## Data Tables",
            "",
            "The source documents have been parsed to extract the following datasets: ",
            "",
        ]
        for i_table, data_table in enumerate(DataTable.list_all(), start=1):
            line = (
                f"{i_table}. [{data_table.table_title}]"
                + f"({data_table.dir_table.replace('data/', '')})"
            )
            lines.append(line)
        lines.append("")
        return lines

    def get_lines_for_footer(self) -> list[str]:
        return [
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith]"
            + "(https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
            "",
        ]

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
