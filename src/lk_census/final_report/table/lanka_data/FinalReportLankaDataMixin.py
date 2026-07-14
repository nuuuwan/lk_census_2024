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
        values = {}
        for k, v in data["values"].items():
            values[String(k).pascal] = v
        values = dict(sorted(values.items(), key=lambda item: -item[1]))
        data["values"] = values

        total_value = sum(values.values())
        pct_values = {k: round(v / total_value, 4) for k, v in values.items()}
        data["total_value"] = total_value
        data["pct_values"] = pct_values

        return data

    @property
    def is_lanka_data_parser_implemented(self):
        data_list = self.data_list
        first_data = data_list[0]

        if "region_id" not in first_data:
            log.warning("No region_id. Skipping")
            return False

        if "total_value" not in first_data:
            log.warning("No total_value. Skipping")
            return False

        if "values" not in first_data:
            log.warning("No values. Skipping")
            return False

        for k in first_data["values"].keys():
            if k.startswith("p_"):
                log.warning(f"Found key starting with 'p_': {k}")
                return False
        return True

    def build_lanka_data(self, force=False):
        if not force and self.lanka_data_file.exists:
            return self.lanka_data_file.read()

        if not self.is_lanka_data_parser_implemented:
            return None

        if not self.is_lanka_data_metadata_complete:
            return None

        _meta = dict(
            source_url=self.source_url,
            source_description=self.source_description,
            what={self.what_label: Parse.str(self.table_name)},
        )

        idx = {}
        for data in self.data_list:
            data = self._expand_values(data)

            idx[data["region_id"]] = data

        lanka_data = dict(_meta=_meta)
        lanka_data[self.what_label] = {self.when_label: idx}
        self.lanka_data_file.write(lanka_data)
        log.info(f"Wrote {self.lanka_data_file}")
        return lanka_data
