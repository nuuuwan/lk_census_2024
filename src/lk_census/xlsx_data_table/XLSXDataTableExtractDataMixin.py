import os
from collections import defaultdict

import openpyxl

from gig_future import Ent, EntType
from lk_census.xlsx_data_table.XLSXDataTableValidateMixin import \
    XLSXDataTableValidateMixin
from utils_future import JSONFile, Log, TSVFile

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


class XLSXDataTableExtractDataMixin(XLSXDataTableValidateMixin):

    @property
    def xlsx_path(self):
        return os.path.join("original_docs", f"{self.doc_name}.xlsx")

    def __extract_raw_rows__(self):
        wb = openpyxl.load_workbook(self.xlsx_path, data_only=True)
        ws = list(wb.worksheets)[0]
        rows = []
        for row in ws.iter_rows(values_only=True):
            if not isinstance(row[0], (int, float)):
                continue
            rows.append(row)
        wb.close()
        return rows

    def __field_values__(self, row):
        return {
            field: (
                int(row[self.column_offset + i])
                if row[self.column_offset + i] is not None
                else 0
            )
            for i, field in enumerate(self.field_list)
        }

    def _get_sums_by_id_and_raw_names_(self, raw_rows):
        sums = defaultdict(lambda: defaultdict(int))
        raw_names = {}

        for row in raw_rows:
            province_id = int(row[0])
            province_name = str(row[1])
            district_id = int(row[2])
            district_name = str(row[3])
            dsd_id = int(row[4])
            dsd_name = str(row[5])
            gnd_id = int(row[6])
            gnd_name = str(row[7])

            ids = {
                "COUNTRY": "LK",
                "PROVINCE": f"LK-{province_id}",
                "DISTRICT": f"LK-{district_id:02d}",
                "DSD": f"LK-{district_id:02d}{dsd_id:02d}",
                "GND": f"LK-{district_id:02d}{dsd_id:02d}{gnd_id:03d}",
            }
            fallbacks = {
                "COUNTRY": "Sri Lanka",
                "PROVINCE": province_name,
                "DISTRICT": district_name,
                "DSD": dsd_name,
                "GND": gnd_name,
            }

            field_vals = self.__field_values__(row)
            for ent_type, rid in ids.items():
                for field, val in field_vals.items():
                    sums[rid][field] += val
                raw_names.setdefault(rid, (ent_type, fallbacks[ent_type]))

        return sums, raw_names

    def _build_d_list_for_existing_types_(self, sums, raw_names):
        d_list = []
        for region_id, field_sums in sums.items():
            ent_type, fallback_name = raw_names[region_id]
            region_name = _ent_name(region_id, fallback_name)
            d = dict(
                region_id=region_id,
                region_name=region_name,
                region_name_in_data=fallback_name,
                region_ent_type=ent_type,
            )
            d.update(field_sums)
            d_list.append(d)

        d_list.sort(key=lambda x: x["region_id"])
        return d_list

    def _build_all_levels_(self, raw_rows):
        sums, raw_names = self._get_sums_by_id_and_raw_names_(raw_rows)
        return self._build_d_list_for_existing_types_(sums, raw_names)

    @property
    def json_path(self):
        return os.path.join(self.dir_table, "data.json")

    @property
    def tsv_path(self):
        return os.path.join(self.dir_table, "data.tsv")

    def extract_data(self):
        log.debug("-" * 40)
        log.info("Extracting data for " + self.name_safe)
        raw_rows = self.__extract_raw_rows__()
        d_list = self._build_all_levels_(raw_rows)
        self.validate(d_list)
        os.makedirs(self.dir_table, exist_ok=True)
        JSONFile(self.json_path).write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.json_path}")
        TSVFile(self.tsv_path).write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.tsv_path}")
        return d_list

    @property
    def data_list(self):
        return JSONFile(self.json_path).read()
