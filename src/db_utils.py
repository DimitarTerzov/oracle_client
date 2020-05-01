from db_client import db_client as client


def insert_in_analysis_unit_dyn_op(values):
    """
    insert_in_analysis_unit_dyn_op(values=list) -> None

    Inserts new row with incremented 'id' in table `analysis_unit_dyn_op`.
    'values' should not contain value for 'id'.
    """
    max_id = get_max_id('analysis_unit_dyn_op', 'ANALYSIS_UNIT_DYN_OP_ID')
    max_id += 20000

    sql = """INSERT INTO analysis_unit_dyn_op (
    ANALYSIS_UNIT_DYN_OP_ID, ANALYSIS_UNIT_ID, EXEC_UNIT_VER_ID, ENGINE_JOB_ID, IS_PRE_SCAN,
    HAVE_SCAN_RESULTS, FREE_DISK_MB, SVN_REVISION, EXIT_STATUS, STOP_TIME,
    STATE, LOGIN_SUCCESSES, LOGIN_FAILURES, DURATION, REQUESTS,
    RESPONSES, LINKS, NETWORK_ERRORS, PORT_SHUTDOWNS, BYTES_SENT,
    BYTES_RECEIVED, FORCE_COMPLETE_EXIT_STATUS, SCAN_EXIT_STATUS, INSERT_TS, MODIFIED_TS,
    MODIFIED_BY, RECORD_VER, TOTAL_DURATION) VALUES {}""".format(_params_as_list(values))

    values.insert(0, max_id)
    client.execute(sql, values)


def get_max_id(db_table, id_column_name):
    """
    get_max_id(db_table=str, id_column_name=str) -> int
    Returns max value for identity column in table with name 'db_table'.
    """
    sql = "select max({}) from {}".format(id_column_name, db_table)
    client.execute(sql)
    return client.fetchone()[0]


def _params_as_list(nums_list):
    """
    _params_as_list(nums_list=iterable) -> string like "(?, ?, ...)"

    Returns a string with as many ? as the length of `nums_list`.
    """
    placeholder_list = ["?"] * len(nums_list)
    return "(?, {})".format(", ".join(placeholder_list))

