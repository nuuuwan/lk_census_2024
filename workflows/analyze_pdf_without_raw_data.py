import os

from lk_census.final_report.table import FinalReportTable

if __name__ == "__main__":
    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 1:
            continue

        print("")
        print(table.table_num)
        print(
            table.build_status,
            FinalReportTable.STATUS_LABELS[table.build_status],
        )
        print("")

        os.system(f'code "{table.original_pdf_file.path}"')

        table.build_raw_data()

        break
