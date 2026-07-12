import os

from utils_future import File, JSONFile, Log, PDFFile

log = Log("FinalReport")


class FinalReport:
    PDF_FILE = PDFFile(os.path.join("original_docs", "CPH2024_Final_Eng.pdf"))

    TABLE_INDEX_START_PAGE, TABLE_INDEX_END_PAGE = 11, 13
    TABLE_INDEX_PDF_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.pdf")
    )
    TABLE_INDEX_TXT_FILE = PDFFile(
        os.path.join("derived_docs", "final-report-index.txt")
    )
    MIN_VALID_TABLE_PAGE_NUM, MAX_VALID_TABLE_PAGE_NUM = 6, 205

    @staticmethod
    def extract_table_index():
        FinalReport.PDF_FILE.extract_subset(
            FinalReport.TABLE_INDEX_START_PAGE,
            FinalReport.TABLE_INDEX_END_PAGE,
            FinalReport.TABLE_INDEX_PDF_FILE,
        )
        FinalReport.TABLE_INDEX_PDF_FILE.to_text_file(
            FinalReport.TABLE_INDEX_TXT_FILE
        )

    TABLE_METADATA_FILE = JSONFile(
        os.path.join("derived_docs", "final-report-index.metadata.json")
    )

    @staticmethod
    def build_table_metadata():

        def clean(text):
            text = text.replace(".", "")
            return text.strip()

        def parse_int(text):
            try:
                return int(text)
            except ValueError:
                return None

        d_list = []
        lines = FinalReport.TABLE_INDEX_TXT_FILE.read_lines()
        for i_line, line in enumerate(lines, start=0):
            if not line.startswith("Table"):
                continue
            words = line.strip().split(" ")
            page_num = parse_int(words[-1])

            if page_num is None or not (
                FinalReport.MIN_VALID_TABLE_PAGE_NUM
                <= page_num
                <= FinalReport.MAX_VALID_TABLE_PAGE_NUM
            ):
                new_line = line.strip() + lines[i_line + 1].strip()
                words = new_line.strip().split(" ")

                page_num = parse_int(words[-1])
                assert (
                    page_num is not None
                ), f"Failed to parse page number from line: {new_line}"
                assert (
                    FinalReport.MIN_VALID_TABLE_PAGE_NUM
                    <= page_num
                    <= FinalReport.MAX_VALID_TABLE_PAGE_NUM
                ), f"Page number {page_num} out of valid range in line: {new_line}"

            table_num = words[1]
            table_name = clean(" ".join(words[3:-2]))
            d = dict(
                table_num=table_num, table_name=table_name, page_num=page_num
            )
            d_list.append(d)
        FinalReport.TABLE_METADATA_FILE.write(d_list)
        log.info(
            f"Wrote {len(d_list)} tables to {FinalReport.TABLE_METADATA_FILE}"
        )

    @staticmethod
    def parse():
        FinalReport.extract_table_index()
        FinalReport.build_table_metadata()
