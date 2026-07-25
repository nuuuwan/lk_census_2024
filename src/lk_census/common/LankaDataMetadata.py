from utils_future import Directory, File, JSONFile, Log

log = Log("LankaDataMetadata")


class LankaDataMetadata:
    METADATA_FILE = JSONFile("metadata", "lanka_data.metadata.json")

    @classmethod
    def _build_for_xlsx(cls):
        metadata_list = []
        dir_data = Directory("data")
        for child_name in dir_data:
            if child_name == "final-report-tables":
                continue
            child_dir = Directory(dir_data, child_name)
            metadata_list.append(child_dir.path)

        return metadata_list

    @classmethod
    def _build_for_final_report(cls):
        metadata_list = []
        dir_data = Directory("data", "final-report-tables")
        for child_name in dir_data:
            child_dir = Directory(dir_data, child_name)
            for child_name2 in child_dir:
                child_dir2 = Directory(child_dir, child_name2)
                lanka_data_file = File(child_dir2, "lanka_data.json")
                if lanka_data_file.exists():
                    metadata_list.append(child_dir2.path)

        return metadata_list

    @classmethod
    def build(cls):
        metadata_list = cls._build_for_xlsx() + cls._build_for_final_report()
        LankaDataMetadata.METADATA_FILE.write(metadata_list)
        log.info(f"Wrote {LankaDataMetadata.METADATA_FILE}")
