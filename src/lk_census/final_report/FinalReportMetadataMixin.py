from lk_census.final_report.FinalReportConstants import FinalReportConstants
from utils_future import Log, Parse

log = Log("FinalReportMetadataMixin")


class FinalReportMetadataMixin:

    @staticmethod
    def clean(text):
        text = text.replace(".", "")
        return text.strip()

    @staticmethod
    def extract_table_index(force=False):
        if not FinalReportConstants.TABLE_INDEX_PDF_FILE.exists or force:
            FinalReportConstants.PDF_FILE.extract_subset(
                FinalReportConstants.TABLE_INDEX_START_PAGE,
                FinalReportConstants.TABLE_INDEX_END_PAGE,
                FinalReportConstants.TABLE_INDEX_PDF_FILE,
            )

        if not FinalReportConstants.TABLE_INDEX_TXT_FILE.exists or force:
            FinalReportConstants.TABLE_INDEX_PDF_FILE.to_text_file(
                FinalReportConstants.TABLE_INDEX_TXT_FILE
            )

    @staticmethod
    def build_table_metadata(force=False):
        if FinalReportConstants.TABLE_INDEX_TXT_FILE.exists and not force:
            return
        d_list = []
        lines = FinalReportMetadataMixin.TABLE_INDEX_TXT_FILE.read_lines()
        for i_line, line in enumerate(lines, start=0):
            if not line.startswith("Table"):
                continue
            words = line.strip().split(" ")
            page_num = Parse.int(words[-1])

            if page_num is None or not (
                FinalReportConstants.MIN_VALID_TABLE_PAGE_NUM
                <= page_num
                <= FinalReportConstants.MAX_VALID_TABLE_PAGE_NUM
            ):
                new_line = line.strip() + lines[i_line + 1].strip()
                words = new_line.strip().split(" ")
                page_num = Parse.int(words[-1])
                assert (
                    page_num is not None
                ), f"Failed to parse page number from line: {new_line}"
                assert (
                    FinalReportConstants.MIN_VALID_TABLE_PAGE_NUM
                    <= page_num
                    <= FinalReportConstants.MAX_VALID_TABLE_PAGE_NUM
                ), (
                    f"Page number {page_num}"
                    + f" out of valid range in line: {new_line}"
                )

            table_num = words[1]
            table_name = FinalReportMetadataMixin.clean(" ".join(words[3:-2]))
            d = dict(
                table_num=table_num, table_name=table_name, page_num=page_num
            )
            d_list.append(d)

        page_num_to_d_list = {}
        for d in d_list:
            page_num = d["page_num"]
            if page_num not in page_num_to_d_list:
                page_num_to_d_list[page_num] = []
            page_num_to_d_list[page_num].append(d)

        for d in d_list:
            page_num = d["page_num"]
            has_page_multiple_tables = len(page_num_to_d_list[page_num]) > 1
            d["has_page_multiple_tables"] = has_page_multiple_tables

        FinalReportConstants.TABLE_METADATA_FILE.write(d_list)
        log.info(f"Wrote {
                len(d_list)} tables to {
                FinalReportConstants.TABLE_METADATA_FILE}")
