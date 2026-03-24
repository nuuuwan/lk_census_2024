import os

from utils import JSONFile

from lk_census.original_doc.OriginalDoc import OriginalDoc


class DataTableLoaderMixin:
    PDF_TABLE_METADATA_PATH = os.path.join(
        OriginalDoc.DIR_ORIGINAL_DOCS, "metadata", "pdf_tables.json"
    )

    @classmethod
    def list_all(cls):
        table_list = []
        for t in JSONFile(cls.PDF_TABLE_METADATA_PATH).read():
            table_list.append(
                cls(
                    original_doc=OriginalDoc.from_doc_name(t["doc_name"]),
                    table_title=t["table_title"],
                    pages=tuple(t["pages"]),
                    field_list=t["field_list"],
                )
            )
        return table_list
