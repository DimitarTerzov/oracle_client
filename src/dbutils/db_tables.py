from was_service_automation.dbutils.db_utils import params_as_list


class App:
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

    @property
    def app_name(self):
        return 'AutomationInsert{}'.format(self._app_id)

    def insert_statement(self):
        sql = """
        insert into APP
        (APP_ID, APP_NAME, ARCHER_APP_NAME, APP_TYPE_ID, DESCRIPTION,
        INDUSTRY_VERTICAL_ID, NAS_DIR, APP_SOURCE_ID, ACCOUNT_ID,
        ENTERPRISE_ACCOUNT_ID,
        VENDOR_ACCOUNT_ID, VENDOR_APP_ID, LOGIN_ACCOUNT_ID, DELETED,
        DELETED_FILES,
        APP_ASSUR_ID, IS_WEBAPP, IS_DYNAMICMP, ASSESS_TYPE, WEB_SITE_URL,
        RDB_PROJECT_ID, NAS_LOGO_PATH, PROFILE_COMPLETE, LAST_AUDITOR_ID,
        MULTI_PLATFORM,
        DEPLOYMENT_METHOD, BUS_UNIT_ID, BUS_OWNER_NAME, BUS_OWNER_EMAIL,
        POLICY_GROUP_ID,
        SEND_POLICY_NOTIFICATIONS, POLICY_LOCKED, LAST_ASSIGNED_TS, SANITIZED,
        SUMMARIZATION_SETTING,
        DYN_SCAN_NOT_REQ_APRVL, DYNAMIC_SCAN_TYPE, S2_SETTING, VENDOR_RESCAN,
        ALLOW_DEP_AS_TOP_LEVEL_MODULES, INSERT_TS, MODIFIED_TS, MODIFIED_BY,
        RECORD_VER,
        DID_SET_ORIGINAL_ISSUE_DATE, ORIGINAL_ISSUE_DATE_TS,
        ENTERPRISE_ENABLED_SCA,
        VENDOR_ENABLED_SCA, REMEDIATION_TS, APP_REMEDIATION_STATUS,XPA_ENABLED,
        IS_DEMO,
        NEXT_DAY_SCHEDULING_ENABLED, KEEP_BINARY_DAYS, S3_ONLY, S3_BUCKET_ID,
        PRESCAN_WORKFLOW)
        VALUES {0} returning APP_ID into :{1}""".format(
                    params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_APP.nextval', self.app_name, None,
            25, 'e460adbc-0626-4826-8907-9c12ab0e8d72',
            447, self.nas_dir, 1607, 1, None, None, None,
            10520, 0, 0, 2502, 1, 1, 1, None, None, None,
            1, '42524238-3376-485e-a768-c5888b2664df', 0,
            1, 1, None, None, 2, 0, 0, '06-APR-20 10.26.57.488000000 PM',
            0, 0, 0, None, 1, 0, 0, '06-APR-20 10.26.57.751000000 PM',
            '06-APR-20 11.06.19.068639000PM', 'internal', 2,
            0, None, 0, 0, None, 1, 0, 0, 0, -1, 0, -1, 0, id_
        )

        return values


class Sandbox:
    def __init__(self):
        self.name = 'sandbox'
        self.id_column = 'SANDBOX_ID'
        self._sandbox_id = None
        self._app_id = None
        self._column_count = 21

    @property
    def id(self):
        return self._sandbox_id

    @id.setter
    def id(self, new_id):
        self._sandbox_id = new_id

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, new_id):
        self._app_id = new_id

    def insert_statement(self):
        sql = """
        insert into SANDBOX (SANDBOX_ID, SANDBOX_NAME, ACCOUNT_ID, APP_ID,
        POLICY_SANDBOX, CREATOR_LOGIN_ID, CREATED_TS, DELETED, LAST_AUDITOR_ID,
        INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER, SANITIZED,
        DYN_UNIQUE_ISSUE_POP_STATUS,
        DYN_UNIQ_ISSU_CHKSM_POP_STS, DYN_UNIQ_ISSU_POP_RETRY_CNT,
        DELETED_FILES,
        EXPIRED_TS, PURGE_ON_PROMOTE, AUTO_RECREATE)
        VALUES {0} returning SANDBOX_ID into :{1}""".format(
                params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_SANDBOX.nextval', 'Policy Sandbox. Do not display this text.',
            1, self.app_id, 1, 10520,
            '06-APR-20 10.26.58.567000000PM',
            0, '42524238-3376-485e-a768-c5888b2664df',
            '06-APR-20 10.26.58.571000000 PM',
            '06-APR-20 11.06.19.075785000 PM',
            'onewas-test', 1, 0, 3, 3, None,
            0, None, 0, 0, id_
        )
        return values


