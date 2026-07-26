from lk_census import FinalReportTable


def main():
    tables = FinalReportTable.list()
    for table in tables:
        table.oneoff_fix_id()


if __name__ == "__main__":
    main()
