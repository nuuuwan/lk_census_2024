from lk_census import FinalReport, ReadMe, XLSXDataTable

if __name__ == "__main__":
    XLSXDataTable.build_all()
    FinalReport.build()
    ReadMe().build()
