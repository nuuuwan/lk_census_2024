import json
import os

from utils_future import (File, Format, JSONFile, Log, Markdown, Time,
                          TimeFormat)

log = Log("CommonTableReadMeMixin")


class CommonTableReadMeMixin:
    @property
    def readme_file(self):
        return File(os.path.join(self.dir_data, "README.md"))

    def get_lines_for_header(self) -> list[str]:
        time_updated_for_badge = Format.badge(
            TimeFormat.DATE.format(Time.now())
        )

        return [
            f"# {self.table_name}",
            "",
            "![CPH]" + "(https://img.shields.io/badge/CPH-2024-blue)",
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
            "",
            f"*{self.source_description}*",
            "",
        ]

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

    URL_LANKA_DATA = "https://github.com/nuuuwan/lanka_data"

    @staticmethod
    def _format_json_lines(data):
        lines = json.dumps(data, indent=4).splitlines()
        n_lines = len(lines)
        MAX_JSON_LINES = 30

        if n_lines > MAX_JSON_LINES:
            lines = lines[:MAX_JSON_LINES] + ["..."]

        return ["```json", *lines, "```"]

    def get_lines_for_lanka_data(self):
        if not self.lanka_data_file.exists():
            return []

        lines = [
            "## Structured Data formatted for"
            + f" [Lanka Data API]({self.URL_LANKA_DATA})",
            "",
            *self._format_json_lines(self.lanka_data),
            "",
            f"- Source File: [{self.lanka_data_file.short_str}]"
            + f"({self.base_dir}{self.lanka_data_file.path})",
            "",
        ]
        return lines

    def get_lines_for_data(self):
        if not self.data_file.exists():
            return []

        lines = [
            "## Structured Data (similar to original layout)",
            "",
            *self._format_json_lines(self.data_list),
            "",
            f"- Source File: [{self.data_file.short_str}]"
            + f"({self.base_dir}{self.data_file.path})",
            "",
        ]
        return lines

    def get_lines_for_tsv(self):
        if not self.tsv_file.exists():
            return []

        N_ROWS = 20
        d_list = self.tsv_file.read()
        suffix = ""
        if len(d_list) > N_ROWS:
            d_list = d_list[:N_ROWS]
            suffix = f" - First {N_ROWS} rows"

        lines = [
            "## Structured TSV Data (similar to original layout)" + suffix,
            "",
            *Markdown.table(d_list),
            f"- Source File: [{self.tsv_file.short_str}]"
            + f"({self.base_dir}{self.tsv_file.path})",
            "",
        ]
        return lines

    def get_lines_for_raw_data(self):
        if not self.raw_data_file.exists():
            return []

        lines = [
            "## Raw Data (directly scraped from PDF)",
            "",
            *self._format_json_lines(self.raw_data_list),
            f"- Source File: [{self.raw_data_file.short_str}]"
            + f"({self.base_dir}{self.raw_data_file.path})",
            "",
        ]
        return lines

    def get_lines_for_original_pdf(self):
        if not self.original_pdf_image_file.exists():
            return []

        lines = [
            "## Original PDF Page",
            "",
            "![Download the original PDF]"
            + f"({self.base_dir}{self.original_pdf_image_file.path})",
            "",
            f"- Source File: [{self.original_pdf_file.short_str}]"
            + f"({self.base_dir}{self.original_pdf_file.path})",
            "",
        ]

        if self.has_page_multiple_tables:
            lines.extend(
                [
                    f"(Table {self.i_table_on_page} on this page.)",
                    "",
                ]
            )
        return lines

    def get_lines_for_source(self):

        lines = [
            "## Source",
            "",
            f"- <{self.source_url}>",
            "",
        ]
        return lines

    def get_lines(self):
        return (
            self.get_lines_for_header()
            + self.get_lines_for_lanka_data()
            + self.get_lines_for_data()
            + self.get_lines_for_tsv()
            + self.get_lines_for_raw_data()
            + self.get_lines_for_original_pdf()
            + self.get_lines_for_source()
            + self.get_lines_for_footer()
        )

    def build_readme(self, force=True):
        if not force and self.readme_file.exists():
            return self.readme_file.read()

        lines = self.get_lines()
        self.readme_file.write("\n".join(lines))
        log.info(f"Wrote {self.readme_file}")
        return self.readme_file.read()

    # DUMMY functions

    @property
    def tsv_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.tsv"))

    @property
    def raw_data_file(self):
        return JSONFile(os.path.join(self.dir_data, "raw_data.json"))

    @property
    def original_pdf_image_file(self):
        return JSONFile(os.path.join(self.dir_data, "original.png"))

    @property
    def base_dir(self):
        return "../../../../"
