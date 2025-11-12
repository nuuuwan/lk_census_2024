import os

from gig import Ent, EntType
from utils import JSONFile, Log, TSVFile

from lk_census.data_table.DataTableExtractDataValidateMixin import (
    DataTableExtractDataValidateMixin,
)

log = Log("DataTable")


class DataTableExtractDataMixin(DataTableExtractDataValidateMixin):

    @staticmethod
    def get_ent_type(region_name: str) -> EntType:
        if region_name == "Sri Lanka":
            return EntType.COUNTRY
        if "District" in region_name:
            return EntType.DISTRICT
        return EntType.DSD

    def clean_raw_table(self, raw_table):
        n_rows = len(raw_table)

        # check 0: shift shifted region names (in-place)
        for i_row in range(len(raw_table) - 1):
            row = raw_table[i_row]
            if len(row) != 2 + self.n_fields:
                continue
            if raw_table[i_row][0] == "":
                if raw_table[i_row + 1][0] != "":
                    log.debug(f"<- {raw_table[i_row + 1][0]}")
                    raw_table[i_row][0] = raw_table[i_row + 1][0]
                    if len(raw_table[i_row + 1]) == 2 + self.n_fields:
                        raw_table[i_row + 1][0] = ""

        cleaned_raw_table = []
        for i_row in range(n_rows):
            row = raw_table[i_row]
            # check 1: split first cell if merged
            if len(row) == 1 + self.n_fields:
                first_cell = row[0]
                tokens = str(first_cell).split(" ")
                if len(tokens) < 2:
                    continue
                value = self.parse_int(tokens[0])
                if not isinstance(value, int):
                    continue
                region_name = " ".join(tokens[1:])
                row = [region_name, value] + row[1:].copy()

            # check 2: correct number of columns
            if len(row) != 2 + self.n_fields:
                continue
            cleaned_raw_table.append(row)

        return cleaned_raw_table

    def extract_data(self):
        raw_table = self.extract_raw_table()
        raw_table = self.clean_raw_table(raw_table)

        d_list = []
        current_parent_id = None

        n_rows = len(raw_table)
        for i_row in range(n_rows):
            row = raw_table[i_row]

            region_name_in_data = row[0]
            region_name = region_name_in_data

            region_name = {
                "Valikamam North": "Valikamam North (Tellipallai)",
                "Kalmunai North Sub": "Kalmunai Tamil Division",
            }.get(region_name, region_name)

            ent_type = self.get_ent_type(region_name)
            if ent_type == EntType.DISTRICT:
                region_name = region_name.replace("District", "").strip()
                current_parent_id = "LK"

            candidate_ents = Ent.list_from_name_fuzzy(
                name_fuzzy=region_name,
                filter_ent_type=ent_type,
                filter_parent_id=current_parent_id,
                min_fuzz_ratio=70,
            )

            if len(candidate_ents) == 0:
                log.warning(
                    "Could not find Ent for"
                    + f" {region_name}/{current_parent_id}."
                )
                region_id = f"{current_parent_id}XX"
            else:
                region_ent = candidate_ents[0]
                region_id = region_ent.id
                region_name = region_ent.name

            if ent_type in [EntType.COUNTRY, EntType.DISTRICT]:
                current_parent_id = region_ent.id

            d = dict(
                region_id=region_id,
                region_name=region_name,
                region_name_in_data=region_name_in_data,
                region_ent_type=ent_type.name,
                total=int(row[1]),
            )

            for i_field, field_name in enumerate(self.field_list):
                value = int(row[2 + i_field])
                d[field_name] = value

            d_list.append(d)

        d_list.sort(key=lambda x: x["region_id"])

        self.validate(d_list)
        json_file = JSONFile(os.path.join(self.dir_table, "data.json"))
        json_file.write(d_list)
        log.debug(f"Wrote {len(d_list)} data rows to {json_file}")

        tsv_file = TSVFile(os.path.join(self.dir_table, "data.tsv"))
        tsv_file.write(d_list)
        log.debug(f"Wrote {len(d_list)} data rows to {tsv_file}")

        return d_list
