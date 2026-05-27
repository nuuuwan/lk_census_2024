import csv

from utils_base.file.File import File

DIALECT = 'excel'


class XSVFile(File):
    @property
    def delimiter(self):
        raise NotImplementedError

    @staticmethod
    def _readHelper(delimiter: str, xsv_lines: list):
        data_list = []
        field_names = None
        reader = csv.reader(
            xsv_lines,
            dialect=DIALECT,
            delimiter=delimiter,
        )
        for row in reader:
            if not field_names:
                field_names = row
            else:
                data = dict(
                    zip(
                        field_names,
                        row,
                    )
                )
                if data:
                    data_list.append(data)
        return data_list

    def read(self):
        xsv_lines = File.read_lines(self)
        return XSVFile._readHelper(self.delimiter, xsv_lines)

    @staticmethod
    def get_field_names(data_list):
        return list(data_list[0].keys())

    @staticmethod
    def get_data_rows(data_list, field_names):
        return list(
            map(
                lambda data: list(
                    map(
                        lambda field_name: data[field_name],
                        field_names,
                    )
                ),
                data_list,
            )
        )

    def write(self, data_list):
        with open(self.path, 'w', encoding="utf8") as fout:
            writer = csv.writer(
                fout,
                dialect=DIALECT,
                delimiter=self.delimiter,
            )

            field_names = XSVFile.get_field_names(data_list)
            writer.writerow(field_names)
            writer.writerows(XSVFile.get_data_rows(data_list, field_names))
            fout.close()
