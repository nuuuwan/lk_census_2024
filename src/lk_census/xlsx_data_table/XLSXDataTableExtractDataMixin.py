import os

import openpyxl
from gig import Ent, EntType
from utils import JSONFile, Log, TSVFile

log = Log("XLSXDataTable")

# Pre-load all GND entities keyed by ID for fast lookup
_GND_BY_ID = {ent.id: ent for ent in Ent.list_from_type(EntType.GND)}


def _build_region_id(district_id: int, dsd_id: int, gnd_id: int) -> str:
    return f"LK-{district_id:02d}{dsd_id:02d}{gnd_id:03d}"


class XLSXDataTableExtractDataMixin:

    @property
    def xlsx_path(self):
        return os.path.join("original_docs", f"{self.doc_name}.xlsx")

    def __extract_raw_rows__(self):
        wb = openpyxl.load_workbook(self.xlsx_path, data_only=True)
        ws = list(wb.worksheets)[0]
        rows = []
        for row in ws.iter_rows(values_only=True):
            # Data rows have an integer province code in column 0
            if not isinstance(row[0], (int, float)):
                continue
            rows.append(row)
        wb.close()
        return rows

    def __build_d__(self, row):
        district_id = int(row[2])
        dsd_id = int(row[4])
        gnd_id = int(row[6])
        region_name_in_data = str(row[7])

        region_id = _build_region_id(district_id, dsd_id, gnd_id)
        gnd_ent = _GND_BY_ID.get(region_id)
        region_name = gnd_ent.name if gnd_ent else region_name_in_data

        d = dict(
            region_id=region_id,
            region_name=region_name,
            region_name_in_data=region_name_in_data,
            region_ent_type=EntType.GND.name,
        )
        for i, field_name in enumerate(self.field_list):
            val = row[self.column_offset + i]
            d[field_name] = int(val) if val is not None else 0
        return d

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
        d_list = [self.__build_d__(row) for row in raw_rows]
        d_list.sort(key=lambda x: x["region_id"])
        os.makedirs(self.dir_table, exist_ok=True)
        JSONFile(self.json_path).write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.json_path}")
        TSVFile(self.tsv_path).write(d_list)
        log.info(f"Wrote {len(d_list)} rows to {self.tsv_path}")
        return d_list

    @property
    def data_list(self):
        return JSONFile(self.json_path).read()
