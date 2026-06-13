import os

import openpyxl

from gig_future import Ent, EntType
from lk_census.xlsx_data_table.XLSXDataTableValidateMixin import \
    XLSXDataTableValidateMixin
from utils_future import JSONFile, Log

log = Log("XLSXDataTable")

# Pre-load all entities keyed by ID for canonical name lookup
_ENT_BY_ID = {
    ent.id: ent
    for et in [
        EntType.COUNTRY,
        EntType.PROVINCE,
        EntType.DISTRICT,
        EntType.DSD,
        EntType.GND,
    ]
    for ent in Ent.list_from_type(et)
}


def _ent_name(region_id: str, fallback: str) -> str:
    ent = _ENT_BY_ID.get(region_id)
    return ent.name if ent else fallback


def parse_int(x):
    if not x:
        return 0
    x = str(x)
    if x in ["", "-"]:
        return 0
    return int(x)


class XLSXDataTableExtractDataMixin(XLSXDataTableValidateMixin):

    def _get_raw_rows(self):
        wb = openpyxl.load_workbook(self.xlsx_path, data_only=True)
        ws = list(wb.worksheets)[0]
        rows = []
        for row in ws.iter_rows(values_only=True):
            if not isinstance(row[0], (int, float)):
                continue
            rows.append(row)
        wb.close()
        return rows

    def _get_values(self, row):
        return {
            field: (parse_int(row[self.fields_col_start_index + i]))
            for i, field in enumerate(self.field_list)
        }

    def _get_source_total_value(self, row):
        return parse_int(row[self.total_col_index])

    def _get_gnd_info_with_province_info(self, row):
        assert self.has_province_info
        province_part, district_part, dsd_part, gnd_part = (
            row[0],
            row[2],
            row[4],
            row[6],
        )
        if not (province_part and district_part and dsd_part and gnd_part):
            return None
        gnd_id = (
            "LK-"
            + f"{province_part:01d}{district_part:01d}"
            + f"{dsd_part:02d}{gnd_part:03d}"
        )
        gnd_name = row[7]
        return gnd_id, gnd_name

    def _get_gnd_info_without_province_info(self, row):
        assert not self.has_province_info
        district_part, dsd_part, gnd_part = (
            row[0],
            row[2],
            row[4],
        )
        if not (district_part and dsd_part and gnd_part):
            return None
        district_part, dsd_part, gnd_part = map(
            int, [district_part, dsd_part, gnd_part]
        )
        gnd_id = (
            "LK-" + f"{district_part:02d}" + f"{dsd_part:02d}{gnd_part:03d}"
        )
        gnd_name = row[5]
        return gnd_id, gnd_name

    def _get_gnd_info(self, row):
        if self.has_province_info:
            return self._get_gnd_info_with_province_info(row)
        return self._get_gnd_info_without_province_info(row)

    def _extract_row_data(self, row):
        output = self._get_gnd_info(row)
        if not output:
            return None
        gnd_id, gnd_name = output
        values = self._get_values(row)
        total_value = sum(values.values())
        total_value_from_source = self._get_source_total_value(row)

        if total_value != total_value_from_source:
            log.debug(f"{row=}")
            log.debug(f"{values=}")
            diff = total_value - total_value_from_source
            log.debug(
                f"{total_value=}, {total_value_from_source=} -> {diff=}"
            )
            raise ValueError(
                f"Total value mismatch for {gnd_name} ({gnd_id})."
            )

        return dict(
            gnd_id=gnd_id,
            gnd_name_from_source=gnd_name,
            total_value_from_source=total_value_from_source,
            values=values,
            total_value=total_value,
        )

    @property
    def json_path(self):
        return os.path.join(self.dir_table, "data.json")

    def extract_data(self):
        json_file = JSONFile(self.json_path)
        if json_file.exists:
            log.debug(f"{json_file} exists")
            return json_file.read()

        raw_rows = self._get_raw_rows()
        d_list = [self._extract_row_data(row) for row in raw_rows]
        d_list = [d for d in d_list if d is not None]
        d_list.sort(key=lambda d: d["gnd_id"])
        os.makedirs(self.dir_table, exist_ok=True)

        json_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.json_path}")
        return d_list

    @property
    def data_list(self):
        return JSONFile(self.json_path).read()
