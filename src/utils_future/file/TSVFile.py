from utils_future.file.XSVFile import XSVFile


class TSVFile(XSVFile):
    @property
    def delimiter(self):
        return "\t"
