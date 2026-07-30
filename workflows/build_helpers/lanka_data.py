from lk_census.final_report.table import FinalReportTable

if __name__ == "__main__":

    table_list = FinalReportTable.list()

    for table in table_list:

        if table.build_status == 3:
            if table.is_can_build_data:
                table.build_data()
                table.data_file.open("code")
                break

        if table.build_status == 4:
            if table.is_lanka_data_fields_complete:
                table.build_lanka_data()
                table.lanka_data_file.open("code")
                break

        if table.build_status == 5:
            print("-" * 32)
            print(table.table_num, table.table_name)
            print("-" * 32)

            if "house" not in table.table_name.lower():
                continue

            fields = table.fields
            entity_class_name = fields.get("entity_class_name", "")
            if entity_class_name == "House":
                continue

            table.fields_file.open("code")
            table.lanka_data_file.open("code")
            table.original_pdf_file.open("code")

            break
