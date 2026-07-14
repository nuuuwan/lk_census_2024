from utils_future import Log

log = Log("XLSXDataTableBuilderMixin")


class XLSXDataTableBuilderMixin:
    def build(self):
        self.download_original_doc()
        self.build_gnd_data()
        self.build_all_data()
        self.build_readme()

    @classmethod
    def build_all(cls):
        n = len(cls.list_all())
        data_tables = cls.list_all()
        for i_data_table, data_table in enumerate(data_tables, start=1):
            log.debug("-" * 20)
            log.info(f"{i_data_table}/{n}: {data_table.data_table_id}")
            log.debug("-" * 20)
            data_table.build()
