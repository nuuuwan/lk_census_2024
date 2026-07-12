import os

from gig_future import Ent, EntType
from utils_future import JSONFile, Log, Parse

log = Log("FinalReportTableDataMixin")


class FinalReportTableDataMixin:
    @property
    def data_file(self):
        return JSONFile(os.path.join(self.dir_data, "data.json"))

    @property
    def fields_file(self):
        return JSONFile(os.path.join(self.dir_data, "fields.json"))

    @property
    def fields(self):
        if not self.fields_file.exists:
            return None
        return self.fields_file.read()

    @staticmethod
    def _get_region(region_name):
        regions = Ent.list_from_name_fuzzy(
            name_fuzzy=region_name,
            filter_ent_type=EntType.DISTRICT,
        )
        if len(regions) != 1:
            raise ValueError(
                f"Expected exactly one region for '{region_name}',"
                + f" found {str(regions)}"
            )
        return regions[0]

    @staticmethod
    def _build_data_item(raw_data, n_fields, fields):
        if "total" in raw_data[0].lower():
            return None
        if len(raw_data) != n_fields:
            return None

        d = {}
        for i_field, field in enumerate(fields):
            value = raw_data[i_field]
            if field == "District":
                region = FinalReportTableDataMixin._get_region(value)
                d = dict(
                    region_id=region.id,
                    region_name=region.name,
                    region_ent_type=EntType.DISTRICT.name,
                )
            else:
                value = Parse.int(value)
                key = field.replace("-", " ").replace(" ", "_").lower()
                d[key] = value
        return d

    def build_data(self):
        raw_data_list = self.raw_data_list
        if not raw_data_list:
            return
        fields = self.fields
        if not fields:
            return

        n_fields = len(fields)
        d_list = []
        for raw_data in raw_data_list:
            d = self._build_data_item(raw_data, n_fields, fields)
            if d:
                d_list.append(d)
        self.data_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.data_file}")
