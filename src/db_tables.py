from db_utils import params_as_list


class App():
    def __init__(self):
        self.name = 'app'
        self.id_column = 'APP_ID'
        self._app_id = None
        self._column_count = 57

    @property
    def id(self):
        return self._app_id

    @id.setter
    def id(self, new_id):
        self._app_id = new_id

    @property
    def nas_dir(self):
        return 'veracode/app{}'.format(self._app_id)

    def insert_statement(self):
        sql = """
        insert into APP (APP_ID, APP_NAME, ARCHER_APP_NAME, APP_TYPE_ID, DESCRIPTION,
        INDUSTRY_VERTICAL_ID, NAS_DIR, APP_SOURCE_ID, ACCOUNT_ID, ENTERPRISE_ACCOUNT_ID,
        VENDOR_ACCOUNT_ID, VENDOR_APP_ID, LOGIN_ACCOUNT_ID, DELETED, DELETED_FILES,
        APP_ASSUR_ID, IS_WEBAPP, IS_DYNAMICMP, ASSESS_TYPE, WEB_SITE_URL,
        RDB_PROJECT_ID, NAS_LOGO_PATH, PROFILE_COMPLETE, LAST_AUDITOR_ID, MULTI_PLATFORM,
        DEPLOYMENT_METHOD, BUS_UNIT_ID, BUS_OWNER_NAME, BUS_OWNER_EMAIL, POLICY_GROUP_ID,
        SEND_POLICY_NOTIFICATIONS, POLICY_LOCKED, LAST_ASSIGNED_TS, SANITIZED, SUMMARIZATION_SETTING,
        DYN_SCAN_NOT_REQ_APRVL, DYNAMIC_SCAN_TYPE, S2_SETTING, VENDOR_RESCAN,
        ALLOW_DEP_AS_TOP_LEVEL_MODULES, INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER,
        DID_SET_ORIGINAL_ISSUE_DATE, ORIGINAL_ISSUE_DATE_TS, ENTERPRISE_ENABLED_SCA,
        VENDOR_ENABLED_SCA, REMEDIATION_TS, APP_REMEDIATION_STATUS, XPA_ENABLED, IS_DEMO,
        NEXT_DAY_SCHEDULING_ENABLED, KEEP_BINARY_DAYS, S3_ONLY, S3_BUCKET_ID, PRESCAN_WORKFLOW)
        VALUES {}""".format(params_as_list(self._column_count))
        return sql

    def values_to_insert(self):
        values = (
            self.id,'20__VeracodeMP__50860', None,
            25, 'e460adbc-0626-4826-8907-9c12ab0e8d72',
            447, self.nas_dir, 1607, 1, None, None, None,
            10520, 0, 0, 2502, 1, 1, 1, None, None, None,
            1, '42524238-3376-485e-a768-c5888b2664df', 0,
            1, 1, None, None, 2, 0, 0, '06-APR-20 10.26.57.488000000 PM',
            0, 0, 0, None, 1, 0, 0, '06-APR-20 10.26.57.751000000 PM',
            '06-APR-20 11.06.19.068639000PM', 'internal', 2,
            0, None, 0, 0, None, 1, 0, 0, 0, -1, 0, -1, 0
        )

        return values


class Sandbox():
    def __init__(self):
        self.name = 'sandbox'


class AppVer():
    def __init__(self):
        self.name = 'app_ver'


class Analysis():
    def __init__(self):
        self.name = 'analysis'


class AnalysisUnit():
    def __init__(self):
        self.name = 'analysis_unit'


class EngineJob():
    def __init__(self):
        self.name = 'engine_job'


class AnalysisUnitDynOp():
    def __init__(self):
        self.name = 'analysis_unit_dyn_op'


class AnalysisUnitDynParams():
    def __init__(self):
        self.name = 'analysis_unit_dyn_params'


class ScanEncrypt():
    def __init__(self):
        self.name = 'scan_encrypt'


class AnalysisUnitScanWindow():
    def __init__(self):
        self.name = 'analysis_unit_scan_window'
