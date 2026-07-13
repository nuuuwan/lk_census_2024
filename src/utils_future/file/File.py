import os

from utils_base.file.FileOrDirectory import FileOrDirectory

DIALECT = "excel"
DELIM_LINE = "\n"
ENCODING = "utf-8"


class File(FileOrDirectory):

    @property
    def ext(self):
        return self.name.split(".")[-1]

    def read(self):
        with open(self.path, "r", encoding=ENCODING) as fin:
            content = fin.read()
            fin.close()
        return content

    def write(self, content):
        with open(self.path, "w", encoding=ENCODING) as fout:
            fout.write(content)
            fout.close()

    def read_lines(self):
        content = File.read(self)
        return content.split(DELIM_LINE)

    def write_lines(self, lines):
        content = DELIM_LINE.join(lines)
        File.write(self, content)

    def open(self, app=None):
        if app is None:
            os.system(f'open "{self.path}"')
        else:
            os.system(f'{app} "{self.path}"')

    def delete(self):
        if os.path.exists(self.path):
            os.remove(self.path)
