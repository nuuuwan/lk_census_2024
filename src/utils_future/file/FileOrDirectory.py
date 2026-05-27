import os


class FileOrDirectory:
    def __init__(self, path):
        self.path = path

    @property
    def name(self):
        return self.path.split(os.sep)[-1]

    @property
    def exists(self):
        return os.path.exists(self.path)

    def __str__(self):
        return f"{self.path} ({self.size_humanized})"

    def __hash__(self):
        return hash(self.path)

    @property
    def size(self):
        if not self.exists:
            return 0

        if os.path.isfile(self.path):
            return os.path.getsize(self.path)

        total = 0
        for root, _, files in os.walk(self.path):
            for f in files:
                total += os.path.getsize(os.path.join(root, f))

        return total

    @staticmethod
    def humanize_size(size):
        for unit, label in [
            (1_000_000_000, "GB"),
            (1_000_000, "MB"),
            (1_000, "kB"),
        ]:
            if size >= unit:
                return f"{size / unit:.1f} {label}"
        return f"{size} B"

    @property
    def size_humanized(self):
        return self.humanize_size(self.size)

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.path == other.path
        return False
