from was_service_automation.utils.clients import db_client as client
from tables_manager import TablesManager
from db_tables import App
from db_tables import Sandbox
from db_tables import AppVer
from db_tables import Analysis
from db_tables import AnalysisUnit
from db_tables import EngineJob
from db_tables import AnalysisUnitDynOp
from db_tables import AnalysisUnitDynParams
from db_tables import ScanEncrypt
from db_tables import AnalysisUnitScanWindow

app = App()
sandbox = Sandbox()
app_ver = AppVer()
analysis = Analysis()
analysis_unint = AnalysisUnit()
engine_job = EngineJob()
analysis_unit_dyn_op = AnalysisUnitDynOp()
analysis_unit_dyn_params = AnalysisUnitDynParams()
scan_encrypt = ScanEncrypt()
analysis_unit_scan_window = AnalysisUnitScanWindow()

manager = TablesManager(client, app, sandbox, app_ver, analysis,
                        analysis_unint, engine_job, analysis_unit_dyn_op,
                        analysis_unit_dyn_params, scan_encrypt,
                        analysis_unit_scan_window)


def main(manager, remote_job_id):
    manager.insert_into_tables(remote_job_id)


def preparePlatformRows(remote_job_id):

    if __name__ == '__main__':
        main(manager, remote_job_id)
