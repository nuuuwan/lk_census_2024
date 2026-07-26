import os

from utils_future import Log

from lk_census.common.CommonTableReadMeMixin import CommonTableReadMeMixin
from lk_census.final_report.table.data import FinalReportTableDataMixin
from lk_census.final_report.table.FinalReportTableBase import (
    FinalReportTableBase,
)
from lk_census.final_report.table.FinalReportTableBuildMixin import (
    FinalReportTableBuildMixin,
)
from lk_census.final_report.table.FinalReportTableIsComplicatedMixin import (
    FinalReportTableIsComplicatedMixin,
)
from lk_census.final_report.table.FinalReportTableLoadMixin import (
    FinalReportTableLoadMixin,
)
from lk_census.final_report.table.FinalReportTablePDFMixin import (
    FinalReportTablePDFMixin,
)
from lk_census.final_report.table.FinalReportTableRawDataMixin import (
    FinalReportTableRawDataMixin,
)
from lk_census.final_report.table.lanka_data.FinalReportLankaDataMixin import (
    FinalReportLankaDataMixin,
)

log = Log("FinalReportTable")


class FinalReportTable(
    FinalReportTableBase,
    FinalReportTablePDFMixin,
    FinalReportTableRawDataMixin,
    FinalReportTableDataMixin,
    FinalReportLankaDataMixin,
    FinalReportTableBuildMixin,
    FinalReportTableIsComplicatedMixin,
    FinalReportTableLoadMixin,
    CommonTableReadMeMixin,
):
    def oneoff_fix_id(self):
        dir_data = self.dir_data
        dir_data2 = self.dir_data2
        if dir_data == dir_data2:
            return
        if not os.path.exists(dir_data):
            return
        os.rename(dir_data, dir_data2)
