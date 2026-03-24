import json

from lk_census.pdf_data_table import PDFDataTable
from lk_census.xlsx_data_table import XLSXDataTable


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
        data_table_list = PDFDataTable.list_all()
        n_tables = len(data_table_list)
        lines = [
            f"## PDF Data Tables ({n_tables:,})",
            "",
            "The following datasets have been extracted from the PDF source documents:",
            "",
        ]
        for i_table, data_table in enumerate(data_table_list, start=1):
            lines.extend(self.get_lines_for_data_table(i_table, data_table))
        return lines

    def get_lines_for_xlsx_data_table(self, i_table, data_table) -> list[str]:
        lines = [
            f"### {i_table:02d}. [{data_table.table_title}]"
            + f"({data_table.dir_table.replace('data/', '')})",
            "",
        ]
        for label, file_path in [
            ("📄 JSON", data_table.json_path),
            ("📄 TSV Table", data_table.tsv_path),
            ("📊 Source XLSX", data_table.xlsx_path),
        ]:
            lines.append(f"- [{label}]({file_path})")
        lines.append("")
        lines.extend(self.get_lines_for_example_data(data_table))
        return lines

    def get_lines_for_xlsx_data_tables(self) -> list[str]:
        data_table_list = XLSXDataTable.list_all()
        n_tables = len(data_table_list)
        lines = [
            f"## XLSX Data Tables ({n_tables:,})",
            "",
            "The following datasets have been extracted from the XLSX source documents:",
            "",
        ]
        for i_table, data_table in enumerate(data_table_list, start=1):
            lines.extend(
                self.get_lines_for_xlsx_data_table(i_table, data_table)
            )
        return lines
