from lk_census import OriginalDoc


def main():
    OriginalDoc.download_all()
    OriginalDoc.build_readme()


if __name__ == "__main__":
    main()
