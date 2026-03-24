import os

from utils import JSONFile

from lk_census.original_doc.OriginalDoc import OriginalDoc


class XLSXDataTableLoaderMixin:
    XLSX_TABLE_METADATA_PATH = os.path.join(
        OriginalDoc.DIR_ORIGINAL_DOCS, "metadata", "xlsx_tables.json"
    )

    @classmethod
    def list_all(cls):
        table_list = []
        for t in JSONFile(cls.XLSX_TABLE_METADATA_PATH).read():
            table_list.append(
                cls(
                    doc_name=t["doc_name"],
                    table_title=t["table_title"],
                    column_offset=t["column_offset"],
                    field_list=t["field_list"],
                )
            )
        return table_list
