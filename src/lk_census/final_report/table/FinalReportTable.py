from lk_census.final_report.table.data import (
    FinalReportTableDataMixin,
)
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
from utils_future import Log

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
):
    pass
