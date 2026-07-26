from lk_census import FinalReport, ReadMe

if __name__ == "__main__":
    FinalReport.clean_all()
    FinalReport.build_all()
    ReadMe().build()
