from utils import Log

log = Log("DataTable")


class DataTableExtractDataCleanerMixin:
    def __shift_shifted_region_names__(self, raw_table):
        for i_row in range(len(raw_table) - 1):
            row = raw_table[i_row]
            if len(row) != 2 + self.n_fields or raw_table[i_row][0] != "":
                continue
            if raw_table[i_row + 1][0] != "":
                log.debug(f"<- {raw_table[i_row + 1][0]}")
                raw_table[i_row][0] = raw_table[i_row + 1][0]
                if len(raw_table[i_row + 1]) == 2 + self.n_fields:
                    raw_table[i_row + 1][0] = ""

        assert (
            len(raw_table) > 0
        ), "No raw table rows, after shifting region names"
        return raw_table

    def __split_row_if_merged__(self, row):
        first_cell = row[0]
        tokens = str(first_cell).split(" ")
        if len(tokens) < 2:
            return row

        value = self.__parse_int__(tokens[0])
        if not isinstance(value, int):
            return row

        region_name = " ".join(tokens[1:])
        row = [region_name, value] + row[1:].copy()
        return row

    def clean_raw_table(self, raw_table):
        log.debug(f"self.n_fields={self.n_fields}")
        raw_table = self.__shift_shifted_region_names__(raw_table)

        n_rows = len(raw_table)
        cleaned_raw_table = []
        for i_row in range(n_rows):
            row = raw_table[i_row]
            if len(row) != 1 + self.n_fields:
                row = self.__split_row_if_merged__(row)
            if len(row) != 2 + self.n_fields:
                continue
            cleaned_raw_table.append(row)

        assert len(cleaned_raw_table) > 0, "No cleaned raw table rows"
        return cleaned_raw_table
