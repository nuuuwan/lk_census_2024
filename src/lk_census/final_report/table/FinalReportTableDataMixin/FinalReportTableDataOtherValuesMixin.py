from gig_future import Ent, EntType
from utils_future import Log, Parse

log = Log("FinalReportTableDataOtherValuesMixin")


class FinalReportTableDataOtherValuesMixin:

    def _is_key_float(self, cell_key):
        for keyword in ["avg", "rate", "ratio"]:
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

    # flake8: noqa: E501
    def _build_value(self, cell_key, cell_value):
        if cell_key.startswith("p_"):
            return Parse.percent(cell_value)

        if self._is_key_float(cell_key):
            return Parse.float(cell_value)

        if self._is_key_str(cell_key):
            return cell_value

        if self._is_key_boolean(cell_key):
            return Parse.boolean(cell_value)

        return Parse.int(cell_value)

    def _build_other_keys(self, other_cells):
        d = {}
        for other_key, other_value in zip(self.other_keys, other_cells):
            if self._is_key_ignored(other_key):
                continue
            value = self._build_value(other_key, other_value)
            if value is None:
                log.warning(f'Null value for "{other_key}": "{other_value}"')
                return None
            d[other_key] = value
        return d
