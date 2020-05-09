from was_service_automation.dbutils.db_tables import App
from was_service_automation.dbutils.db_tables import Sandbox
from was_service_automation.dbutils.db_tables import AppVer
from was_service_automation.dbutils.db_tables import Analysis
from was_service_automation.dbutils.db_tables import AnalysisUnit
from was_service_automation.dbutils.db_tables import EngineJob
from was_service_automation.dbutils.db_tables import AnalysisUnitDynOp
from was_service_automation.dbutils.db_tables import AnalysisUnitDynParams
from was_service_automation.dbutils.db_tables import ScanEncrypt
from was_service_automation.dbutils.db_tables import AnalysisUnitScanWindow


class TablesManager():
    def __init__(self, client, app=None, sandbox=None, app_ver=None,
                 analysis=None, analysis_unit=None, engine_job=None,
                 analysis_unit_dyn_op=None, analysis_unit_dyn_params=None,
                 scan_encrypt=None, analysis_unit_scan_window=None):
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

    def initTables(self):
        self.app = App()
        self.sandbox = Sandbox()
        self.app_ver = AppVer()
        self.analysis = Analysis()
        self.analysis_unit = AnalysisUnit()
        self.engine_job = EngineJob()
        self.analysis_unit_dyn_op = AnalysisUnitDynOp()
        self.analysis_unit_dyn_params = AnalysisUnitDynParams()
        self.scan_encrypt = ScanEncrypt()
        self.analysis_unit_scan_window = AnalysisUnitScanWindow()

    def insert_into_app(self):
        new_id = self._get_next_seq(self.app.name)
        print("IdValue={}".format(new_id))
        self.app.id = new_id
        sqlString = self.app.insert_statement()
        sqlValues = self.app.values_to_insert()
        print("sqlString={} \nsqlValues={}".format(
            sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_sandbox(self):
        self.sandbox.app_id = self.app.id
        IdValue = self._get_next_seq(self.sandbox.name)
        self.sandbox.id = IdValue
        sqlString = self.sandbox.insert_statement()
        sqlValues = self.sandbox.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_app_ver(self):
        self.app_ver.sandbox_id = self.sandbox.id
        IdValue = self._get_next_seq(self.app_ver.name)
        self.app_ver.id = IdValue
        sqlString = self.app_ver.insert_statement()
        sqlValues = self.app_ver.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_analysis(self):
        self.analysis.app_ver_id = self.app_ver.id
        IdValue = self._get_next_seq(self.analysis.name)
        self.analysis.id = IdValue
        sqlString = self.analysis.insert_statement()
        sqlValues = self.analysis.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_analysis_unit(self):
        self.analysis_unit.analysis_id = self.analysis.id
        IdValue = self._get_next_seq(self.analysis_unit.name)
        self.analysis_unit.id = IdValue
        sqlString = self.analysis_unit.insert_statement()
        sqlValues = self.analysis_unit.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_engine_job(self, remote_job_id):
        self.engine_job.app_ver_id = self.app_ver.id
        self.engine_job.analysis_unit_id = self.analysis_unit.id
        self.engine_job.remote_job_id = remote_job_id
        IdValue = self._get_next_seq(self.engine_job.name)
        self.engine_job.id = IdValue
        sqlString = self.engine_job.insert_statement()
        sqlValues = self.engine_job.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_analysis_unit_dyn_op(self):
        self.analysis_unit_dyn_op.analysis_unit_id = self.analysis_unit.id
        self.analysis_unit_dyn_op.engine_job_id = self.engine_job.id
        IdValue = self._get_next_seq(self.analysis_unit_dyn_op.name)
        self.analysis_unit_dyn_op.id = IdValue
        sqlString = self.analysis_unit_dyn_op.insert_statement()
        sqlValues = self.analysis_unit_dyn_op.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_analysis_unit_dyn_params(self):
        self.analysis_unit_dyn_params.analysis_unit_id = self.analysis_unit.id
        IdValue = self._get_next_seq(self.analysis_unit_dyn_params.name)
        self.analysis_unit_dyn_params.id = IdValue
        sqlString = self.analysis_unit_dyn_params.insert_statement()
        sqlValues = self.analysis_unit_dyn_params.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_scan_encrypt(self):
        self.scan_encrypt.app_ver_id = self.app_ver.id
        IdValue = self._get_next_seq(self.scan_encrypt.name)
        self.scan_encrypt.id = IdValue
        sqlString = self.scan_encrypt.insert_statement()
        sqlValues = self.scan_encrypt.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_analysis_unit_scan_window(self):
        self.analysis_unit_scan_window.analysis_unit_id = self.analysis_unit.id
        IdValue = self._get_next_seq(self.analysis_unit_scan_window.name)
        self.analysis_unit_scan_window.id = IdValue
        sqlString = self.analysis_unit_scan_window.insert_statement()
        sqlValues = self.analysis_unit_scan_window.values_to_insert()
        print("IdValue={} \nsqlString={} \nsqlValues={}".format(
            IdValue, sqlString, sqlValues))
        self.client.execute(sqlString, sqlValues)

    def insert_into_tables(self, remote_job_id):
        self.insert_into_app()
        self.insert_into_sandbox()
        self.insert_into_app_ver()
        self.insert_into_analysis()
        self.insert_into_analysis_unit()
        self.insert_into_engine_job(remote_job_id)
        self.insert_into_analysis_unit_dyn_op()
        self.insert_into_analysis_unit_dyn_params()
        self.insert_into_scan_encrypt()
        self.insert_into_analysis_unit_scan_window()

        self.client.close()

    def preparePlatformTables(self, remote_job_id):
        self.initTables()
        self.insert_into_tables(remote_job_id)

    def _get_max_id(self, db_table):
        """
        get_max_id(db_table=str, id_column_name=str) -> int
        Returns max value for identity column in table with name 'db_table'.
        """
        sql = "select max({}) from {}".format(
            db_table.id_column, db_table.name)
        print("sqlMax={}".format(sql))
        self.client.execute(sql)
        return self.client.fetchone()[0]

    def _get_next_seq(self, db_table_name):
        sName = "SEQ_{}".format(db_table_name)
        sName = sName[ :28]
        sql = "select {}.nextval from dual connect by level <= 1".format(sName)
        print("sqlSeq={} client={}".format(sql, self.client))
        self.client.execute(sql)
        return self.client.fetchone()[0]
