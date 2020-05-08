from was_service_automation.utils.clients import db_client as client


def params_as_list(params_count):
    """
    params_as_list(params_count=integer) -> string like "(:1, :2, ...)"

    Returns a string with as many place holders(:1) as `params_count`.
    """
    placeholder_list = []
    for i in range(1, params_count + 1):
        placeholder_list.append(':{}'.format(i))
    return "({})".format(", ".join(placeholder_list))


def get_max_id(db_table, id_column_name):
    print(client.dsn)
    print(client.username)
    print(client.password)
    """
    get_max_id(db_table=str, id_column_name=str) -> int
    Returns max value for identity column in table with name 'db_table'.
    """
    sql = "select max({}) from {}".format(id_column_name, db_table)
    client.execute(sql)
    return client.fetchone()[0]
