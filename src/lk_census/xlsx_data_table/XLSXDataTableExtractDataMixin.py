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


def parse_int(x):
    x = str(x)
    if x in ["", "-"]:
        return 0
    return int(x)


class XLSXDataTableExtractDataMixin(XLSXDataTableValidateMixin):

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
                parse_int(row[self.column_offset + i])
                if row[self.column_offset + i] is not None
                else 0
            )
            for i, field in enumerate(self.field_list)
        }

    def _get_ids_and_fallbacks_no_province(self, row):
        district_id, district_name, dsd_id, dsd_name, gnd_id, gnd_name = row[
            :6
        ]

        if gnd_id is None:
            return None

        district_id, dsd_id, gnd_id = map(
            parse_int, (district_id, dsd_id, gnd_id)
        )

        ids = {
            "COUNTRY": "LK",
            "DISTRICT": f"LK-{district_id:02d}",
            "DSD": f"LK-{district_id:02d}{dsd_id:02d}",
            "GND": f"LK-{district_id:02d}{dsd_id:02d}{gnd_id:03d}",
        }
        fallbacks = {
            "COUNTRY": "Sri Lanka",
            "DISTRICT": district_name,
            "DSD": dsd_name,
            "GND": gnd_name,
        }
        return ids, fallbacks

    def _get_ids_and_fallbacks_with_province(self, row):
        (
            province_id,
            province_name,
            district_id,
            district_name,
            dsd_id,
            dsd_name,
            gnd_id,
            gnd_name,
        ) = row[:8]

        province_id, district_id, dsd_id, gnd_id = map(
            parse_int, (province_id, district_id, dsd_id, gnd_id)
        )

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
        return ids, fallbacks

    def _get_ids_and_fallbacks(self, row):
        if self.has_province_info:
            return self._get_ids_and_fallbacks_with_province(row)
        return self._get_ids_and_fallbacks_no_province(row)

    def _get_sums_by_id_and_raw_names_(self, raw_rows):
        sums = defaultdict(lambda: defaultdict(int))
        raw_names = {}

        for row in raw_rows:
            output = self._get_ids_and_fallbacks(row)
            if output is None:
                continue
            ids, fallbacks = output

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

    @staticmethod
    def _build_d_list_for_remaining_types_(
        d_list, field_list, ent_type_and_child_ent_type
    ):
        new_d_list = []
        for ent_type, child_ent_type in ent_type_and_child_ent_type:
            d_list_for_ent = XLSXDataTableExtractDataMixin._build_d_list_for_remaining_type_(  # noqa: E501
                d_list, ent_type, child_ent_type, field_list
            )
            new_d_list.extend(d_list_for_ent)
        return new_d_list

    @staticmethod
    def _build_d_list_for_remaining_type_(
        d_list, ent_type, child_ent_type, field_list
    ):
        ent_idx = Ent.idx_from_type(ent_type)
        child_ent_idx = Ent.idx_from_type(child_ent_type)
        ent_id_key = f"{ent_type.name.lower()}_id"
        child_d_list = [
            d
            for d in d_list
            if d["region_ent_type"].lower() == child_ent_type.name
        ]
        assert len(child_d_list) > 0, "No child entities found to build from"

        id_to_d_list = {}
        for d in child_d_list:
            child_id = d["region_id"]
            child_ent = child_ent_idx.get(child_id)
            if not child_ent:
                log.warning(f"Child ent {child_id} not found.")
                continue
            ent_id = child_ent.d[ent_id_key]

            if ent_id not in id_to_d_list:
                id_to_d_list[ent_id] = []
            id_to_d_list[ent_id].append(d)

        new_d_list = []
        if "total" in d_list[0]:
            if "total" not in field_list:
                field_list = ["total"] + field_list
        for id, d_list_for_ent in id_to_d_list.items():
            ent = ent_idx[id]
            ent_d = {
                "region_id": ent.id,
                "region_name": ent.name,
                "region_name_in_data": None,
                "region_ent_type": ent_type.name.upper(),
            }
            for d in d_list_for_ent:
                for field in field_list:
                    ent_d[field] = ent_d.get(field, 0) + d.get(field, 0)
            new_d_list.append(ent_d)

        return new_d_list

    def _build_all_levels_(self, raw_rows):
        sums, raw_names = self._get_sums_by_id_and_raw_names_(raw_rows)
        d_list = self._build_d_list_for_existing_types_(sums, raw_names)
        new_d_list = self._build_d_list_for_remaining_types_(
            d_list,
            self.field_list,
            [
                (EntType.ED, EntType.DISTRICT),
                (EntType.PD, EntType.GND),
                (EntType.LG, EntType.GND),
            ],
        )
        d_list.extend(new_d_list)
        d_list.sort(key=lambda x: x["region_id"])
        return d_list

    @property
    def json_path(self):
        return os.path.join(self.dir_table, "data.json")

    @property
    def tsv_path(self):
        return os.path.join(self.dir_table, "data.tsv")

    def extract_data(self):
        json_file = JSONFile(self.json_path)
        if json_file.exists:
            log.debug(f"{json_file} exists")
            return json_file.read()

        raw_rows = self.__extract_raw_rows__()
        d_list = self._build_all_levels_(raw_rows)
        self.validate(d_list)
        os.makedirs(self.dir_table, exist_ok=True)

        json_file.write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.json_path}")
        TSVFile(self.tsv_path).write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.tsv_path}")
        return d_list

    @property
    def data_list(self):
        return JSONFile(self.json_path).read()
