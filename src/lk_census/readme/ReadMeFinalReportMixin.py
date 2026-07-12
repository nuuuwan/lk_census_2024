import json


class ReadMeFinalReportMixin:
    URL_FINAL_REPORT = (
        "https://www.statistics.gov.lk"
        + "/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf"
    )

    def get_lines_for_final_report_table(self, final_report_table):
        lines = [
            f"#### [Table {final_report_table.table_num}]"
            + f"({final_report_table.dir_data})"
            + f" - {final_report_table.table_name}",
        ]

        if final_report_table.data_file.exists:
            example_row = final_report_table.data_list[0]
            lines.extend(
                [
                    "##### Example Data Row (JSON)",
                    "",
                    "```json",
                    json.dumps(example_row, indent=4),
                    "```",
                    "",
                ]
            )

        return lines

    def get_lines_for_final_report(self, final_report_table_list):
        n = len(final_report_table_list)

        lines = [
            "## Final Report Tables",
            "",
            f"**{n}** tables have been extracted from the"
            + " [Census of Population and Housing - 2024 Final Report]"
            + f"({self.URL_FINAL_REPORT})",
            "",
            f"- Source: <{self.URL_FINAL_REPORT}>",
            "",
        ]

        idx = {}
        for final_report_table in final_report_table_list:
            chapter_num = final_report_table.chapter_num
            if chapter_num not in idx:
                idx[chapter_num] = []
            idx[chapter_num].append(final_report_table)

        for chapter_num, final_report_table_list_for_chapter in idx.items():
            lines.extend([f"### Chapter {chapter_num}", ""])
            for final_report_table in final_report_table_list_for_chapter:
                lines.extend(
                    self.get_lines_for_final_report_table(final_report_table)
                )
        return lines
