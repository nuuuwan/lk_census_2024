import os

from gig import Ent, EntType
from utils import JSONFile, Log, TSVFile

from lk_census.data_table.DataTableExtractDataCleanerMixin import \
    DataTableExtractDataCleanerMixin
from lk_census.data_table.DataTableExtractDataValidateMixin import \
    DataTableExtractDataValidateMixin

log = Log("DataTable")


class DataTableExtractDataMixin(
    DataTableExtractDataCleanerMixin, DataTableExtractDataValidateMixin
):

    @staticmethod
    def get_ent_type(region_name: str) -> EntType:
        if region_name == "Sri Lanka":
            return EntType.COUNTRY
        if "District" in region_name:
            return EntType.DISTRICT
        return EntType.DSD

    @staticmethod
    def __get_ent_data__(region_name, ent_type, current_parent_id):
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

        return region_id, region_name

    @staticmethod
    def extract_datum(field_list, row, current_parent_id):
        region_name_in_data = row[0]
        region_name = region_name_in_data

        region_name = {
            "Valikamam North": "Valikamam North (Tellipallai)",
            "Kalmunai North Sub": "Kalmunai Tamil Division",
        }.get(region_name, region_name)

        ent_type = DataTableExtractDataMixin.get_ent_type(region_name)
        if ent_type == EntType.DISTRICT:
            region_name = region_name.replace("District", "").strip()
            current_parent_id = "LK"
        region_id, region_name = DataTableExtractDataMixin.__get_ent_data__(
            region_name, ent_type, current_parent_id
        )

        if ent_type in [EntType.COUNTRY, EntType.DISTRICT]:
            assert region_id is not None, (
                "region_id should not be None,"
                + " for EntType.COUNTRY or EntType.DISTRICT"
            )
            current_parent_id = region_id

        d = dict(
            region_id=region_id,
            region_name=region_name,
            region_name_in_data=region_name_in_data,
            region_ent_type=ent_type.name,
            total=int(row[1]),
        )

        for i_field, field_name in enumerate(field_list):
            value = int(row[2 + i_field])
            d[field_name] = value

        return d, current_parent_id

    def __extract_data_d_list__(self):
        raw_table = self.extract_raw_table()
        raw_table = self.clean_raw_table(raw_table)

        d_list = []
        current_parent_id = None
        n_rows = len(raw_table)
        for i_row in range(n_rows):
            row = raw_table[i_row]
            d, current_parent_id = self.extract_datum(
                self.field_list, row, current_parent_id
            )
            d_list.append(d)
        d_list.sort(key=lambda x: x["region_id"])
        return d_list

    def __write_json__(self, d_list):
        json_file = JSONFile(os.path.join(self.dir_table, "data.json"))
        json_file.write(d_list)
        log.debug(f"Wrote {len(d_list)} data rows to {json_file}")

    def __write_tsv__(self, d_list):
        tsv_file = TSVFile(os.path.join(self.dir_table, "data.tsv"))
        tsv_file.write(d_list)
        log.debug(f"Wrote {len(d_list)} data rows to {tsv_file}")

    def extract_data(self):
        d_list = self.__extract_data_d_list__()
        self.validate(d_list)
        self.__write_json__(d_list)
        self.__write_tsv__(d_list)
        return d_list
