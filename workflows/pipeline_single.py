import sys

from utils_future import Directory

from lk_census import FinalReportTable


def main(table_num):
    table = FinalReportTable.from_table_num(table_num)

    table.clean()
    table.build()

    table.fields_file.open("code")
    table.data_file.open("code")
    table.lanka_data_file.open("code")
    table.original_pdf_image_file.open("code")


if __name__ == "__main__":
    main(table_num=sys.argv[1])
