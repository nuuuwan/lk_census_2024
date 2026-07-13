from lk_census import FinalReport, ReadMe, XLSXDataTable


def not_used():
    XLSXDataTable.build_all()


if __name__ == "__main__":
    FinalReport.build()
    ReadMe().build()
