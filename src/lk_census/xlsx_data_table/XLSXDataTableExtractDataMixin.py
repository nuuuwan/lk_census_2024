import os

import openpyxl

from utils_future import JSONFile, Log

log = Log("XLSXDataTable")


def parse_int(x):
    if not x:
        return 0
    x = str(x)
    if x in ["", "-"]:
        return 0
    return int(x)


class XLSXDataTableExtractDataMixin:

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
        district_part, dsd_part, gnd_part = (
            row[2],
            row[4],
            row[6],
        )
        if not (district_part and dsd_part and gnd_part):
            return None
        gnd_id = (
            "LK-" + f"{district_part:02d}" + f"{dsd_part:02d}{gnd_part:03d}"
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
        if len(gnd_id) != 10:
            raise ValueError(f"Invalid GND ID format: {gnd_id}")
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

    def get_aggr_data(self, data_list):
        values = {}
        for d in data_list:
            d_values = d["values"]
            for k, v in d_values.items():
                values[k] = values.get(k, 0) + v

        total_value_from_source = sum(
            d["total_value_from_source"] for d in data_list
        )
        total_value = sum(d["total_value"] for d in data_list)

        return dict(
            total_value_from_source=total_value_from_source,
            values=values,
            total_value=total_value,
        )

    def extract_data(self):
        json_file = JSONFile(self.json_path)
        if json_file.exists:
            log.debug(f"{json_file} exists")
            return json_file.read()

        raw_rows = self._get_raw_rows()
        d_list = [self._extract_row_data(row) for row in raw_rows]
        d_list = [d for d in d_list if d is not None]
        d_list.sort(key=lambda d: d["gnd_id"])
        n = len(d_list)
        expected_row_count = self.expected_row_count
        if n != expected_row_count:
            log.debug(f"{n=}, {expected_row_count=}")
            raise ValueError(
                f"Expected rows mismatch for {self.data_table_id}. "
            )

        aggr_data = self.get_aggr_data(d_list)
        expected_total_value = self.expected_total_value
        actual_total_value = aggr_data["total_value"]
        if actual_total_value != expected_total_value:
            diff = actual_total_value - expected_total_value
            log.debug(
                f"{actual_total_value=}, {expected_total_value=} -> {diff=}"
            )
            raise ValueError(
                f"Expected total mismatch for {self.data_table_id}. "
            )

        os.makedirs(self.dir_table, exist_ok=True)
        json_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.json_path}")
        return d_list

    @property
    def data_list(self):
        return JSONFile(self.json_path).read()
