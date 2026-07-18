import json

from lk_census.final_report.table import FinalReportTable
from lk_census.readme import ReadMe


def print_line():
    print("-" * 40)


if __name__ == "__main__":

    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 4:
            continue

        if table.lanka_data_pass:
            continue

        print_line()

        print(table.table_num)
        print(table.table_name)
        print(
            table.build_status,
            FinalReportTable.STATUS_LABELS[table.build_status],
        )
        print_line()

        print(json.dumps(table.fields, indent=4))
        print_line()

        print(json.dumps(table.data_list[0], indent=4))
        print_line()

        if table.is_lanka_data_fields_complete:
            table.build_lanka_data()
            if table.lanka_data_file.exists():
                table.lanka_data_file.open("code")
        else:
            fields = table.fields
            fields["entity_class_name"] = (
                fields.get("entity_class_name") or "Person"
            )
            fields["time_value"] = fields.get("time_value") or "2024"
            fields["row_dim_class_name"] = (
                fields.get("row_dim_class_name") or "District"
            )
            fields["row_dim_key"] = fields.get("row_dim_key") or "region_id"
            fields["col_dim_class_name"] = (
                fields.get("col_dim_class_name") or None
            )
            fields["cell_label"] = fields.get("cell_label") or "Count"
            fields["cell_class_name"] = fields.get("cell_class_name") or "Int"
            table.fields_file.write(fields)

            table.fields_file.open("code")

        ReadMe().build()
        break
