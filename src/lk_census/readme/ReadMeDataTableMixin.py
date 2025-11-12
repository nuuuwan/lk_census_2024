import json

from lk_census.data_table import DataTable


class ReadMeDataTableMixin:

    def get_lines_for_example_data(self, data_table) -> list[str]:
        lines = []
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
            tokens.append(f"{region_ent_type.title()} ({n:,})")
        n = len(data_list)
        lines.extend(
            [
                f"**{n:,}** rows in total, by " + ", ".join(tokens),
                "",
            ]
        )
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

        lines.extend(self.get_lines_for_example_data(data_table))

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
