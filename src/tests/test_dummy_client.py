import cx_Oracle

from db_client import db_client as client
from db_utils import get_max_id


#def test_drop_table():
    #client = DBClient()
    #try:
        #cursor.execute("DROP TABLE identity_demo")
    #except cx_Oracle.DatabaseError as e:
        #print(e)
        #assert False
    #else:
        #assert True


def test_create_table():
    try:
        client.execute("CREATE TABLE identity_demo (\
        id NUMBER GENERATED ALWAYS AS IDENTITY,\
        description VARCHAR2(100) not null)")
    except cx_Oracle.DatabaseError as e:
        print(e)
        assert False
    else:
        assert True


def test_insert():
    try:
        client.execute("INSERT INTO identity_demo(description)\
VALUES('Oracle identity column demo with GENERATED ALWAYS')")
    except cx_Oracle.DatabaseError as e:
        print(e)
        assert False
    else:
        assert True


def test_get_max_id():
    try:
        max_id = get_max_id("identity_demo", "id")
    except cx_Oracle.DatabaseError as e:
        print(e)
        assert False
    else:
        print('Max ID:', max_id)
        assert True
