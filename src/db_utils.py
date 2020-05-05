def params_as_list(params_count):
    """
    params_as_list(params_count=integer) -> string like "(:1, :2, ...)"

    Returns a string with as many place holders (:1) as `params_count`.
    """
    placeholder_list = []
    for i in range(1, params_count+1):
        placeholder_list.append(':{}'.format(i))
    return "({})".format(", ".join(placeholder_list))

