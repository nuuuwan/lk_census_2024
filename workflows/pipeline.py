from lk_census import FinalReport, LankaDataMetadata, ReadMe, XLSXDataTable


def main():
    FinalReport.clean_all()
    FinalReport.build_all()

    XLSXDataTable.clean_all()
    XLSXDataTable.build_all()

    LankaDataMetadata.build()
    ReadMe().build()


if __name__ == "__main__":
    main()
