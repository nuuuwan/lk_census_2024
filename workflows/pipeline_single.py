import sys

from utils_future import Directory

from lk_census import FinalReportTable


def main(table_num):
    table = FinalReportTable.from_table_num(table_num)
    Directory(table.dir_data).open("code")

    table.build()


if __name__ == "__main__":
    main(table_num=sys.argv[1])
