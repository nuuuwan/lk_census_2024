from utils_base.file.XSVFile import XSVFile


class TSVFile(XSVFile):
    @property
    def delimiter(self):
        return '\t'
