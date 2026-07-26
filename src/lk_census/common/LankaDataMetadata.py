from ds import Datumset
from utils_future import Directory, File, JSONFile, Log

log = Log("LankaDataMetadata")


class LankaDataMetadata:
    METADATA_FILE = JSONFile("metadata", "lanka_data.metadata.json")

    @classmethod
    def _get_files_for_xlsx(cls):
        lanka_data_files = []
        dir_data = Directory("data")
        for child_name in dir_data:
            if child_name == "final-report-tables":
                continue
            child_dir = Directory(dir_data, child_name)
            lanka_data_file = JSONFile(child_dir, "lanka_data.json")
            if lanka_data_file.exists():
                lanka_data_files.append(lanka_data_file)

        return lanka_data_files

    @classmethod
    def _get_files_for_final_report(cls):
        lanka_data_files = []
        dir_data = Directory("data", "final-report-tables")
        for child_name in dir_data:
            child_dir = Directory(dir_data, child_name)
            for child_name2 in child_dir:
                child_dir2 = Directory(child_dir, child_name2)
                lanka_data_file = JSONFile(child_dir2, "lanka_data.json")
                if lanka_data_file.exists():
                    lanka_data_files.append(lanka_data_file)

        return lanka_data_files

    @classmethod
    def _build_from_lanka_data_files(cls, lanka_data_files):
        idx = {}
        for lanka_data_file in lanka_data_files:
            datumset = Datumset.from_data(lanka_data_file.read())
            for datum in datumset:
                query_str = datum.query.query_str
                if query_str not in idx:
                    idx[query_str] = []
                if lanka_data_file.path not in idx[query_str]:
                    idx[query_str].append(lanka_data_file.path)

        for query_str, files in idx.items():
            if len(files) > 1:
                log.warning(
                    f"Query '{query_str}' is present in multiple files: {files}"
                )
        return idx

    @classmethod
    def build(cls):
        lanka_data_files = (
            cls._get_files_for_xlsx() + cls._get_files_for_final_report()
        )

        idx = cls._build_from_lanka_data_files(lanka_data_files)

        LankaDataMetadata.METADATA_FILE.write(idx)
        log.info(f"Wrote {LankaDataMetadata.METADATA_FILE}")
