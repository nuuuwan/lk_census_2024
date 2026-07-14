from functools import cached_property


class FinalReportTableBuildMixin:
    def build(self):
        self.build_original_pdf()
        self.build_raw_data()
        self.build_data()
        self.build_lanka_data()

    STATUS_LABELS = {
        0: "⚫️ Original PDF is missing",
        1: "🟤 Raw data is missing",
        2: "🔴 Raw data is difficult to parse",
        3: "🟠 Data is missing",
        4: "🟡 Lanka data is missing",
        9: "🟢 Complete",
    }

    # flake8: noqa: C901
    @cached_property
    def build_status(self):
        if not self.original_pdf_file.exists:
            return 0

        if not self.raw_data_file.exists:
            return 1

        if self.is_complicated:
            return 2

        if not self.data_file.exists:
            return 3

        if not self.lanka_data_file.exists:
            return 4

        return 5
