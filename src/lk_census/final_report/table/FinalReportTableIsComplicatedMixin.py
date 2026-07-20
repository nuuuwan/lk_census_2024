class FinalReportTableIsComplicatedMixin:
    COMPLICATED_TABLE_NUM_LIST = [
        # Chapter 5
        "5.1.7",  # Triple Row
        "5.2.2",  # Triple Row
        "5.2.5",  # Col Sum
        # Chapter 6
        "6.1.6",  # Data error
        "6.1.13",  # Double Row
        "6.2.1",  # Double Row
        "6.2.4",  # Double Row
        "6.2.5",  # Double Row
        "6.2.13",  # Double Row
        "6.2.14",  # Double Row
        "6.3.1",  # Data error
        # Chapter 7
        "7.6",  # Double Row
        # Chapter 9
        "9.1",  # Double Row
        "9.2",  # Double Row
        "9.17",  # no primary_key
        # Chapter 10
        "10.3",  # Double Row
        "10.4",  # Double Row
        "10.6",  # Double Row
        "10.7",  # Double Row
        "10.10",  # Double Row
        # Chapter 11
        "11.6",  # Sub-headings
        "11.17",  # Sub-headings
    ]

    @property
    def is_complicated(self):
        return self.table_num in self.COMPLICATED_TABLE_NUM_LIST
