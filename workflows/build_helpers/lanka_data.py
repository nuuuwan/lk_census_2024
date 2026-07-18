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
            if table.lanka_data_metadata_file.exists():
                lanka_data_metadata = table.lanka_data_metadata_file.read()
            table.lanka_data_metadata_file.write(lanka_data_metadata)

        table.lanka_data_metadata_file.open("code")

        if table.is_lanka_data_metadata_complete:
            table.build_lanka_data(force=True)
            table.lanka_data_file.open("code")

        ReadMe().build()
        break
