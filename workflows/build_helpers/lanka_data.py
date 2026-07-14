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

        if "7.10" != table.table_num:
            continue

        if not table.is_lanka_data_parser_implemented:
            continue

        print_line()

        print(table.table_num)
        print(table.table_name)
        print(
            table.build_status,
            FinalReportTable.STATUS_LABELS[table.build_status],
        )
        print_line()

        print(json.dumps(table.data_list[0], indent=4))
        print_line()

        if not table.is_lanka_data_metadata_complete:
            lanka_data_metadata = {}
            if table.lanka_data_metadata_file.exists:
                lanka_data_metadata = table.lanka_data_metadata_file.read()
            if "what_label" not in lanka_data_metadata:
                lanka_data_metadata |= {
                    "what_label": table.table_name,
                }
            table.lanka_data_metadata_file.write(lanka_data_metadata)
            table.lanka_data_metadata_file.open("code")
            break

        else:
            lanka_data = table.build_lanka_data()
            print(json.dumps(lanka_data, indent=4))
            print_line()
            if lanka_data is not None:
                table.lanka_data_file.open("code")

        ReadMe().build()
        break
