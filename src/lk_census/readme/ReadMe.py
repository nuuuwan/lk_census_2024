from utils_future import File, Format, Log, Time, TimeFormat

from lk_census.final_report.table import FinalReportTable
from lk_census.readme.ReadMeDataTableMixin import ReadMeDataTableMixin
from lk_census.readme.ReadMeFinalReportMixin import ReadMeFinalReportMixin
from lk_census.xlsx_data_table import XLSXDataTable

log = Log("ReadMe")


class ReadMe(ReadMeDataTableMixin, ReadMeFinalReportMixin):
    PATH = "README.md"

    def get_lines_for_header(self, n_xlsx, n_final) -> list[str]:
        time_updated_for_badge = Format.badge(
            TimeFormat.TIME.format(Time.now())
        )
        n = n_xlsx + n_final
        return [
            "# 🇱🇰 Sri Lanka - " + "Census of Population and Housing 2024",
            "",
            "![CPH]" + "(https://img.shields.io/badge/CPH-2024-blue)",
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
            "",
            f"**{n:,}** Datasets on Population, Housing and more,"
            + " by Country, Province, District,"
            + " Divisional Secretariat Division (DSD),"
            + " Grama Niladhari Division (GND), Electoral District (ED),"
            + " Polling Division (PD), and"
            + " Local Government Authority (LG) levels.",
            "",
            f"- **{n_xlsx:,}** Datasets from Excel Files"
            + " shared on the Website of the"
            + " [Department of Census and Statistics, Sri Lanka]"
            + f"({XLSXDataTable.URL_BASE}),",
            f"- **{n_final:,}** Datasets from the"
            + " [Final Report of the Census]"
            + f"({FinalReportTable.URL_FINAL_REPORT})",
            "",
        ]

    def get_lines_for_footer(self) -> list[str]:
        return [
            "![Maintainer]"
            + "(https://img.shields.io/badge/maintainer-nuuuwan-red)",
            "![MadeWith]"
            + "(https://img.shields.io/badge/made_with-python-blue)",
            "[![License: MIT]"
            + "(https://img.shields.io/badge/License-MIT-yellow.svg)]"
            + "(https://opensource.org/licenses/MIT)",
            "",
        ]

    def get_lines(self) -> list[str]:
        data_table_list = XLSXDataTable.list_all()
        final_report_table_list = FinalReportTable.list()
        n_xlsx = len(data_table_list)
        n_final = len(final_report_table_list)
        return (
            self.get_lines_for_header(n_xlsx, n_final)
            + self.get_lines_for_xlsx_data_tables(data_table_list)
            + self.get_lines_for_final_report(final_report_table_list)
            + self.get_lines_for_footer()
        )

    def build(self):
        readme_file = File(self.PATH)
        readme_file.write("\n".join(self.get_lines()))
        log.info(f"Wrote {readme_file}")
