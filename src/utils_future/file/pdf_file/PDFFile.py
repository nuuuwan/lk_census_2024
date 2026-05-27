import pymupdf
from utils_base.console.Log import Log
from utils_base.file.File import File
from utils_base.file.pdf_file.PDFFileCompressMixin import PDFFileCompressMixin
from utils_base.file.pdf_file.PDFTextMixin import PDFTextMixin

log = Log("PDFFile")


class PDFFile(File, PDFTextMixin, PDFFileCompressMixin):

    def __init__(self, path):
        assert path.endswith(".pdf")
        super().__init__(path)

    def download_image(self, i_page: int, image_path: str) -> None:
        doc = pymupdf.open(self.path)
        page = doc[i_page]
        pix = page.get_pixmap()
        pix.save(image_path)
        log.info(f"Wrote image {self} to {image_path}")
