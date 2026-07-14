from utils_future.file.XSVFile import XSVFile


class CSVFile(XSVFile):
    @property
    def delimiter(self):
        return ","
