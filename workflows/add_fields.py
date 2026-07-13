import os

from lk_census.final_report.table import FinalReportTable

if __name__ == "__main__":
    table_list = FinalReportTable.list()

    for table in table_list:
        if table.build_status != 2:
            continue

        os.system(f"code {table.original_pdf_file.path}")

        if not table.fields_file.exists:
            table.fields_file.write(
                dict(original_key="", other_keys=[], is_summable=False)
            )
            os.system(f"code {table.fields_file.path}")
