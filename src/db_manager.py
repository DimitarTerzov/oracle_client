from db_client import db_client as client
from tables_magaer import TablesManager
from db_tables import *


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
                analysis_unit_dyn_params, scan_encrypt, analysis_unit_scan_window)

def main(manager, remote_job_id):
    manager.set_primary_keys()
    manager.set_foreign_keys(remote_job_id)
    manager.insert_into_tables()


if __name__ == '__main__':
    main(manager)
