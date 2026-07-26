from lk_census import FinalReport, LankaDataMetadata, ReadMe

if __name__ == "__main__":
    FinalReport.clean_all()
    FinalReport.build_all()
    LankaDataMetadata.build()
    ReadMe().build()
