from lk_census import FinalReport, LankaDataMetadata, ReadMe, XLSXDataTable


def main():
    FinalReport.build()
    XLSXDataTable.build_all()
    LankaDataMetadata.build()
    ReadMe().build()


if __name__ == "__main__":
    main()