class AppVer:
    def __init__(self):
        self.name = 'app_ver'
        self.id_column = 'APP_VER_ID'
        self._app_ver_id = None
        self._sandbox_id = None
        self._column_count = 55

    @property
    def id(self):
        return self._app_ver_id

    @id.setter
    def id(self, new_id):
        self._app_ver_id = new_id

    @property
    def sandbox_id(self):
        return self._sandbox_id

    @property
    def nas_dir(self):
        return 'veracode/app{}'.format(self._app_ver_id)

    @sandbox_id.setter
    def sandbox_id(self, new_id):
        self._sandbox_id = new_id

    def insert_statement(self):
        sql = """
        insert into APP_VER (APP_VER_ID, SANDBOX_ID, PREV_APP_VER_ID,
        PLATFORM_ID, ACCOUNT_ID,
        LOGIN_ACCOUNT_ID, VERSION_LABEL, COMMENTS, NAS_DIR, LIFECYCLE_STAGE_ID,
        SHIP_TS, TPL_SEARCH_INDEX_VER, TPL_SEARCH_INDEX_STATE,
        CMP_TPL_SEARCH_INDEX_VER, CMP_TPL_SEARCH_INDEX_STATE,
        DELETED, DELETED_FILES, LAST_AUDITOR_ID, AUTOPUB_DISABLED, POLICY_ID,
        LAST_COMP_CHECK_TS,GRACE_TS,SCORE_GRACE_TS,SCAN_FREQ_TS,POLICY_STATUS,
        RULES_STATUS, POLICY_REASON, MIN_SCORE_STATUS, IS_DYNAMICMP,
        BINARIES_DELETED,
        SANITIZED, REMEDIATION_SCAN, REEVALUATE_SEVERITY,
        POLICY_EVALUATED_ON_ISSUE,INSERT_TS,
        MODIFIED_TS, MODIFIED_BY, RECORD_VER, AUTO_SCAN, PREFLIGHT_FILE_NAME,
        NON_FATAL_SCAN, SCA_RULE_STATUS, SCA_GRACE_TS, SUMMARIES_DELETED,
        RT_DELETED,
        LAST_SCA_MITIGATION_ID, LAST_POLICY_UPDATE_TS,NEEDS_REPORT_DATA_UPDATE,
        IS_ONEWAS,
        BINARIES_ARCHIVED, TEMPLATES_ARCHIVED, DELETED_EMPTY_EXEC_DIRS,
        BINARIES_ON_S3,
        S3_BUCKET_ID, IS_STACK_FRAME_DELETED)
        VALUES {} returning APP_VER_ID into :{1}""".format(
                params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_APP_VER', self.sandbox_id, None, 208, 1,
            10520, 'Mon Apr 06 22:26:58 EDT 2020', None, self.nas_dir, 807,
            None, None, 1, None, 1, 0, 0,
            '42524238-3376-485e-a768-c5888b2664df', 0, 7,
            '06-APR-20 11.07.04.300000000 PM',
            '01-FEB-00 12.00.00.000000000 AM',
            '01-FEB-00 12.00.00.000000000 AM',
            None, 5, 5, 4, 5, 0, 0, 0, 0, 0, 1,
            '06-APR-20 10.26.58.704000000 PM',
            '06-APR-20 11.07.04.344814000 PM',
            'internal', 4, 0, None, 0, 2, None,
            0, 0, None,
            '06-APR-20 10.26.58.703000000 PM',
            0, 0, 0, 0, 1, 0, -1, 0, id_
        )
        return values


class Analysis:
    def __init__(self):
        self.name = 'analysis'
        self.id_column = 'ANALYSIS_ID'
        self._analysis_id = None
        self._app_ver_id = None
        self._column_count = 8

    @property
    def id(self):
        return self._analysis_id

    @id.setter
    def id(self, new_id):
        self._analysis_id = new_id

    @property
    def app_ver_id(self):
        return self._app_ver_id

    @app_ver_id.setter
    def app_ver_id(self, new_id):
        self._app_ver_id = new_id

    def insert_statement(self):
        sql = """
        insert into ANALYSIS (ANALYSIS_ID, ANALYSIS_NAME,
        APP_VER_ID, REVIEWED_TS, INSERT_TS, MODIFIED_TS,
        MODIFIED_BY, RECORD_VER)
        VALUES {} returning ANALYSIS_ID into :{1}""".format(
            params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_ANALYSIS', 'initial',
            self.app_ver_id, None,
            '6-APR-20 10.26.58.750000000 PM',
            '06-APR-20 10.26.58.750000000 PM',
            'onewas-test', 1, id_
        )
        return values


