def get_max_id(db_table, id_column_name):
    """
    get_max_id(db_table=str, id_column_name=str) -> int
    Returns max value for identity column in table with name 'db_table'.
    """
    sql = "select max({}) from {}".format(id_column_name, db_table)
    client.execute(sql)
    return client.fetchone()[0]


def params_as_list(params_count):
    """
    _params_as_list(params_count=integer) -> string like "(?, ?, ...)"

    Returns a string with as many ? as `params_count`.
    """
    placeholder_list = ["?"] * params_count
    return "({})".format(", ".join(placeholder_list))

