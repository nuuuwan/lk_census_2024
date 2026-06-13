from dataclasses import dataclass


@dataclass
class XLSXDataTableBase:
    data_table_id: str
    remote_file_name: str
    column_offset: int
    field_list: list[str]
    has_province_info: bool

    @property
    def n_fields(self) -> int:
        return len(self.field_list)
