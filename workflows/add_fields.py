import os

from lk_census.final_report.table import FinalReportTable

if __name__ == "__main__":
    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 3:
            continue

        print(FinalReportTable.COMPLICATED_TABLE_NUM_LIST)
        print("9.1" in FinalReportTable.COMPLICATED_TABLE_NUM_LIST)
        print(
            table.table_num,
            table.table_num in FinalReportTable.COMPLICATED_TABLE_NUM_LIST,
        )

        print("")
        print(table.table_num)
        print(
            table.build_status,
            FinalReportTable.STATUS_LABELS[table.build_status],
        )
        print("Is Complicated" if table.is_complicated else "")
        print("")

        if not table.has_complete_fields:
            table.fields_file.write(
                dict(primary_key="", other_keys=[], is_summable=False)
            )
            os.system(f"code {table.fields_file.path}")
            os.system(f"code {table.original_pdf_file.path}")

        else:
            table.build_data(force=True)
            os.system(f"code {table.data_file.path}")

        break
