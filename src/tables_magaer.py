class TablesManager():
    def __init__(self, client, app, sandbox, app_ver, analysis, analysis_unit,
                 engine_job, analysis_unit_dyn_op, analysis_unit_dyn_params,
                 scan_encrypt, analysis_unit_scan_window):
        self.client = client
        self.app_table = app
        self.sandbox_table = sandbox
        self.app_ver_table = app_ver
        self.analysis_table = analysis
        self.analysis_unit_table = analysis_unit
        self.engine_job_table = engine_job
        self.analysis_unit_dyn_op_table = analysis_unit_dyn_op
        self.analysis_unit_dyn_params_table = analysis_unit_dyn_params
        self.scan_encrypt_table = scan_encrypt
        self.analysis_unit_scan_window_table = analysis_unit_scan_window

    def set_new_ids(self):
        tables = [self.app_table, self.sandbox_table, self.app_ver_table,
            self.analysis_table, self.analysis_unit_table, self.engine_job_table,
            self.analysis_unit_dyn_op_table, self.analysis_unit_dyn_params_table,
            self.scan_encrypt_table, self.analysis_unit_scan_window_table]

        for table in tables:
            max_id = self._get_max_id(table)
            new_id = max_id + 20000
            table.id = new_id

    def insert_into_tables(self):
        tables = [self.app_table, self.sandbox_table, self.app_ver_table,
            self.analysis_table, self.analysis_unit_table, self.engine_job_table,
            self.analysis_unit_dyn_op_table, self.analysis_unit_dyn_params_table,
            self.scan_encrypt_table, self.analysis_unit_scan_window_table]

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