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

        table.original_pdf_file.open("code")

        fields = {}
        if table.fields_file.exists:
            fields = table.fields_file.read()
        if "raw_table_index_list" not in fields:
            fields["raw_table_index_list"] = []
        table.fields_file.write(fields)
        table.fields_file.open("code")

        if table.raw_data_file.exists:
            if "raw_table_index_list" in table.raw_data_file.read():
                table.raw_data_file.delete()

        table.build_raw_data(force=True)

        break
