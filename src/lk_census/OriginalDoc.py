import os
import re
from dataclasses import dataclass

from utils import WWW, File, Log

log = Log("OriginalDoc")


@dataclass
class OriginalDoc:
    title: str
    url_prefix: str

    DIR_ORIGINAL_DOCS = "original_docs"
    README_PATH = os.path.join(DIR_ORIGINAL_DOCS, "README.md")
    URL_BASE = "https://www.statistics.gov.lk"

    @property
    def url(self) -> str:
        return f"{self.URL_BASE}/{self.url_prefix}"

    @property
    def file_path(self) -> str:
        safe_name = re.sub(r"\s+", " ", self.title)
        safe_name = self.title.replace(" ", "-")
        safe_title = "".join(
            char for char in safe_name if char.isalnum() or char == "-"
        )
        return os.path.join(self.DIR_ORIGINAL_DOCS, f"{safe_title}.pdf")

    def download(self) -> str:
        if os.path.exists(self.file_path):
            log.warning(f"{File(self.file_path)} exists. Skipping download.")
            return self.file_path
        www = WWW(self.url)
        os.makedirs(self.DIR_ORIGINAL_DOCS, exist_ok=True)
        www.download_binary(self.file_path)
        log.info(f"Downloaded '{self.title}' to '{File(self.file_path)}'")
        return self.file_path

    BASIC_POPULATION = (
        "Basic Population"
        + " by Districts and Divisional Secretary Divisions",
        "Resource/en/Population/CPH_2024"
        + "/Population_Preliminary_Report.pdf",
    )

    BASIC_HOUSING = (
        "Basic Housing Information"
        + " by Districts and Divisional Secretary Divisions",
        "Resource/en/Population/CPH_2024" + "/Housing_Preliminary_Report.pdf",
    )

    PRELIMINARY_REPORT = (
        "Population of Sri Lanka"
        + " by District - Census of Population & Housing 2024",
        "Resource/en/Population/CPH_2024" + "/CPH2024_Preliminary_Report.pdf",
    )

    @classmethod
    def list_all(cls) -> list["OriginalDoc"]:
        doc_list = []
        for t in [
            cls.BASIC_POPULATION,
            cls.BASIC_HOUSING,
            cls.PRELIMINARY_REPORT,
        ]:
            doc = cls(*t)
            doc_list.append(doc)
        return doc_list

    @classmethod
    def download_all(cls):
        for original_doc in cls.list_all():
            original_doc.download()

    @classmethod
    def build_readme(cls):
        lines = [
            "# Original Documents for Census 2024",
            "",
            "The following original documents have been"
            + f" downloaded from [{cls.URL_BASE}]({cls.URL_BASE})",
            "",
        ]
        for i_doc, original_doc in enumerate(cls.list_all(), start=1):
            lines.append(
                f"{i_doc}. [{original_doc.title}]"
                + f"({os.path.basename(original_doc.file_path)})"
            )
        lines.append("")
        readme_file = File(cls.README_PATH)
        readme_file.write_lines(lines)
        log.info(f" Wrote {readme_file}")
