import cx_Oracle
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
        app_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.app.insert_statement(),
                            self.app.values_to_insert(app_id))
        self.app.id = int(app_id.getvalue()[0])

    def insert_into_sandbox(self):
        self.sandbox.app_id = self.app.id
        sandbox_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.sandbox.insert_statement(),
                            self.sandbox.values_to_insert(sandbox_id))
        self.sandbox.id = int(sandbox_id.getvalue()[0])

    def insert_into_app_ver(self):
        self.app_ver.sandbox_id = self.sandbox.id
        app_ver_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.app_ver.insert_statement(),
                    self.app_ver.values_to_insert(app_ver_id))
        self.app_ver.id = int(app_ver_id.getvalue()[0])

    def insert_into_analysis(self):
        self.analysis.app_ver_id = self.app_ver.id
        analysis_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.analysis.insert_statement(),
                    self.analysis.values_to_insert(analysis_id))
        self.analysis.id = int(analysis_id.getvalue()[0])

    def insert_into_analysis_unit(self):
        self.analysis_unit.analysis_id = self.analysis.id
        analysis_unit_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.analysis_unit.insert_statement(),
                self.analysis_unit.values_to_insert(analysis_unit_id))
        self.analysis_unit.id = int(analysis_unit_id.getvalue()[0])

    def insert_into_engine_job(self, remote_job_id):
        self.engine_job.app_ver_id = self.app_ver.id
        self.engine_job.analysis_unit_id = self.analysis_unit.id
        self.engine_job.remote_job_id = remote_job_id
        engine_job_id = self.client.cursor.var(cx_Oracle.NUMBER)
        self.client.execute(self.engine_job.insert_statement(),
                    self.engine_job.values_to_insert(engine_job_id))
        self.engine_job.id = int(engine_job_id.getvalue()[0])

    def insert_into_analysis_unit_dyn_op(self):
        self.analysis_unit_dyn_op.analysis_unit_id = self.analysis_unit.id
        self.analysis_unit_dyn_op.engine_job_id = self.engine_job.id
        self.client.execute(self.analysis_unit_dyn_op.insert_statement(),
                            self.analysis_unit_dyn_op.values_to_insert())

    def insert_into_analysis_unit_dyn_params(self):
        self.analysis_unit_dyn_params.analysis_unit_id = self.analysis_unit.id
        self.client.execute(self.analysis_unit_dyn_params.insert_statement(),
                            self.analysis_unit_dyn_params.values_to_insert())

    def insert_into_scan_encrypt(self):
        self.scan_encrypt.app_ver_id = self.app_ver.id
        self.client.execute(self.scan_encrypt.insert_statement(),
                            self.scan_encrypt.values_to_insert())

    def insert_into_analysis_unit_scan_window(self):
        self.analysis_unit_scan_window.analysis_unit_id = self.analysis_unit.id
        self.client.execute(self.analysis_unit_scan_window.insert_statement(),
                            self.analysis_unit_scan_window.values_to_insert())


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