class AnalysisUnit:
    def __init__(self):
        self.name = 'analysis_unit'
        self.id_column = 'ANALYSIS_UNIT_ID'
        self._analysis_unit_id = None
        self._analysis_id = None
        self._column_count = 49

    @property
    def id(self):
        return self._analysis_unit_id

    @id.setter
    def id(self, new_id):
        self._analysis_unit_id = new_id

    @property
    def analysis_id(self):
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, new_id):
        self._analysis_id = new_id

    def insert_statement(self):
        sql = """
        insert into ANALYSIS_UNIT (ANALYSIS_UNIT_ID, ANALYSIS_ID,ANALYSIS_TYPE,
        NAS_DIR, REPORTS_AVAIL, SCAN_STATUS_ID, HAS_PREFLIGHT_RESULT,
        CREATOR_LOGIN_ACCOUNT_ID, SUBMITTER_LOGIN_ACCOUNT_ID, PUBLISH_TS,
        FIRST_PUBLISH_TS, ERROR_MSG_ID,ANALYSIS_SIZE_BYTES,NUM_SCANS,SUBMIT_TS,
        ESTIMATE_READY_TS, ENHANCED_DYN, SLO_TS, EXTEND_SLO, BETA_SLO,
        SALES_PUBLISH_PRIORITY, PROGRESS_SCORE, WEBAPP, AUTO_PUB_STATUS,
        DYNAMIC_SCAN_TYPE,
        HAS_NESTED_ARCHIVE,ETA_HOURS,ETA_ESTIMATE_TYPE, ESTIMATE_READY_TS_ORIG,
        SUPPRESSED_LOGIN_ERROR,SUPPRESSED_LOGIN_ERROR_ONLY,SCAN_RUNNING_OFFLINE,
        DELETED, ENGINE_VERSION, VENDOR_RESCAN, PROMOTE_FROM_SCAN_ID,AUTO_SCAN,
        SANITIZED, INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER,
        FIXED_FLAW_STATE,
        IS_PARTIAL_RESULTS_READY, SENT_INCREMENTAL_PUBLISH_EMAIL,
        NEEDS_FIXED_REOPENED_RECALC,
        CODEBASE_PRICING_SIZE, USED_CODEBASE_PRICING_SIZE,
        UNSUBMITTED_STATIC_NOTICE_TS)
        VALUES {} returning ANALYSIS_UNIT_ID into :{1}""".format(
                params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_ANALYSIS_UNIT', self.analysis_id, 4,
            'veracode/app157399/ver69555/analysis69576/analysisUnit169536',
            0, 711, 0, 10520, None,
            '06-APR-20 11.06.18.886000000 PM',
            '06-APR-20 11.06.18.886000000 PM',
            None, None, None, None, None, 0,
            None, None, None, None, 100, 0,
            2, 3, 0, 0, None, None, 0, 0, 0,
            0, None, 0, None, 0, 0,
            '06-APR-20 10.26.58.755000000 PM',
            '07-APR-20 12.06.01.340044000 AM',
            'internal', 7, 1, 0, 0, 0, None,
            0, None, id_
        )
        return values


