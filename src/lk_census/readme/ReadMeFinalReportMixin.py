from utils_future import Markdown

from lk_census.final_report.table.FinalReportTable import FinalReportTable


class ReadMeFinalReportMixin:

    def get_lines_for_final_report_status(self, final_report_table_list):
        status_to_n = {}
        for final_report_table in final_report_table_list:
            status = final_report_table.build_status
            if status not in status_to_n:
                status_to_n[status] = 0
            status_to_n[status] += 1

        lines = [
            "### Final Report Build Status",
            "",
        ]
        status_to_n = dict(sorted(status_to_n.items(), key=lambda x: x[0]))
        total = len(final_report_table_list)
        d_list = [
            dict(
                status=f"**{status}**/5",
                status_label=FinalReportTable.STATUS_EMOJIS[status]
                + " "
                + FinalReportTable.STATUS_LABELS[status],
                n=f"**{n:,}**",
                n_raw=n,
                p=f"**{n / total:.1%}**",
                color=FinalReportTable.STATUS_COLORS[status],
            )
            for status, n in status_to_n.items()
        ]
        lines.extend(Markdown.table(d_list))
        lines.extend(
            Markdown.pie_chart(
                "Final Report Build Status",
                d_list,
                "status_label",
                "n_raw",
                "color",
            )
        )
        return lines

    def get_lines_for_final_report_table(self, final_report_table):
        emoji = FinalReportTable.STATUS_EMOJIS[final_report_table.build_status]
        return [
            f"- {emoji} Table {final_report_table.table_num}"
            + f" - [{final_report_table.table_name}]"
            + f"({final_report_table.readme_file.path})"
        ]

    @staticmethod
    def _group_by_chapter(table_list):
        idx = {}
        for table in table_list:
            chapter = table.chapter_num
            if chapter not in idx:
                idx[chapter] = []
            idx[chapter].append(table)
        return idx

    def get_lines_for_final_report(self, final_report_table_list):
        n = len(final_report_table_list)

        lines = [
            f"## Datasets from Final Report (**{n:,}**)",
            "",
            "*Smaller tables spanning a wide range of topics.*",
            "",
        ]

        idx = self._group_by_chapter(final_report_table_list)
        for chapter, table_list_for_chapter in idx.items():
            lines.extend([f"### Chapter {chapter}", ""])
            for final_report_table in table_list_for_chapter:
                lines.extend(
                    self.get_lines_for_final_report_table(final_report_table)
                )
            lines.append("")
        lines.append("")
        lines.extend(
            [""]
            + self.get_lines_for_final_report_status(final_report_table_list)
        )

        return lines
