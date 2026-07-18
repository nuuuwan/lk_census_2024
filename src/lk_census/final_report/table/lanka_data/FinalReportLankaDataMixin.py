import os

from ds import DimToTimeToValueAdapter, RegionValueAdapter
from utils_future import JSONFile, Log

from lk_census.final_report.table.lanka_data.FinalReportLankaMetaDataMixin import (
    FinalReportLankaMetaDataMixin,
)

log = Log("FinalReportLankaDataMixin")


class FinalReportLankaDataMixin(FinalReportLankaMetaDataMixin):
    @property
    def lanka_data_file(self) -> JSONFile:
        return JSONFile(
            os.path.join(
                self.dir_data,
                "lanka_data.json",
            )
        )

    def _get_datumset_with_region_value_adapter(self, force=False):
        if self.lanka_data_file.exists() and not force:
            return

        d_list = self.data_list
        return RegionValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            time_str=self.time_str,
            measurement_class_name=self.measurement_class_name,
        )

    def _get_datumset_with_dim1_etc_adapter(self, force=False):
        if self.lanka_data_file.exists() and not force:
            return

        d_list = self.data_list
        return DimToTimeToValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            dim1_class_name=self.dim1_class_name,
            dim1_class_key=self.dim1_class_key,
            value_label=self.value_label,
        )

    def _get_datumset(self, force=False):
        if self.adapter_class_name == "RegionValueAdapter":
            return self._get_datumset_with_region_value_adapter(force=force)
        elif self.adapter_class_name == "DimToTimeToValueAdapter":
            return self._get_datumset_with_dim1_etc_adapter(force=force)

        raise ValueError(
            f"Unknown adapter_class_name: {self.adapter_class_name}"
        )

    def build_lanka_data(self, force=False):
        datumset = self._get_datumset(force=force)
        self.lanka_data_file.write(datumset.to_data())
        log.info(f"Wrote {self.lanka_data_file}")

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
