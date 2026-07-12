from lk_census import FinalReport, ReadMe, XLSXDataTable


def not_used():
    XLSXDataTable.build_all()
    ReadMe().build()


if __name__ == "__main__":
    FinalReport.parse()
