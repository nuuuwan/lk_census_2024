import os

from lk_census.original_doc.OriginalDoc import OriginalDoc
from utils_future import JSONFile


class XLSXDataTableLoaderMixin:
    XLSX_TABLE_METADATA_PATH = os.path.join(
        OriginalDoc.DIR_ORIGINAL_DOCS, "metadata", "xlsx_tables.json"
    )

    @classmethod
    def list_all(cls):
        table_list = []
        configs = JSONFile(cls.XLSX_TABLE_METADATA_PATH).read()
        for t in configs:
            table_list.append(
                cls(
                    doc_name=t["doc_name"],
                    table_title=t["table_title"],
                    column_offset=t["column_offset"],
                    field_list=t["field_list"],
                    has_province_info=t.get("has_province_info", True),
                )
            )
        return table_list
