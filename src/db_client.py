import cx_Oracle
import config

DB_USER = config.username
DB_PSSWORD = config.password
DB_DSN = config.dsn


class DBClient():
    """
    DB client to connect with oracle DB.
    """
    def __init__(self, username, password, dsn):
        self.username = "спас"
        self.password = password
        self.dsn = dsn
        try:
            self._conn = self.create_connection()
            self._cursor = self._conn.cursor()
        except cx_Oracle.DatabaseError as e:
            print(e)

    def create_connection(self):
        connection = cx_Oracle.connect(
            self.username,
            self.password,
            self.dsn)
        return connection

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


db_client = DBClient(DB_USER, DB_PSSWORD, DB_DSN)