class EngineJob:
    def __init__(self):
        self.name = 'engine_job'
        self.id_column = 'ENGINE_JOB_ID'
        self._engine_job_id = None
        self._app_ver_id = None
        self._analysis_unit_id = None
        self._remote_job_id = None
        self._column_count = 62

    @property
    def remote_job_id(self):
        return self._remote_job_id

    @remote_job_id.setter
    def remote_job_id(self, new_id):
        self._remote_job_id = new_id

    @property
    def analysis_unit_id(self):
        return self._analysis_unit_id

    @analysis_unit_id.setter
    def analysis_unit_id(self, new_id):
        self._analysis_unit_id = new_id

    @property
    def app_ver_id(self):
        return self._app_ver_id

    @app_ver_id.setter
    def app_ver_id(self, new_id):
        self._app_ver_id = new_id

    @property
    def id(self):
        return self._engine_job_id

    @id.setter
    def id(self, new_id):
        self._engine_job_id = new_id

    def insert_statement(self):
        sql = """
        insert into ENGINE_JOB (ENGINE_JOB_ID, STATUS, PRIMARY_JOB_ID,
        IS_BACKUP, STATUS_STRING,TYPE,ENGINE_MACHINE_ID,APP_VER_ID,
        EXEC_UNIT_VER_ID,ANALYSIS_UNIT_ID, NAME,LOGIN_ACCOUNT_ID,ACCOUNT_ID,
        MACHINE_GROUP_ID,ENGINE_VERSION,RUN_VER_ID, PRIORITY,SUBMIT_TIME,
        START_TIME,STOP_TIME,LLRN_TIME,MACHINE_NAME,XML_PATH,XML_RESULT_FILE,
        COPY_RESULT_PATH,COPY_SUMMARIZATION_PATH,COPY_RESULT_RUN_VER_ID,
        COPY_SUMMARY_RUN_VER_ID,BINARY_PATH,SUMMARY_FILE_PATH,USES_SUMMARIES,
        READ_RESULTS,STATUS_XML,START_PHASE,ANALYSIS_TYPE,MAXVM,TRACK_C,
        RESULTS_FILE_TRACK_C,IS_LATEST,SAF_PID,DYNAMIC_SCAN_TYPE,COMMUNICATION_TYPE,
        S2_FILE_PATH,S2_PREVIOUS_PATH,OWNERSHIP_TOKEN,TMP_STATUS,IS_RECENT_JOB,
        SKIP_FAST_LANE,PARALLEL_SCAN_TYPE,PARALLEL_SCAN_SLICE,MODEL_JOB_ID,DYN_SUM_STATS,
        INSERT_TS,MODIFIED_TS,MODIFIED_BY,RECORD_VER,SCANNER_NAME,REMOTE_JOB_ID,
        RESULT_FILES_DELETED,XPA_ENABLED,S3_ONLY,S3_BUCKET_ID)
        VALUES {} returning ENGINE_JOB_ID into :{1}""".format(
                params_as_list(self._column_count), self._column_count+1)
        return sql

    def values_to_insert(self, id_):
        values = (
            'SEQ_ENGINE_JOB', 2, None, 0, 'completed',
            2, None, self.app_ver_id, 331559,
            self.analysis_unit_id,
            'http://rome.cloudloop.veracodelabs.com/',
            10520, 1, 10192, None, 106133, 5,
            '06-APR-20 10.26.58.998000000 PM',
            '06-APR-20 10.32.43.384000000 PM',
            '06-APR-20 11.05.49.405000000 PM',
            None, 'onewas-remote-engine:9080',
            'veracode/app157399/ver69555/execunits/331559/runvers/106133',
            None, None, None, 0, 0, None, None,
            0, 1, 'One WAS status', None, 4, 0,
            1, 0, 1, 0, 3, 3, None, None, None,
            -1, 1, 0, None, None, None, 0,
            '06-APR-20 10.26.59.000000000 PM',
            '06-APR-20 11.06.18.755436000 PM',
            'internal', 6, None, self.remote_job_id,
            0, 0, 0, -1, id_
        )
        return values


class AnalysisUnitDynOp:
    def __init__(self):
        self.name = 'analysis_unit_dyn_op'
        self.id_column = 'ANALYSIS_UNIT_DYN_OP_ID'
        self._analysis_unit_dyn_op_id = None
        self._analysis_unit_id = None
        self._engine_job_id = None
        self._column_count = 28

    @property
    def engine_job_id(self):
        return self._engine_job_id

    @engine_job_id.setter
    def engine_job_id(self, new_id):
        self._engine_job_id = new_id

    @property
    def analysis_unit_id(self):
        return self._analysis_unit_id

    @analysis_unit_id.setter
    def analysis_unit_id(self, new_id):
        self._analysis_unit_id = new_id

    @property
    def id(self):
        return self._analysis_unit_dyn_op_id

    @id.setter
    def id(self, new_id):
        self._analysis_unit_dyn_op_id = new_id

    def insert_statement(self):
        sql = """
        insert into  analysis_unit_dyn_op (ANALYSIS_UNIT_DYN_OP_ID,
        ANALYSIS_UNIT_ID, EXEC_UNIT_VER_ID, ENGINE_JOB_ID, IS_PRE_SCAN,
        HAVE_SCAN_RESULTS, FREE_DISK_MB, SVN_REVISION, EXIT_STATUS, STOP_TIME,
        STATE, LOGIN_SUCCESSES, LOGIN_FAILURES, DURATION, REQUESTS,
        RESPONSES, LINKS, NETWORK_ERRORS, PORT_SHUTDOWNS, BYTES_SENT,
        BYTES_RECEIVED, FORCE_COMPLETE_EXIT_STATUS, SCAN_EXIT_STATUS,
        INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER, TOTAL_DURATION)
        VALUES {}""".format(params_as_list(self._column_count))
        return sql

    def values_to_insert(self):
        values = (
            'SEQ_ANALYSIS_UNIT_DYN_OP', self.analysis_unit_id,
            331560, self.engine_job_id,
            0, 1, 36692, '20.3.3', None,
            None, 'Completed', 0, 0,
            1986021, 0, 0, 1, 0, 0, 0,
            0, None, 16, '06-APR-20 10:22:23',
            '08-APR-20 10:22:23', 'reportconsumer',
            2, 1986021
        )
        return values


