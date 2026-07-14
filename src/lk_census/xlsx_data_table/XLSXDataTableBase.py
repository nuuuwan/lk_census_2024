import os
from dataclasses import dataclass

from utils_future import JSONFile


@dataclass
class XLSXDataTableBase:
    data_table_id: str
    remote_file_name: str
    total_col_index: int
    fields_col_start_index: int
    field_list: list[str]
    has_province_info: bool
    expected_total_value: int
    expected_row_count: int

    @property
    def n_fields(self) -> int:
        return len(self.field_list)

    @property
    def table_name(self):
        return self.data_table_id

    @property
    def source_description(self):
        return ", ".join(
            [
                self.table_name,
                "2024 Census of Population and Housing",
                "Department of Census and Statistics, Sri Lanka",
            ]
        )
