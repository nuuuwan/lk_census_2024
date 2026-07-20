from functools import cached_property


class FinalReportTableBuildMixin:
    def clean(self):
        self.raw_data_file.delete()
        self.data_file.delete()
        self.lanka_data_file.delete()

    def build(self, force=False):
        self.build_original_pdf(force)
        self.build_raw_data(force)
        self.build_data(force)
        self.build_lanka_data(force)
        self.build_readme(force)

    STATUS_LABELS = {
        0: "Original PDF is missing",
        1: "Raw data is missing",
        2: "Raw data is difficult to parse",
        3: "Data is missing",
        4: "Lanka data is missing",
        5: "All Stages Complete",
    }

    STATUS_EMOJIS = {
        0: "⚫️",
        1: "🟤",
        2: "🔴",
        3: "🟠",
        4: "🟡",
        5: "✅",
    }

    STATUS_COLORS = {
        0: "#000000",
        1: "#8B4513",
        2: "#FF0000",
        3: "#FFA500",
        4: "#FFFF00",
        5: "#00c000",
    }

    # flake8: noqa: C901
    @cached_property
    def build_status(self):
        if not self.original_pdf_file.exists():
            return 0

        if not self.raw_data_file.exists():
            return 1

        if self.is_complicated:
            return 2

        if not self.data_file.exists():
            return 3

        if not self.lanka_data_file.exists():
            return 4

        return 5
