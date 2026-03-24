import os
import re
from dataclasses import dataclass

from utils import WWW, File, JSONFile, Log

log = Log("OriginalDoc")


@dataclass
class OriginalDoc:
    url: str
    file_path: str

    DIR_ORIGINAL_DOCS = "original_docs"
    DOC_METADATA_PATH = os.path.join(
        DIR_ORIGINAL_DOCS, "metadata", "docs.json"
    )
    URL_BASE = "https://www.statistics.gov.lk"

    @property
    def doc_name(self) -> str:
        file_name = os.path.basename(self.file_path)
        file_name = os.path.splitext(file_name)[0]

        safe_name = re.sub(r"\s+", " ", file_name)
        safe_name = file_name.replace(" ", "-")
        safe_name = file_name.replace("_", "-")
        safe_name = "".join(
            char for char in safe_name if char.isalnum() or char == "-"
        )
        tokens = safe_name.split("-")
        return "-".join(tokens)

    @property
    def pdf_path(self) -> str:
        if not self.file_path.lower().endswith(".pdf"):
            raise ValueError(f"file_path '{self.file_path}' is not a PDF")
        return self.file_path

    @property
    def title(self) -> str:
        return os.path.basename(self.file_path)

    def download(self) -> str:
        if os.path.exists(self.file_path):
            log.warning(f"{File(self.file_path)} exists. Skipping download.")
            return self.file_path
        www = WWW(self.url)
        os.makedirs(self.DIR_ORIGINAL_DOCS, exist_ok=True)
        www.download_binary(self.file_path)
        log.info(f"Downloaded '{self.url}' to '{File(self.file_path)}'")
        return self.file_path

    @classmethod
    def list_all(cls) -> list["OriginalDoc"]:
        doc_list = []
        for t in JSONFile(cls.DOC_METADATA_PATH).read():
            doc = cls(url=t["url"], file_path=t["file_path"])
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
