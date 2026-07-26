from lk_census import ReadMe, XLSXDataTable

if __name__ == "__main__":
    XLSXDataTable.clean_all()
    XLSXDataTable.build_all()
    ReadMe().build()
