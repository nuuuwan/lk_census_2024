import json

from lk_census.final_report.table.FinalReportTable import FinalReportTable
from utils_future import Markdown


class ReadMeFinalReportMixin:
    URL_FINAL_REPORT = FinalReportTable.URL_FINAL_REPORT

    def flatten_dict(self, d):
        flat_d = {}
        for k, v in d.items():
            if k == "values":
                for k1, v1 in v.items():
                    flat_d[k1.replace("_", " ").title()] = v1
            else:
                flat_d[k.replace("_", " ").title()] = v
        return flat_d

    def get_lines_for_final_report_table_with_pdf_data(
        self, final_report_table
    ):
        assert final_report_table.original_pdf_image_file.exists
        lines = [
            "### Original Table",
            "",
            f"![{final_report_table.table_id}]"
            + f"({final_report_table.original_pdf_image_file.path})",
            "",
        ]
        return lines

    def get_lines_for_final_report_table_with_raw_data(
        self, final_report_table
    ):
        assert final_report_table.raw_data_file.exists
        lines = []

        example_rows = final_report_table.raw_data_list[:10]
        max_cols = max(len(row) for row in example_rows)

        d_list = [
            {
                f"Col {i}": row[i] if i < len(row) else "--"
                for i in list(range(max_cols))
            }
            for row in example_rows
        ]
        lines.extend(
            [
                "### Raw Data (first 10 rows)",
                "",
            ]
            + Markdown.table(d_list)
        )

        return lines

    def get_lines_for_final_report_table_with_raw_data_complicated(
        self, final_report_table
    ):
        assert final_report_table.raw_data_file.exists
        lines = []

        example_rows = final_report_table.raw_data_list[:10]
        max_cols = max(len(row) for row in example_rows)

        d_list = [
            {
                f"Col {i}": row[i] if i < len(row) else "--"
                for i in list(range(max_cols))
            }
            for row in example_rows
        ]
        lines.extend(
            [
                "### Raw Data (first 10 rows)",
                "",
            ]
            + Markdown.table(d_list)
        )

        return lines

    def get_lines_for_final_report_table_with_structured_data(
        self, final_report_table
    ):
        assert final_report_table.data_file.exists
        N_DISPLAY = 10

        d_list_for_table = [
            self.flatten_dict(d) for d in final_report_table.data_list
        ]
        n_total = len(d_list_for_table)

        title = "Data Table"
        if N_DISPLAY < n_total:
            title += f" (first {N_DISPLAY} of {n_total} rows)"
            d_list_for_table = d_list_for_table[:N_DISPLAY]

        lines = []
        lines.extend(
            [
                f"### {title}",
                "",
            ]
            + Markdown.table(d_list_for_table)
        )
        lines.extend(
            [
                "### Example Data Row (JSON)",
                "",
                "```json",
                json.dumps(d_list_for_table[0], indent=4),
                "```",
                "",
            ]
        )

        return lines

    def get_lines_for_final_report_table_with_lanka_data(
        self, final_report_table
    ):
        assert final_report_table.data_file.exists
        N_DISPLAY_LINES = 30

        data_lines = json.dumps(final_report_table.lanka_data, indent=4).split(
            "\n"
        )
        n_data_lines = len(data_lines)

        if n_data_lines > N_DISPLAY_LINES:
            data_lines = data_lines[:N_DISPLAY_LINES] + ["..."]
            title = (
                f"Lanka Data (first {N_DISPLAY_LINES} of {n_data_lines} lines)"
            )
        else:
            title = "Lanka Data"

        lines = []
        lines.extend(
            [
                f"### {title}",
                "",
                "```json",
            ]
            + data_lines
            + [
                "```",
                "",
            ]
        )

        return lines

    def _get_lines_for_final_report_table_inner(self, final_report_table):
        status = final_report_table.build_status

        if status == 5:
            return self.get_lines_for_final_report_table_with_lanka_data(
                final_report_table
            )

        if status == 4 or status == 5:
            return self.get_lines_for_final_report_table_with_structured_data(
                final_report_table
            )

        if status == 3:
            return self.get_lines_for_final_report_table_with_raw_data(
                final_report_table
            )

        if status == 2:
            return self.get_lines_for_final_report_table_with_raw_data_complicated(
                final_report_table
            )

        if status == 1:
            return self.get_lines_for_final_report_table_with_pdf_data(
                final_report_table
            )

        raise ValueError(
            f"Final report table {final_report_table.table_num} "
            + "does not have any data file"
        )

    def get_lines_for_final_report_table(self, i_dataset, final_report_table):
        description = FinalReportTable.STATUS_LABELS[
            final_report_table.build_status
        ]
        lines = [
            f"## {i_dataset}. [{final_report_table.table_name}]"
            + f"({final_report_table.dir_data})",
            "",
            f"*Build Status (**{final_report_table.build_status}**)"
            + f" {description}*",
            "",
        ]
        lines.extend(
            self._get_lines_for_final_report_table_inner(final_report_table)
        )
        lines.extend(
            [
                "### Source",
                "",
                f"- [{self.URL_FINAL_REPORT}]({self.URL_FINAL_REPORT})"
                + f" (Table {final_report_table.table_num})",
                "",
            ]
        )
        return lines

    def get_lines_for_final_report_status(self, final_report_table_list):
        status_to_n = {}
        for final_report_table in final_report_table_list:
            status = final_report_table.build_status
            if status not in status_to_n:
                status_to_n[status] = 0
            status_to_n[status] += 1

        lines = [
            "## `Final Report Build Status`",
            "",
        ]
        status_to_n = dict(sorted(status_to_n.items(), key=lambda x: x[0]))
        d_list = [
            dict(
                status=status,
                status_label=FinalReportTable.STATUS_LABELS[status],
                n=n,
            )
            for status, n in status_to_n.items()
        ]
        lines.extend(Markdown.table(d_list))
        return lines

    def get_lines_for_final_report(
        self, n_datasets_non_final_table, final_report_table_list
    ):
        len(final_report_table_list)

        lines = self.get_lines_for_final_report_status(final_report_table_list)
        i_dataset = n_datasets_non_final_table + 1
        for final_report_table in final_report_table_list:

            lines.extend(
                self.get_lines_for_final_report_table(
                    i_dataset, final_report_table
                )
            )
            i_dataset += 1
        return lines
