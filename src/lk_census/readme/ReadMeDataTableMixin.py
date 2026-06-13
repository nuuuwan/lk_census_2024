import json

from lk_census.xlsx_data_table import XLSXDataTable


class ReadMeDataTableMixin:

    def get_lines_for_example_data(self, data_table) -> list[str]:
        lines = []
        data_list = data_table.data_list
        first_data = data_list[0]
        lines.extend(
            [
                "### Example Data Row (JSON)",
                "",
                "```json",
                json.dumps(first_data, indent=4),
                "```",
                "",
            ]
        )

        return lines

    def get_lines_for_xlsx_data_table(self, i_table, data_table) -> list[str]:
        lines = [
            f"## {i_table:02d}. [{data_table.data_table_id}]"
            + f"({data_table.dir_table})",
            "",
        ]
        lines.extend(self.get_lines_for_example_data(data_table))

        lines.extend(["### Data Files", ""])
        for emoji, file in [
            ("📄", data_table.all_data_file),
            ("📕", data_table.tsv_file),
            ("📊", data_table.xlsx_file),
        ]:
            lines.append(f"- [{emoji} {file}]({file.path})")
        lines.append("")

        lines.extend(["### Source", ""])
        lines.append(
            f"- 🌐: [{data_table.url_remote}]({data_table.url_remote})"
        )
        lines.append("")

        return lines

    def get_lines_for_xlsx_data_tables(self) -> list[str]:
        data_table_list = XLSXDataTable.list_all()
        len(data_table_list)
        lines = []
        for i_table, data_table in enumerate(data_table_list, start=1):
            lines.extend(
                self.get_lines_for_xlsx_data_table(i_table, data_table)
            )
        return lines
