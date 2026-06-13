from lk_census.readme.ReadMeDataTableMixin import ReadMeDataTableMixin
from lk_census.xlsx_data_table import XLSXDataTable
from utils_future import File, Format, Log, Time, TimeFormat

log = Log("ReadMe")


class ReadMe(ReadMeDataTableMixin):
    PATH = "README.md"

    def get_lines_for_header(self, data_table_list) -> list[str]:
        time_updated_for_badge = Format.badge(
            TimeFormat.TIME.format(Time.now())
        )
        n = len(data_table_list)
        return [
            "# 🇱🇰 Sri Lanka - " + "Census of Population and Housing 2024",
            "",
            "![CPH]" + "(https://img.shields.io/badge/CPH-2024-blue)",
            "![LastUpdated](https://img.shields.io/badge"
            + f"/last_updated-{time_updated_for_badge}-green)",
            "",
            f"{n} Datasets on Population and Housing"
            + " by Country, Province, District,"
            + " Divisional Secretariat Division (DSD),"
            + " Grama Niladhari Division (GND), Electoral District (ED),"
            + " Polling Division (PD), and"
            + " Local Government Authority (LG) levels.",
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
        return (
            self.get_lines_for_header(data_table_list)
            + self.get_lines_for_xlsx_data_tables(data_table_list)
            + self.get_lines_for_footer()
        )

    def build(self):
        readme_file = File(self.PATH)
        readme_file.write_lines(self.get_lines())
        log.info(f"Wrote {readme_file}")
