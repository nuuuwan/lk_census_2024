from gig_future import Ent, EntType
from utils_future import Log, Parse

log = Log("FinalReportTableDataOtherValuesMixin")


class FinalReportTableDataOtherValuesMixin:

    def _is_key_float(self, cell_key):
        for keyword in ["avg", "rate", "ratio", "index", "median"]:
            if keyword in cell_key:
                return True
        return False

    def _is_key_ignored(self, cell_key):
        return cell_key.startswith("_")

    def _is_key_str(self, cell_key):
        for keyword in ["name"]:
            if keyword in cell_key:
                return True
        return False

    def _is_key_boolean(self, cell_key):
        return cell_key.startswith("is_") or cell_key.startswith("has_")

    def _is_key_int_in_thousands(self, cell_key):
        if cell_key.endswith("_population_k"):
            return True
        return False

    # flake8: noqa: E501
    def _build_value(self, cell_key, cell_value):
        if self._is_key_str(cell_key):
            return cell_value

        if self._is_key_boolean(cell_key):
            return Parse.boolean(cell_value)

        if cell_key.startswith("p_"):
            return Parse.percent(cell_value)

        if self._is_key_float(cell_key):
            return Parse.float(cell_value)

        if self._is_key_int_in_thousands(cell_key):
            f = Parse.float(cell_value) or 0
            return int(f * 1000)

        return Parse.int(cell_value)

    def _build_sums(self, d):
        values = d["values"]
        total_value = sum(values.values())
        if total_value <= 0:
            raise ValueError(f"Total value is non-positive: {total_value}")
        d["total_value"] = total_value
        return d

    def _build_other_keys(self, other_cells):
        values = {}
        for other_key, other_value in zip(self.other_keys, other_cells):
            if self._is_key_ignored(other_key):
                continue
            value = self._build_value(other_key, other_value)
            if value is None:
                log.warning(f'Null value for "{other_key}": "{other_value}"')
                return None
            values[other_key] = value

        if "total_value" in values:
            total_value = values["total_value"]
            del values["total_value"]
            error = total_value - sum(values.values())
            values[self.error_key] = error

        d = dict(values=values)
        if self.total_description:
            d["total_description"] = self.total_description

        if self.is_summable:
            self._build_sums(d)
        return d
