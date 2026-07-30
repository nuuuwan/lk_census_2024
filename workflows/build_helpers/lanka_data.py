from utils_future import Log

from lk_census.final_report.table import FinalReportTable

log = Log("build_helpers/lanka_data")

if __name__ == "__main__":

    table_list = FinalReportTable.list()

    for table in table_list:

        if table.build_status == 3:
            if table.is_can_build_data:
                log.error(f"{table} build_data...")
                table.build_data()
                table.data_file.open("code")
                break

        if table.build_status == 4:
            if table.is_lanka_data_fields_complete:
                if table.is_can_build_lanka_data:
                    log.error(f"{table} build_lanka_data...")
                    table.data_file.open("code")
                    table.build_lanka_data()
                    table.lanka_data_file.open("code")
                    break

        if table.build_status == 5:

            if table.is_lanka_data_verified:
                continue

            log.info("-" * 32)
            log.info(f"table.table_num={table.table_num}")
            log.info("-" * 32)

            fields = table.fields
            fields["is_lanka_data_verified"] = False
            table.fields_file.write(fields)

            table.fields_file.open("code")
            table.original_pdf_file.open("code")
            table.lanka_data_file.open("code")

            break
