import os

from lk_census.final_report.table import FinalReportTable

if __name__ == "__main__":
    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 3:
            continue

        print("")
        print(table.table_num)
        print("")

        if not table.has_complete_fields:
            table.fields_file.write(
                dict(original_key="", other_keys=[], is_summable=False)
            )
            os.system(f"code {table.fields_file.path}")
            os.system(f"code {table.original_pdf_file.path}")

        else:
            table.build()
            os.system(f"code {table.data_file.path}")

        break
