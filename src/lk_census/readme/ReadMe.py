import json
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

    def get_lines_for_data_table(self, i_table, data_table) -> list[str]:
        lines = [
            f"### {i_table:02d}. [{data_table.table_title}]"
            + f"({data_table.dir_table.replace('data/', '')})",
            "",
        ]

        for label, file_path in [
            ("📄 JSON", data_table.json_path),
            ("📄 TSV Table", data_table.tsv_path),
            ("📜 PDF-Table Only", data_table.subset_pdf_path),
            ("📜 Original Source PDF", data_table.original_doc.pdf_path),
        ]:
            lines.append(f"- [{label}]({file_path})")
        lines.append("")

        data_list = data_table.data_list
        first_data = data_list[0]
        lines.extend(
            [
                "#### Example Data",
                "",
                "```json",
                json.dumps(first_data, indent=4),
                "```",
                "",
            ]
        )

        region_ent_type_to_n = {}
        for d in data_list:
            region_ent_type = d["region_ent_type"]
            region_ent_type_to_n[region_ent_type] = (
                region_ent_type_to_n.get(region_ent_type, 0) + 1
            )
        tokens = []
        for region_ent_type, n in region_ent_type_to_n.items():
            tokens.append(f"{region_ent_type.title()} ({n})")
        n = len(data_list)
        lines.extend(
            [
                f"{n} rows in total, by " + ", ".join(tokens),
                "",
            ]
        )

        return lines

    def get_lines_for_data_tables(self) -> list[str]:
        lines = [
            "## Data Tables",
            "",
            "The source documents have been parsed"
            + " to extract the following datasets: ",
            "",
        ]
        for i_table, data_table in enumerate(DataTable.list_all(), start=1):
            lines.extend(self.get_lines_for_data_table(i_table, data_table))
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
