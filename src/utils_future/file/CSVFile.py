from utils_base.file.XSVFile import XSVFile


class CSVFile(XSVFile):
    @property
    def delimiter(self):
        return ','
