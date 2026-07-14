import os

from lk_census.final_report.table.lanka_data.FinalReportLankaMetaDataMixin import (
    FinalReportLankaMetaDataMixin,
)
from utils_future import JSONFile, Log, Parse, String

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

    def _expand_values(self, data):
        if self.is_all_not_pct_values:
            values = {}
            for k, v in data["values"].items():
                values[String(k).pascal] = v
            values = dict(sorted(values.items(), key=lambda item: -item[1]))
            data["values"] = values

            total_value = sum(values.values())
            pct_values = {
                k: round(v / total_value, 4) for k, v in values.items()
            }
            data["total_value"] = total_value
            if self.total_description:
                data["total_description"] = self.total_description
            data["pct_values"] = pct_values
            return data

        if self.is_all_pct_values:
            pct_values = {}
            for k, v in data["values"].items():
                assert k.startswith("p_")
                k = k[2:]
                pct_values[String(k).pascal] = v
            pct_values = dict(
                sorted(pct_values.items(), key=lambda item: -item[1])
            )
            total_value = data["total_value"]

            values = {
                k: int(round(v * total_value, 0))
                for k, v in pct_values.items()
            }
            if self.is_summable:
                _rounding_error = total_value - sum(values.values())
                if _rounding_error != 0:
                    values["_rounding_error"] = _rounding_error

            data["values"] = values
            data["total_value"] = total_value
            if self.total_description:
                data["total_description"] = self.total_description
            data["pct_values"] = pct_values

            return data

        raise ValueError(
            "Data must be either all pct values or all non-pct values."
        )

    @property
    def is_admin_region_dataset(self):
        data_list = self.data_list
        first_data = data_list[0]

        if "region_id" not in first_data:
            log.warning("No region_id. Skipping")
            return False
        return True

    @property
    def is_all_pct_values(self):
        data_list = self.data_list
        first_data = data_list[0]
        for k in first_data["values"].keys():
            if not k.startswith("p_"):
                return False
        return True

    @property
    def is_all_not_pct_values(self):
        data_list = self.data_list
        first_data = data_list[0]
        for k in first_data["values"].keys():
            if k.startswith("p_"):
                return False
        return True

    @property
    def is_lanka_data_parser_implemented(self):
        data_list = self.data_list
        first_data = data_list[0]

        if "total_value" not in first_data:
            log.warning("No total_value. Skipping")
            return False

        if "values" not in first_data:
            log.warning("No values. Skipping")
            return False

        if not (self.is_all_not_pct_values or self.is_all_pct_values):
            log.warning(
                "Values mixed between percentage & non-percentage. Skipping"
            )
            return False

        return True

    def get_lanka_data_for_regions(self):

        where_types = list(
            set([data["region_ent_type"] for data in self.data_list])
        )
        _meta = dict(
            source_url=self.source_url,
            source_description=self.source_description,
            what={self.what_label: Parse.str(self.table_name)},
            when=self.when_label,
            where_types=where_types,
        )

        idx = {}
        for data in self.data_list:
            data = self._expand_values(data)

            idx[data["region_id"]] = data

        lanka_data = dict(_meta=_meta)
        lanka_data[self.what_label] = {self.when_label: idx}
        return lanka_data

    def build_lanka_data(self, force=False):
        if not force and self.lanka_data_file.exists:
            return self.lanka_data_file.read()

        if not self.is_lanka_data_parser_implemented:
            return None

        if not self.is_lanka_data_metadata_complete:
            return None

        if self.is_admin_region_dataset:
            lanka_data = self.get_lanka_data_for_regions()
        else:
            return None

        self.lanka_data_file.write(lanka_data)
        log.info(f"Wrote {self.lanka_data_file}")
        return lanka_data

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists:
            return {}
        return self.lanka_data_file.read()
