from lk_census.xlsx_data_table.XLSXDataTableBase import XLSXDataTableBase
from lk_census.xlsx_data_table.XLSXDataTableBuilderMixin import \
    XLSXDataTableBuilderMixin
from lk_census.xlsx_data_table.XLSXDataTableDownloadMixin import \
    XLSXDataTableDownloadMixin
from lk_census.xlsx_data_table.XLSXDataTableExpandDataMixin import \
    XLSXDataTableExpandDataMixin
from lk_census.xlsx_data_table.XLSXDataTableExtractDataMixin import \
    XLSXDataTableExtractDataMixin
from lk_census.xlsx_data_table.XLSXDataTableLoaderMixin import \
    XLSXDataTableLoaderMixin
from utils_future import Log

log = Log("XLSXDataTable")


class XLSXDataTable(
    XLSXDataTableBase,
    XLSXDataTableLoaderMixin,
    XLSXDataTableBuilderMixin,
    #
    XLSXDataTableDownloadMixin,
    XLSXDataTableExtractDataMixin,
    XLSXDataTableExpandDataMixin,
):
    pass
