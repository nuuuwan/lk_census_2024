import os

from utils import File, Log

log = Log("OriginalDoc")


class OriginalDocReadMeMixin:
    DIR_ORIGINAL_DOCS = "original_docs"
    README_PATH = os.path.join(DIR_ORIGINAL_DOCS, "README.md")

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
                + f"({os.path.basename(original_doc.pdf_path)})"
            )
        lines.append("")
        readme_file = File(cls.README_PATH)
        readme_file.write_lines(lines)
        log.info(f" Wrote {readme_file}")
