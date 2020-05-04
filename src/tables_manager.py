class TablesManager():
    def __init__(self, client, app, sandbox, app_ver, analysis, analysis_unit,
                 engine_job, analysis_unit_dyn_op, analysis_unit_dyn_params,
                 scan_encrypt, analysis_unit_scan_window):
        self.client = client
        self.app = app
        self.sandbox = sandbox
        self.app_ver = app_ver
        self.analysis = analysis
        self.analysis_unit = analysis_unit
        self.engine_job = engine_job
        self.analysis_unit_dyn_op = analysis_unit_dyn_op
        self.analysis_unit_dyn_params = analysis_unit_dyn_params
        self.scan_encrypt = scan_encrypt
        self.analysis_unit_scan_window = analysis_unit_scan_window

    def set_primary_keys(self):
        tables = [self.app, self.sandbox, self.app_ver,
            self.analysis, self.analysis_unit, self.engine_job,
            self.analysis_unit_dyn_op, self.analysis_unit_dyn_params,
            self.scan_encrypt, self.analysis_unit_scan_window]

        for table in tables:
            max_id = self._get_max_id(table)
            new_id = max_id + 20000
            table.id = new_id

    def set_foreign_keys(self, remote_job_id):
        pass

    def insert_into_tables(self):
        tables = [self.app, self.sandbox, self.app_ver,
            self.analysis, self.analysis_unit, self.engine_job,
            self.analysis_unit_dyn_op, self.analysis_unit_dyn_params,
            self.scan_encrypt, self.analysis_unit_scan_window]

        for table in tables:
            self.client.excute(table.insert_statement(), table.values_to_insert())

        self.client.close()

    def _get_max_id(self, db_table):
        """
        get_max_id(db_table=str, id_column_name=str) -> int
        Returns max value for identity column in table with name 'db_table'.
        """
        sql = "select max({}) from {}".format(db_table.id_column, db_table.name)
        self.client.execute(sql)
        return self.client.fetchone()[0]
