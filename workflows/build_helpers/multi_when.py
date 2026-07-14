import json

from lk_census.final_report.table import FinalReportTable
from lk_census.readme import ReadMe


def print_line():
    print("-" * 40)


def get_years_in_keys(values):
    keys = list(values.keys())
    years = set()
    for key in keys:
        for i in range(len(key) - 3):
            part = key[i : i + 4]
            if part.isdigit():
                years.add(int(part))
    return sorted(years)


if __name__ == "__main__":

    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 4:
            continue

        values = table.data_list[0]["values"]
        years = get_years_in_keys(values)
        if len(years) == 0:
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

        print(json.dumps(values, indent=4))
        print_line()

        print("⚠️ Years in keys:", years)
        print_line()

        table.build_lanka_data()

        break