class AnalysisUnitDynParams:
    def __init__(self):
        self.name = 'analysis_unit_dyn_params'
        self.id_column = 'ANALYSIS_UNIT_DYN_PARAMS_ID'
        self._analysis_unit_dyn_params_id = None
        self._analysis_unit_id = None
        self._column_count = 63

    @property
    def analysis_unit_id(self):
        return self._analysis_unit_id

    @analysis_unit_id.setter
    def analysis_unit_id(self, new_id):
        self._analysis_unit_id = new_id

    @property
    def id(self):
        return self._analysis_unit_dyn_params_id

    @id.setter
    def id(self, new_id):
        self._analysis_unit_dyn_params_id = new_id

    def insert_statement(self):
        sql = """
        insert into ANALYSIS_UNIT_DYN_PARAMS (ANALYSIS_UNIT_DYN_PARAMS_ID,
        ANALYSIS_UNIT_ID, TARGET_URL, TARGET_IP, RESTRICT_TO_DIR, MAX_LINKS,
        RESPONSE_TIMEOUT, EXCLUDE_PORTIONS, LOGIN_REQUIRED,BROWSER_BASED_LOGIN,
        SCRIPT_BASED_LOGIN, CLIENT_CERT_AUTH, LOGIN_USERNAME, LOGIN_SSO_URL,
        NTLM_DOMAIN_NAME, ENHANCED_DYN,SPECIAL_INSTRUCTIONS,IT_CONT_FIRST_NAME,
        IT_CONT_LAST_NAME, IT_CONT_PHONE, IT_CONT_EMAIL, LOGIN_SEQ_FILE_NAME,
        VERIFICATION_URL, VERIFICATION_TEXT, SPEC_CRAWL_SEQ_REQUIRED,
        CRAWL_SEQ_FILE_NAME, CRAWL_SEQ_FILE_TYPE, USER_AGENT,
        CLIENT_CERT_FILE_NAME,
        SANITIZED, VERACODE_DYNAMIC_THRESHOLD, CUSTOM_PLUGIN_CONFIGURATION,
        DISABLE_HTML_CRAWLER,DYNAMIC_TEMPLATE_SOURCE,CERTIFIED,ALLOW_AUTO_SCAN,
        DYN_SCAN_NEEDS_APPROVAL, DYN_SCAN_ON_VSA_NEEDS_APPROVAL,
        DYN_SCAN_HOLDS_RELEASED,
        BOTH_HTTP_HTTPS, LOGOUT_DETECTOR, VSA_ID, VSA_GROUP_ID,
        OVERRIDE_GROUP_ID,
        SCAN_USE_CUSTOM_JSON, AUTO_LOGIN_REQUIRED, AUTO_LOGIN_USERNAME,
        AUTO_LOGIN_VERIFY_COMMAND, SHELL_SHOCK_ONLY_SCAN, IS_SCAN_RESUME,
        INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER, MULTITHREADING,
        RESCAN_TYPE,
        VERIFY_FLAW_COUNT, ALTERNATOR_MODE, LOGOUT_SEQ_FILE_NAME,
        CUSTOM_DEFINED_TECHNOLOGIES,
        CRAWL_DEPTH_LIMIT, MAX_EXCHANGES_PER_LINK, SUBDIRECTORY_LIMIT)
        VALUES {}""".format(params_as_list(self._column_count))
        return sql

    def values_to_insert(self):
        values = (
            'SEQ_ANALYSIS_UNIT_DYN_PARAMS', self.analysis_unit_id,
            'http://rome.cloudloop.veracodelabs.com/plugintest/',
            None, 0, 5000, 100, None, 0, 0,
            0, 0, None, None, None, 0, None,
            'Alex', 'Deng', 1234, 'adeng@veracode.com',
            None, None, None, 0, None, 0,
            '"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/72.0.3626.0 Safari/537.36\
            /Veracode Security scan/support@veracode.com"',
            None, 0, 60, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, None, None, None, 0, 0,
            None, None, 0, 0,
            '13-APR-20 03.49.28.651000000 PM',
            '13-APR-20 03.54.13.359395000 PM',
            'reportconsumer', 3, 1,
            None, 221, 1, None, 0, 0, 0, 0
        )
        return values


