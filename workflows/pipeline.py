from lk_census import FinalReport, ReadMe, XLSXDataTable


def not_running():
    FinalReport.build()


if __name__ == "__main__":
    XLSXDataTable.build_all()
    ReadMe().build()
