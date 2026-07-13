from gig_future import Ent, EntType


class FinalReportTableDataAggregateMixin:
    def _aggregate(self, parent_id, d_list_for_parent):
        parent = Ent.from_id(parent_id)
        parent_values = {}
        for d in d_list_for_parent:
            for k, v in d["values"].items():
                parent_values[k] = parent_values.get(k, 0) + v
        d_parent = dict(
            region_id=parent_id,
            region_name=parent.name,
            region_ent_type=EntType.from_id(parent_id).name,
            values=parent_values,
        )
        if self.is_summable:
            d_parent["total_value"] = sum(parent_values.values())
        return d_parent

    @staticmethod
    def _get_parent_id(ent_type, child_region):
        if ent_type == EntType.COUNTRY:
            return "LK"
        parent_id_key = ent_type.name.lower() + "_id"
        return child_region.d[parent_id_key]

    def _map_to_parents(self, d_list):
        parent_types = [EntType.COUNTRY, EntType.PROVINCE, EntType.ED]
        parent_id_to_d_list = {}
        for ent_type in parent_types:
            for d in d_list:
                child_region = Ent.from_id(d["region_id"])
                parent_id = self._get_parent_id(ent_type, child_region)
                if parent_id not in parent_id_to_d_list:
                    parent_id_to_d_list[parent_id] = []
                parent_id_to_d_list[parent_id].append(d)
        return parent_id_to_d_list

    def _expand_data_list(self, d_list):
        parent_map = self._map_to_parents(d_list)
        for parent_id, d_list_for_parent in parent_map.items():
            d_list.append(self._aggregate(parent_id, d_list_for_parent))
        return d_list
