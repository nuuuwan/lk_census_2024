import os

from gig_future import Ent, EntType
from utils_future import JSONFile, Log
from utils_future.file import TSVFile

log = Log("XLSXDataTableAllDataMixin")


class XLSXDataTableAllDataMixin:
    @property
    def all_data_file(self):
        return JSONFile(os.path.join(self.dir_table, "data.json"))

    def build_all_data_json(self):
        if self.all_data_file.exists:
            log.debug(f"{self.all_data_file} exists.")
            return self.all_data_file.read()

        gnd_data_list = self.gnd_data_list

        non_admin_ent_types = [
            EntType.DSD,
            EntType.ED,
            EntType.PD,
            EntType.LG,
        ]
        admin_ent_types_and_id_len = [
            (EntType.COUNTRY, 2),
            (EntType.PROVINCE, 4),
            (EntType.DISTRICT, 5),
            (EntType.DSD, 7),
        ]

        gnd_idx = Ent.idx_from_type(EntType.GND)
        parent_to_data_lists = {}
        gnd_ids_not_in_lk_admin_regions = set()
        for d in gnd_data_list:
            gnd_id = d["region_id"]
            gnd = gnd_idx.get(gnd_id)

            for ent_type, id_len in admin_ent_types_and_id_len:
                parent_id = gnd_id[:id_len]
                if parent_id not in parent_to_data_lists:
                    parent_to_data_lists[parent_id] = []
                parent_to_data_lists[parent_id].append(d)

            if not gnd:
                gnd_ids_not_in_lk_admin_regions.add(gnd_id)
                log.warning(f"{gnd_id} not found in lk_admin_regions.")
                continue

            for ent_type in non_admin_ent_types:
                parent_id_key = f"{ent_type.name.lower()}_id"
                parent_id = gnd.d[parent_id_key]
                if parent_id not in parent_to_data_lists:
                    parent_to_data_lists[parent_id] = []
                parent_to_data_lists[parent_id].append(d)

        all_data_list = []
        for parent_id, data_lists in parent_to_data_lists.items():
            region_name = Ent.from_id(parent_id).name
            parent_data = dict(
                region_id=parent_id,
                region_name=region_name,
                region_ent_type=EntType.from_id(parent_id).name,
            ) | self.get_aggr_data(data_lists)
            all_data_list.append(parent_data)

        for d in gnd_data_list:
            gnd = gnd_idx.get(d["region_id"])
            gnd_data = dict(
                region_id=d["region_id"],
                region_name=gnd.name if gnd else d["region_name_from_source"],
                region_ent_type=EntType.GND.name,
                total_value=d["total_value"],
                values=d["values"],
                in_lk_admin_regions=gnd is not None,
            )
            all_data_list.append(gnd_data)

        all_data_list.sort(key=lambda d: -d["total_value"])

        os.makedirs(self.dir_table, exist_ok=True)
        self.all_data_file.write(all_data_list)
        log.info(f"Wrote {len(all_data_list)} rows to {self.all_data_file}")

        if gnd_ids_not_in_lk_admin_regions:
            log.warning(
                f"{len(gnd_ids_not_in_lk_admin_regions)}"
                + " gnd_ids not found in lk_admin_regions. "
            )

        gnd_ids_in_data_table = set(d["region_id"] for d in gnd_data_list)
        gnd_ids_not_in_data_table = (
            set(gnd_idx.keys()) - gnd_ids_in_data_table
        )
        if gnd_ids_not_in_data_table:
            log.warning(
                f"{len(gnd_ids_not_in_data_table)}"
                + " gnd_ids not found in data table."
            )

    @property
    def data_list(self):
        return self.all_data_file.read()

    @property
    def tsv_file(self):
        return TSVFile(os.path.join(self.dir_table, "data.tsv"))

    def build_all_data_tsv(self):
        tsv_file = self.tsv_file
        if tsv_file.exists:
            log.debug(f"{tsv_file} exists.")
            return

        def map_tsv(d):
            return (
                dict(
                    region_id=d["region_id"],
                    region_name=d["region_name"],
                    region_ent_type=d["region_ent_type"],
                    total_value=d["total_value"],
                )
                | d["values"]
            )

        d_list_for_tsv = [map_tsv(d) for d in self.data_list]
        tsv_file.write(d_list_for_tsv)
        log.info(f"Wrote {len(d_list_for_tsv)} rows to {tsv_file}")

    def build_all_data(self):
        self.build_all_data_json()
        self.build_all_data_tsv()
