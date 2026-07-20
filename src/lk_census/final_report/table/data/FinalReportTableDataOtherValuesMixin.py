from utils_future import Log, Parse

log = Log("FinalReportTableDataOtherValuesMixin")


class FinalReportTableDataOtherValuesMixin:

    def _is_key_float(self, cell_key):
        for keyword in [
            "avg",
            "rate",
            "ratio",
            "index",
            "median",
            "mean",
            "deviation",
        ]:
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
        if "_population_k" in cell_key:
            return True
        return False

    def _is_key_rate_per_k(self, cell_key):
        if cell_key.endswith("_rate_per_k"):
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

        if self._is_key_rate_per_k(cell_key):
            return Parse.float(cell_value)

        if self._is_key_float(cell_key):
            return Parse.float(cell_value)

        if self._is_key_int_in_thousands(cell_key):
            f = Parse.float(cell_value) or 0
            return int(f * 1000)

        return Parse.int(cell_value) or Parse.float(cell_value)

    def _build_sums(self, d):
        if self.has_non_p_values(d) and not self.has_p_values(d):
            values = d.get("values", {})
            non_total_values = [
                v for k, v in values.items() if k != "total_value"
            ]
            total_value = sum(non_total_values)
            if self.has_total_value(d):
                log.debug(
                    "[_build_sums] Case 1.1: non_p values and total_value"
                )
                error = values["total_value"] - total_value
                del d["values"]["total_value"]
                error_key = self.error_key or "_error"
                d["values"][error_key] = error
                d["total_value"] = total_value
            else:
                log.debug(
                    "[_build_sums] Case 1.2: non_p values and, NO total_value"
                )
                d["total_value"] = total_value

        elif self.has_p_values(d) and not self.has_non_p_values(d):

            values = d.get("values", {})
            non_total_values = [
                v for k, v in values.items() if k != "total_value"
            ]
            if self.has_total_value(d):
                log.debug("[_build_sums] Case 2: p values and total_value")
                total_value = d["values"]["total_value"]
                new_values = {
                    k[2:]: int(round(v * total_value, 0))
                    for k, v in values.items()
                    if k.startswith("p_")
                }
                d["values"] = new_values
                d["total_value"] = total_value
            else:
                log.debug(
                    "[_build_sums] Case 2.2: p values and, NO total_value"
                )
        else:
            log.debug("[_build_sums] Case 3: mixed p and non_p values")

    def has_non_p_values(self, d):
        values = d.get("values", {})
        for key in values.keys():
            if not key.startswith("p_") and key != "total_value":
                return True
        return False

    def has_p_values(self, d):
        values = d.get("values", {})
        for key in values.keys():
            if key.startswith("p_"):
                return True
        return False

    def has_total_value(self, d):
        return "total_value" in d["values"]

    def _build_other_keys(self, other_cells):
        d = {}
        values = {}
        for other_key, other_value in zip(self.other_keys, other_cells):
            if self._is_key_ignored(other_key):
                continue
            value = self._build_value(other_key, other_value)
            if value is None:
                log.warning(f'Null value for "{other_key}": "{other_value}"')
                return None
            values[other_key] = value

        d["values"] = values
        if self.total_description:
            d["total_description"] = self.total_description

        log.debug(f"self.is_summable={self.is_summable}")
        if self.is_summable:
            self._build_sums(d)
        return d
