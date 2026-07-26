from lk_census import LankaDataMetadata, ReadMe, XLSXDataTable

if __name__ == "__main__":
    XLSXDataTable.clean_all()
    XLSXDataTable.build_all()
    LankaDataMetadata.build()
    ReadMe().build()
