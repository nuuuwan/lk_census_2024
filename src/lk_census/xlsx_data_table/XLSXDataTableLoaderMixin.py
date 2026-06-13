import os

from utils_future import JSONFile


class XLSXDataTableLoaderMixin:
    XLSX_TABLE_METADATA_PATH = os.path.join("metadata", "xlsx_tables.json")

    @classmethod
    def list_all(cls):
        table_list = []
        configs = JSONFile(cls.XLSX_TABLE_METADATA_PATH).read()
        for t in configs:
            table_list.append(
                cls(
                    data_table_id=t["data_table_id"],
                    remote_file_name=t["remote_file_name"],
                    total_col_index=t["total_col_index"],
                    fields_col_start_index=t["fields_col_start_index"],
                    field_list=t["field_list"],
                    has_province_info=t.get("has_province_info", True),
                    expected_total_value=t["expected_total_value"],
                    expected_row_count=t["expected_row_count"],
                )
            )
        return table_list
