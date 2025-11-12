import os

from lk_census import OriginalDoc


def main():
    OriginalDoc.download_all()
    OriginalDoc.build_readme()
    os.system("git add original_docs")
    os.system(
        'git commit -m "[download_original_docs] $(date +%"Y-%m-%d %H:%M")"'
    )


if __name__ == "__main__":
    main()
