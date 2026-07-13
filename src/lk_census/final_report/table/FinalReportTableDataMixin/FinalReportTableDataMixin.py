import json
import os

from utils_future import JSONFile, Log

from .FinalReportTableDataAggregateMixin import (
    FinalReportTableDataAggregateMixin,
)
from .FinalReportTableDataFieldsMixin import FinalReportTableDataFieldsMixin
from .FinalReportTableDataOtherValuesMixin import (
    FinalReportTableDataOtherValuesMixin,
)
from .FinalReportTableDataRowMixin import FinalReportTableDataRowMixin

log = Log("FinalReportTableDataMixin")


class FinalReportTableDataMixin(
    FinalReportTableDataFieldsMixin,
    FinalReportTableDataRowMixin,
    FinalReportTableDataOtherValuesMixin,
    FinalReportTableDataAggregateMixin,
):
    MIN_N_DATA_LIST = 5

    @property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    def _build_data_list(self):
        d_list = []
        for raw_data in self.raw_data_list:
            d = self._build_data_item(raw_data)
            if d is not None:
                d_list.append(d)
        return d_list

    def _validate_data_list(self, d_list):
        if len(d_list) >= self.MIN_N_DATA_LIST:
            return
        raise ValueError(
            f"[{self}] Expected >={self.MIN_N_DATA_LIST} data items,"
            + f" found only {len(d_list)}"
        )

    def build_data(self, force=False):

        if self.data_file.exists and not force:
            return
        if not (bool(self.raw_data_list) and bool(self.fields)):
            return

        log.debug("-" * 40)
        log.debug(f"[{self}] Building DATA")
        log.debug("-" * 40)

        d_list = self._build_data_list()

        self._validate_data_list(d_list)
        if self.is_expandable:
            d_list = self._expand_data_list(d_list)
        self.data_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.data_file}")

    @property
    def data_list(self):
        if not self.data_file.exists:
            return None
        return self.data_file.read()