class ScanEncrypt:
    def __init__(self):
        self.name = 'scan_encrypt'
        self.id_column = 'SCAN_ENCRYPT_ID'
        self._scan_encrypt_id = None
        self._app_ver_id = None
        self._column_count = 13

    @property
    def app_ver_id(self):
        return self._app_ver_id

    @app_ver_id.setter
    def app_ver_id(self, new_id):
        self._app_ver_id = new_id

    @property
    def id(self):
        return self._scan_encrypt_id

    @id.setter
    def id(self, new_id):
        self._scan_encrypt_id = new_id

    def insert_statement(self):
        sql = """
        insert into SCAN_ENCRYPT (SCAN_ENCRYPT_ID, APP_VER_ID, ALIAS,
        ENCRYPT_KEY, ENCRYPT_IV, ENCRYPT_METHOD_ID, INSERT_TS,
        MODIFIED_TS, MODIFIED_BY, RECORD_VER, KPK_INFO_ID, KPK_STATUS_ID,
        NEEDS_REKEY) Values {}""".format(params_as_list(self._column_count))
        return sql

    def values_to_insert(self):
        values = (
            'SEQ_SCAN_ENCRYPT', self.app_ver_id, None,
            '010201007832ae2082d802f9cb9d420cd6abc3c\
1badd954470d0f0b95bfd14f49fb29fbd1e01613d\
b2bfd8e61d3b303e29c41aba693a0000008f30818\
c06092a864886f70d010706a07f307d02010030780\
6092a864886f70d010701301e0609608648016503\
04012e3011040cfa3d1bbb0fbb026f5a4cbeca0201\
10804bb4d7c64f673b04b867d0a405413b796efb3\
fae3d78d49bc8cb351c455bba7d7b2685471b7c15\
b420ecbe26c08a6269fb000e73f457a8b651bf33fb\
6c48342f68bd60327b84ecd1b093e0da',
            None, 7,
            '13-APR-20 04.04.39.946000000 PM',
            '13-APR-20 04.04.39.946000000 PM',
            'onewas-test', 1, None, 0, 0
        )
        return values


class AnalysisUnitScanWindow:
    def __init__(self):
        self.name = 'analysis_unit_scan_window'
        self.id_column = 'ANALYSIS_UNIT_SCAN_WINDOW_ID'
        self._analysis_unit_scan_window_id = None
        self._analysis_unit_id = None
        self._column_count = 10

    @property
    def analysis_unit_id(self):
        return self._analysis_unit_id

    @analysis_unit_id.setter
    def analysis_unit_id(self, new_id):
        self._analysis_unit_id = new_id

    @property
    def id(self):
        return self._analysis_unit_scan_window_id

    @id.setter
    def id(self, new_id):
        self._analysis_unit_scan_window_id = new_id

    def insert_statement(self):
        sql = """
        Insert into ANALYSIS_UNIT_SCAN_WINDOW (ANALYSIS_UNIT_SCAN_WINDOW_ID,
        ANALYSIS_UNIT_ID, START_TIME, END_TIME, RUN_IMMEDIATELY, DURATION,
        INSERT_TS, MODIFIED_TS, MODIFIED_BY, RECORD_VER)
        VALUES {}""".format(params_as_list(self._column_count))
        return sql

    def values_to_insert(self):
        values = (
            'SEQ_ANALYSIS_UNIT_SCAN_WINDOW',
            self.analysis_unit_id,
            '13-APR-20 06.33.09.404000000 PM',
            '19-APR-20 06.33.00.000000000 PM',
            0, 0,
            '13-APR-20 06.33.09.410000000 PM',
            '13-APR-20 06.33.09.410000000 PM',
            'mqiu@veracode.com', 1
        )
        return values
