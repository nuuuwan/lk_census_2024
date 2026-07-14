import json

from gig_future import EntType


class ReadMeDataTableMixin:

    def get_lines_for_data_table(self, data_table) -> list[str]:
        return [
            f"- [{data_table.data_table_id}]" + f"({data_table.dir_data})",
        ]

    def get_lines_for_xlsx_data_tables(self, data_table_list) -> list[str]:
        lines = ["## Datasets from Excel Files", ""]
        for data_table in data_table_list:
            lines.extend(self.get_lines_for_data_table(data_table))
        return lines
