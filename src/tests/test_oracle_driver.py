def test_import_oracle():
    try:
        import cx_Oracle
    except ImportError:
        print('You have to install cx_Oracle')
        assert False
    else:
        print('Python interface to Oracle Database version:', cx_Oracle.__version__)
        assert True