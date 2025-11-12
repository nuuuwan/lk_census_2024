import os
import re
from dataclasses import dataclass

import camelot
import pandas as pd
from gig import Ent, EntType
from pypdf import PdfReader, PdfWriter
from utils import JSONFile, Log, PDFFile, TSVFile

log = Log("OriginalDocTable")


@dataclass
class OriginalDocTable:
    doc_name: str
    table_title: str
    pages: tuple[int, int]
    field_list: list[str]

    DIR_DATA = "data"

    @property
    def n_fields(self) -> int:
        return len(self.field_list)

    @property
    def pdf_file(self):
        return PDFFile(
            os.path.join(
                "original_docs",
                f"{self.doc_name}.pdf",
            )
        )

    @property
    def page_start(self):
        return self.pages[0]

    @property
    def page_end(self):
        return self.pages[1]

    @property
    def pdf_path(self):
        return os.path.join(
            "original_docs",
            f"{self.doc_name}.pdf",
        )

    @property
    def name_safe(self):
        name_safe = re.sub(r"\s+", " ", self.table_title)
        name_safe = name_safe.replace(" ", "-")
        name_safe = "".join(
            char for char in name_safe if char.isalnum() or char == "-"
        )
        return name_safe

    @property
    def dir_table(self):
        return os.path.join(
            self.DIR_DATA,
            self.doc_name,
            self.name_safe,
        )

    @property
    def subset_pdf_path(self):
        return os.path.join(
            self.dir_table,
            "table.pdf",
        )

    def save_subset_pdf(self):
        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        for page_num in range(self.page_start - 1, self.page_end):
            if page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])

        with open(self.subset_pdf_path, "wb") as output_file:
            writer.write(output_file)

        log.debug(
            f"Wrote pages {self.page_start}-{self.page_end} "
            + f"to {PDFFile(self.subset_pdf_path)}"
        )
        return self.subset_pdf_path

    @staticmethod
    def parse_int(x: str) -> int | str:
        try:
            return int(x)
        except ValueError:
            return x

    def extract_raw_table(self):
        pages = f"{self.page_start}-{self.page_end}"
        tables = camelot.read_pdf(
            self.pdf_path,
            pages=pages,
            flavor="stream",
            strip_text="\n",
            row_tol=20,
            edge_tol=300,
        )
        df = pd.concat([t.df for t in tables], ignore_index=True)
        table_data = df.to_dict(orient="records")

        arr_of_arr = []
        for row_data in table_data:
            arr = []
            for cell_original in row_data.values():
                cell = str(cell_original)
                if cell in ["", "nan"]:
                    continue
                cell = cell.replace("‐", "-")
                cell = cell.replace("- - ", "")
                cell = cell.replace("- - ", "")
                cell = re.sub(r"[^A-Za-z0-9\s\-]", "", cell)
                cell = re.sub(r"\s+", " ", cell).strip()
                cell = self.parse_int(cell)

                arr.append(cell)
            arr_of_arr.append(arr)

        json_file = JSONFile(os.path.join(self.dir_table, "raw-table.json"))
        json_file.write(arr_of_arr)
        log.debug(f"Wrote {len(arr_of_arr)} raw rows to {json_file}")
        return arr_of_arr

    @staticmethod
    def get_ent_type(region_name: str) -> EntType:
        if region_name == "Sri Lanka":
            return EntType.COUNTRY
        if "District" in region_name:
            return EntType.DISTRICT
        return EntType.DSD

    @staticmethod
    def validate(d_list: list[dict]):
        d_list_without_ents = [
            ent for ent in d_list if ent.get("region_id", "").endswith("XX")
        ]

        if not d_list_without_ents:
            log.debug("✅ All region names mapped to Ents successfully.")
        else:
            log.error(
                f"⁉️ {len(d_list_without_ents)} region names"
                + " could not be mapped to Ents:"
            )
            for d in d_list_without_ents:
                log.error(f" - {d['region_id']} {d['region_name']}")

        parsed_id_set = set([d["region_id"] for d in d_list])
        for ent_type in [EntType.COUNTRY, EntType.DISTRICT, EntType.DSD]:
            ent_id_set = set([ent.id for ent in Ent.list_from_type(ent_type)])
            non_parsed_district_set = ent_id_set - parsed_id_set
            if non_parsed_district_set:
                log.error(
                    f"⁉️ {len(non_parsed_district_set)}"
                    + f" {ent_type.name}s not parsed:"
                )
                for ent_id in non_parsed_district_set:
                    ent = Ent.from_id(ent_id)
                    log.error(f" - {ent.id} {ent.name}")
            else:
                log.debug(f"✅All {ent_type.name}s parsed successfully.")

        total_mismatch_d_list = []
        for d in d_list:
            total = d["total"]
            total_from_fields = sum([v for v in list(d.values())[5:]])
            if total != total_from_fields and 2 * total != total_from_fields:
                total_mismatch_d_list.append(
                    d | dict(total_from_fields=total_from_fields)
                )

        if not total_mismatch_d_list:
            log.debug("✅ All totals match sum of fields.")
        else:
            log.error(
                f"⁉️ {len(total_mismatch_d_list)} rows with"
                + " total mismatch errors:"
            )
            for d in total_mismatch_d_list:
                log.error(
                    f" - {d['region_id']} {d['region_name']}:"
                    + f" {d['total']} != {d['total_from_fields']}"
                )

        d_list_population_mismatch = []
        MAX_POPULATION_CHANGE_RATIO = 1.5
        for d in d_list:
            if "XX" in d["region_id"]:
                continue
            ent = Ent.from_id(d["region_id"])
            total = d["total"]
            total_from_ent_2012 = ent.population
            population_change_ratio = total / total_from_ent_2012

            if (
                population_change_ratio > MAX_POPULATION_CHANGE_RATIO
                or population_change_ratio < 1 / MAX_POPULATION_CHANGE_RATIO
            ):
                d_list_population_mismatch.append(
                    d
                    | dict(
                        total_from_ent_2012=total_from_ent_2012,
                        population_change_ratio=population_change_ratio,
                    )
                )

        if len(d_list_population_mismatch) == 0:
            log.debug("✅ All population changes within expected range.")
        else:
            log.error(
                f"⚠️ {len(d_list_population_mismatch)} rows with"
                + " large population changes:"
            )
            for d in d_list_population_mismatch:
                population_change_ratio = d["population_change_ratio"]
                log.error(
                    f" - {d['region_id']} {d['region_name']}:"
                    + f" {d['total_from_ent_2012']:,} -> {d['total']:,}"
                    + f" ({population_change_ratio:.2}x)"
                )

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

        parsed_region_set = set()
        n_rows = len(raw_table)
        region_names_without_ents = []
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
                region_names_without_ents.append((region_id, region_name))
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
            parsed_region_set.add(region_id)

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

    @classmethod
    def list_all(cls) -> list["OriginalDocTable"]:
        return [
            # OriginalDocTable(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A4. Migrant population"
            #     + " by reason for migrating according to districts",
            #     (110, 111),
            #     [],
            # ),
            # OriginalDocTable(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A5. Population by sex, age and district according to DSD",
            #     (112, 136),
            #     [
            #         "sex-male",
            #         "sex-female",
            #         "age-under-15",
            #         "age-15-to-59",
            #         "age-60-to-64",
            #         "age-65-and-over",
            #     ],
            # ),
            # OriginalDocTable(
            #     "Basic-Population-Information"
            #     + "-by-Districts-and-Divisional-Secretary-Divisions",
            #     "A6. Population by ethnicity and district according to DSD",
            #     (137, 161),
            #     [
            #         "sinhalese",
            #         "sri_lanka_tamil",
            #         "indian_tamil_or_malaiyaga_thamilar",
            #         "sri_lanka_moor_or_muslim",
            #         "burgher",
            #         "malay",
            #         "sri_lanka_chetty",
            #         "bharatha",
            #         "veddhas",
            #         "other",
            #     ],
            # ),
            OriginalDocTable(
                "Basic-Population-Information"
                + "-by-Districts-and-Divisional-Secretary-Divisions",
                "A7. Population by religion and district according to DSD",
                (162, 185),
                [
                    "buddhist",
                    "hindu",
                    "islam",
                    "roman_catholic",
                    "other_christian",
                    "other",
                ],
            ),
        ]

    @classmethod
    def extract_all(cls):

        for original_doc_table in cls.list_all():
            os.makedirs(original_doc_table.dir_table, exist_ok=True)
            original_doc_table.save_subset_pdf()
            original_doc_table.extract_data()
