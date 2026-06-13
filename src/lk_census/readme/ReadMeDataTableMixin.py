import json
import os

from lk_census.xlsx_data_table import XLSXDataTable


class ReadMeDataTableMixin:

    _VALIDATION_DESCRIPTIONS = {
        "parent_child_totals": "aggregated values don't match sum of children",
        "all_gig_gnds_present": "GNDs in the reference gazetteer missing from this dataset (boundary differences)",
        "gnds_are_valid": "GND IDs in this dataset not found in the reference gazetteer (boundary differences)",
        "total_field": "'total' field doesn't equal sum of other fields",
    }

    def get_lines_for_validations(self, data_table) -> list[str]:
        validations_path = os.path.join(
            data_table.dir_table, "validations.json"
        )
        if not os.path.exists(validations_path):
            return []
        with open(validations_path) as f:
            results = json.load(f)
        failures = [r for r in results if r["status"] == "fail"]
        if not failures:
            return []
        lines = ["#### Validation Errors", ""]
        for r in failures:
            desc = self._VALIDATION_DESCRIPTIONS.get(r["name"], r["name"])
            lines.append(f"⚠️ **{r['error_count']:,}** {desc}")
            examples = r.get("errors", [])[:3]
            for ex in examples:
                name = (
                    ex.get("region_name")
                    or ex.get("region_name_in_data")
                    or ex.get("region_id")
                )
                label = f"{name} (`{ex['region_id']}`)"
                if "total" in ex and "total_from_fields" in ex:
                    label += (
                        f" — total: {ex['total']:,},"
                        f" sum of fields: {ex['total_from_fields']:,}"
                    )
                lines.append(f"  - {label}")
            lines.append("")
        return lines

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
            + f"({data_table.dir_table})",
            "",
        ]

        for label, file_path in [
            ("📄 JSON", data_table.json_path),
            ("📄 TSV Table", data_table.tsv_path),
        ]:
            lines.append(f"- [{label}]({file_path})")
        lines.append("")

        lines.extend(self.get_lines_for_example_data(data_table))
        lines.extend(self.get_lines_for_validations(data_table))

        return lines

    def get_lines_for_xlsx_data_table(self, i_table, data_table) -> list[str]:
        lines = [
            f"### {i_table:02d}. [{data_table.table_title}]"
            + f"({data_table.dir_table})",
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
        lines.extend(self.get_lines_for_validations(data_table))
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
