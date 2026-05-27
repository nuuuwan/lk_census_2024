import json

from utils_base.file.File import File


class JSONFile(File):
    def read(self):
        content = File.read(self)
        return json.loads(content)

    def write(self, data):
        content = json.dumps(data, indent=2)
        File.write(self, content)
