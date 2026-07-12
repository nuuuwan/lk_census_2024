import json

from utils_future import Markdown


class ReadMeFinalReportMixin:
    URL_FINAL_REPORT = (
        "https://www.statistics.gov.lk"
        + "/Resource/en/Population/CPH_2024/CPH2024_Final_Eng.pdf"
    )

    def flatten_dict(self, d):
        flat_d = {}
        for k, v in d.items():
            if k == "values":
                for k1, v1 in v.items():
                    flat_d[k1.replace("_", " ").title()] = v1
            else:
                flat_d[k.replace("_", " ").title()] = v
        return flat_d

    def get_lines_for_final_report_table(self, final_report_table):
        lines = [
            f"#### [Table {final_report_table.table_num}]"
            + f"({final_report_table.dir_data})"
            + f" - {final_report_table.table_name}",
            "",
        ]

        if final_report_table.data_file.exists:
            d_list = final_report_table.data_list
            d_list_by_district = [
                d for d in d_list if d["region_ent_type"] == "district"
            ]
            d_list_for_table = [
                self.flatten_dict(d) for d in d_list_by_district
            ]

            lines.extend(
                [
                    "##### Data by District",
                    "",
                ]
                + Markdown.table(d_list_for_table)
            )
            lines.extend(
                [
                    "##### Example Data Row (JSON)",
                    "",
                    "```json",
                    json.dumps(d_list_by_district[0], indent=4),
                    "```",
                    "",
                ]
            )

        elif final_report_table.raw_data_file.exists:
            example_rows = final_report_table.raw_data_list[:10]

            d_list = [
                {f"Col {i}": cell for i, cell in enumerate(row, start=1)}
                for row in example_rows
            ]
            lines.extend(
                [
                    "##### Raw Data (first 10 rows)",
                    "",
                ]
                + Markdown.table(d_list)
                + [""]
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
