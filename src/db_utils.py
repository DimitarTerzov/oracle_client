def params_as_list(params_count):
    """
    _params_as_list(params_count=integer) -> string like "(?, ?, ...)"

    Returns a string with as many ? as `params_count`.
    """
    placeholder_list = ["?"] * params_count
    return "({})".format(", ".join(placeholder_list))

