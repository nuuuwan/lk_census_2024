import json

from gig_future import EntType


class ReadMeDataTableMixin:

    def get_lines_for_data_table(self, data_table) -> list[str]:
        return [
            f"- [{data_table.data_table_id}]" + f"({data_table.dir_data})",
        ]

    def get_lines_for_xlsx_data_tables(self, data_table_list) -> list[str]:
        n = len(data_table_list)
        lines = [
            f"## Datasets from Excel Files (**{n:,}**)",
            "",
            "*Large tables at GND level detail, on a small set of topics.*",
            "",
        ]

        for data_table in data_table_list:
            lines.extend(self.get_lines_for_data_table(data_table))
        lines.append("")
        return lines
