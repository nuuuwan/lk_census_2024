import os
import sys

from lk_census.final_report.table import FinalReportTable
from lk_census.readme.ReadMe import ReadMe

if __name__ == "__main__":
    table_num = sys.argv[1]
    table = FinalReportTable.from_table_num(table_num)

    os.system(f"code {table.original_pdf_file.path}")

    if not table.fields_file.exists:
        table.fields_file.write(
            dict(original_key="", other_keys=[], is_summable=False)
        )
        os.system(f"code {table.fields_file.path}")
    else:
        table.build()
        ReadMe().build()
        os.system(f"code {table.data_file.path}")
