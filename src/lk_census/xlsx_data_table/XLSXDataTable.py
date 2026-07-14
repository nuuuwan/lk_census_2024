import os

from lk_census.common.CommonTableReadMeMixin import (
    CommonTableReadMeMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableAllDataMixin import (
    XLSXDataTableAllDataMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableBase import XLSXDataTableBase
from lk_census.xlsx_data_table.XLSXDataTableBuilderMixin import (
    XLSXDataTableBuilderMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableDownloadMixin import (
    XLSXDataTableDownloadMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableGNDDataMixin import (
    XLSXDataTableGNDDataMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableLankaDataMixin import (
    XLSXDataTableLankaDataMixin,
)
from lk_census.xlsx_data_table.XLSXDataTableLoaderMixin import (
    XLSXDataTableLoaderMixin,
)
from utils_future import JSONFile, Log

log = Log("XLSXDataTable")


class XLSXDataTable(
    XLSXDataTableBase,
    XLSXDataTableLoaderMixin,
    XLSXDataTableBuilderMixin,
    #
    XLSXDataTableDownloadMixin,
    XLSXDataTableGNDDataMixin,
    XLSXDataTableAllDataMixin,
    XLSXDataTableLankaDataMixin,
    CommonTableReadMeMixin,
):
    @property
    def base_dir(self):
        return "../../"
