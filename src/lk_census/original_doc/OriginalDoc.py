import os
import re
from dataclasses import dataclass

from utils import WWW, File, JSONFile, Log

from lk_census.original_doc.OriginalDocReadMeMixin import \
    OriginalDocReadMeMixin

log = Log("OriginalDoc")


@dataclass
class OriginalDoc(OriginalDocReadMeMixin):
    title: str
    url_prefix: str

    DIR_ORIGINAL_DOCS = "original_docs"
    URL_BASE = "https://www.statistics.gov.lk"
    METADATA_PATH = os.path.join(DIR_ORIGINAL_DOCS, "metadata.json")

    @property
    def url(self) -> str:
        return f"{self.URL_BASE}/{self.url_prefix}"

    @property
    def doc_name(self) -> str:
        safe_name = re.sub(r"\s+", " ", self.title)
        safe_name = self.title.replace(" ", "-")
        safe_name = "".join(
            char for char in safe_name if char.isalnum() or char == "-"
        )
        tokens = safe_name.split("-")
        return "-".join(tokens[:2])

    @property
    def pdf_path(self) -> str:
        return os.path.join(self.DIR_ORIGINAL_DOCS, f"{self.doc_name}.pdf")

    def download(self) -> str:
        if os.path.exists(self.pdf_path):
            log.warning(f"{File(self.pdf_path)} exists. Skipping download.")
            return self.pdf_path
        www = WWW(self.url)
        os.makedirs(self.DIR_ORIGINAL_DOCS, exist_ok=True)
        www.download_binary(self.pdf_path)
        log.info(f"Downloaded '{self.title}' to '{File(self.pdf_path)}'")
        return self.pdf_path

    @classmethod
    def list_all(cls) -> list["OriginalDoc"]:
        doc_list = []
        for t in JSONFile(cls.METADATA_PATH).read():
            doc = cls(*t)
            doc_list.append(doc)
        return doc_list

    @classmethod
    def from_doc_name(cls, doc_name: str) -> "OriginalDoc":
        for original_doc in cls.list_all():
            if original_doc.doc_name == doc_name:
                return original_doc
        raise ValueError(f"No OriginalDoc with doc_name='{doc_name}'")

    @classmethod
    def download_all(cls):
        for original_doc in cls.list_all():
            original_doc.download()
