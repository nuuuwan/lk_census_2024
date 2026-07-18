import os

from ds import (
    DimToTimeToValueAdapter,
    DimToValueAdapter,
    GenericValueAdapter,
    RegionValueAdapter,
)
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

    def _get_datumset_with_region_value_adapter(self):

        d_list = self.data_list
        return RegionValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            time_str=self.time_str,
            measurement_class_name=self.measurement_class_name,
            value_label=self.value_label,
            value_class_name=self.value_class_name,
        )

    def _get_datumset_with_dim1_etc_adapter(self):

        d_list = self.data_list
        return DimToTimeToValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            dim_class_name=self.dim_class_name,
            dim_class_key=self.dim_class_key,
            value_label=self.value_label,
        )

    def _get_datumset_with_dim_to_value_adapter(self):
        d_list = self.data_list
        return DimToValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            dim_class_name=self.dim_class_name,
            dim_class_key=self.dim_class_key,
            value_class_name=self.value_class_name,
            value_label=self.value_label,
        )

    def _get_datumset_with_generic_value_adapter(self):

        d_list = self.data_list
        return GenericValueAdapter.build_datumset(
            d_list=d_list,
            entity_class_name=self.entity_class_name,
            dim_idx=self.dim_idx,
            cell_idx=self.cell_idx,
        )

    def _get_get_datumset_helper(self):
        return {
            "RegionValueAdapter": self._get_datumset_with_region_value_adapter,
            "DimToTimeToValueAdapter": self._get_datumset_with_dim1_etc_adapter,
            "DimToValueAdapter": self._get_datumset_with_dim_to_value_adapter,
            "GenericValueAdapter": self._get_datumset_with_generic_value_adapter,
        }.get(self.adapter_class_name)

    def _get_datumset(self):
        _helper = self._get_get_datumset_helper()
        if _helper is not None:
            return _helper()
        raise ValueError(
            f"Unknown adapter_class_name: {self.adapter_class_name}"
        )

    def build_lanka_data(self, force=False):
        datumset = self._get_datumset()
        self.lanka_data_file.write(datumset.to_data())
        log.info(f"Wrote {self.lanka_data_file}")

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists():
            return {}
        return self.lanka_data_file.read()
