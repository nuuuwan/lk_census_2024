import os
import re

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

    def _expand_values_with_values(self, data):
        values = {}
        for k, v in data["values"].items():
            assert not k.startswith("p_")
            values[String(k).pascal] = v
        values = dict(sorted(values.items(), key=lambda item: -item[1]))
        data["values"] = values

        n = len(values.keys())

        total_value = sum(values.values())
        if total_value and n > 1:
            pct_values = {
                k: round(v / total_value, 4) for k, v in values.items()
            }
            data["total_value"] = total_value
            if self.total_description:
                data["total_description"] = self.total_description
            data["pct_values"] = pct_values
        return data

    def _expand_values_with_pct_values(self, data):
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
            k: int(round(v * total_value, 0)) for k, v in pct_values.items()
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

    def _expand_values(self, data):
        if self.is_all_not_pct_values:
            return self._expand_values_with_values(data)

        if self.is_all_pct_values:
            return self._expand_values_with_pct_values(data)

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
        if not data_list or len(data_list) == 0:
            log.warning("No data available. Skipping")
            return False
        first_data = data_list[0]

        if "values" not in first_data:
            log.warning("No values. Skipping")
            return False

        if not (self.is_all_not_pct_values or self.is_all_pct_values):
            log.warning(
                "Values mixed between percentage & non-percentage. Skipping"
            )
            return False

        return True

    def _get_meta(self, where_who_types, when_labels):
        return dict(
            source_url=self.source_url,
            source_description=self.source_description,
            what={self.what_label: Parse.str(self.table_name)},
            when=list(sorted(set(self.when_labels) | set(when_labels))),
            where_who_types=where_who_types,
        )

    def _get_where_who_types(self):

        if self.is_admin_region_dataset:
            return list(
                set([data["region_ent_type"] for data in self.data_list])
            )

        where_type = list(self.data_list[0].keys())[0]
        assert where_type not in ["region_id", "values", "total_value"]
        return [where_type]

    def _get_when_for_key(self, key):
        last5_charts = key[-5:]
        if last5_charts[0] == "_" and Parse.int(last5_charts[1:]) is not None:
            year = Parse.int(last5_charts[1:])
            assert 1800 < year < 2100
            return str(year)
        return "2024"

    def _split_by_when(self, data):
        idx = {}
        for k, v in data["values"].items():
            when_label = self._get_when_for_key(k)
            if when_label not in idx:
                idx[when_label] = dict(values={})
            idx[when_label]["values"][k] = v
        return idx

    def _get_non_values(self, data):
        return {k: v for k, v in data.items() if k != "values"}

    def _get_lanka_data(self):
        first_key = list(self.data_list[0].keys())[0]

        idx = {}
        when_labels = set()
        for data in self.data_list:
            data_non_values = self._get_non_values(data)
            for when_label, data_for_when in self._split_by_when(data).items():
                data_for_when = self._expand_values(data_for_when)
                if when_label not in idx:
                    idx[when_label] = {}
                idx[when_label][data[first_key]] = (
                    data_non_values | data_for_when
                )
                when_labels.add(when_label)

        where_who_types = self._get_where_who_types()
        _meta = self._get_meta(where_who_types, when_labels)
        lanka_data = dict(_meta=_meta)
        lanka_data[self.what_label] = idx
        return lanka_data

    def build_lanka_data(self, force=False):
        if not force and self.lanka_data_file.exists:
            return self.lanka_data_file.read()

        if not self.is_lanka_data_parser_implemented:
            return None

        if not self.is_lanka_data_metadata_complete:
            return None

        lanka_data = self._get_lanka_data()

        self.lanka_data_file.write(lanka_data)
        log.info(f"Wrote {self.lanka_data_file}")
        return lanka_data

    @property
    def lanka_data(self):
        if not self.lanka_data_file.exists:
            return {}
        return self.lanka_data_file.read()
