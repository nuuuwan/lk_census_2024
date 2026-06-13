import json

from gig_future import EntType
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

    def get_lines_for_provinces_table(self, data_table) -> list[str]:
        provinces_data = [
            d
            for d in data_table.data_list
            if d["region_ent_type"]
            in [EntType.COUNTRY.name, EntType.PROVINCE.name]
        ]
        provinces_data.sort(key=lambda d: d["region_id"])
        lines = ["### Data by Country & Province", ""]
        # render as markdown table columns are region_id, region_name, and all
        # the keys in values
        header = ["region_id", "region_name", "total_value"] + list(
            data_table.data_list[0]["values"].keys()
        )
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["--:"] * len(header)) + "|")
        for d in provinces_data:
            row = [d["region_id"], d["region_name"], f"{d['total_value']:,}"]
            row.extend(f"{v:,}" for v in d["values"].values())
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
        return lines

    def get_lines_for_data_files(self, data_table) -> list[str]:
        lines = []
        lines.extend(["### Data Files", ""])
        for emoji, file in [
            ("📄", data_table.all_data_file),
            ("📕", data_table.tsv_file),
            ("📊", data_table.xlsx_file),
        ]:
            lines.append(f"- [{emoji} {file}]({file.path})")
        lines.append("")
        return lines

    def get_lines_for_source(self, data_table) -> list[str]:
        lines = []
        lines.extend(["### Source", ""])
        lines.append(
            f"- 🌐: [{data_table.url_remote}]({data_table.url_remote})"
        )
        lines.append("")
        return lines

    def get_lines_for_data_table(self, i_table, data_table) -> list[str]:
        lines = [
            f"## {i_table:02d}. [{data_table.data_table_id}]"
            + f"({data_table.dir_table})",
            "",
        ]
        lines.extend(self.get_lines_for_provinces_table(data_table))
        lines.extend(self.get_lines_for_example_data(data_table))
        lines.extend(self.get_lines_for_data_files(data_table))
        lines.extend(self.get_lines_for_source(data_table))

        lines.append("")

        return lines

    def get_lines_for_xlsx_data_tables(self) -> list[str]:
        data_table_list = XLSXDataTable.list_all()
        len(data_table_list)
        lines = []
        for i_table, data_table in enumerate(data_table_list, start=1):
            lines.extend(self.get_lines_for_data_table(i_table, data_table))
        return lines
