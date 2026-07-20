from lk_census import FinalReport, ReadMe, XLSXDataTable


def not_running():
    FinalReport.build()
    XLSXDataTable.build_all()
    ReadMe().build()


if __name__ == "__main__":
    # FinalReport.build()
    XLSXDataTable.build_all()
    ReadMe().build()
