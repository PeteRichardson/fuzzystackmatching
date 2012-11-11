# stacktrace_gateway.py - python class to handle stacktraces db

import psycopg2


class ST_Gateway:

    CREATE = '''CREATE TABLE stacktraces (
                    st_id SERIAL PRIMARY KEY,
                    st_sig VARCHAR(200),
                    st_stacktrace TEXT
                )'''

    DELETE = "DROP TABLE IF EXISTS stacktraces;"

    INSERT = "INSERT INTO stacktraces (st_stacktrace, st_sig) " +\
             "VALUES ('{0}', '{1}')"

    FIND = "SELECT * FROM stacktraces WHERE st_sig='{0}'"

    def __init__(self):
        self.conn = None

    def connect(self):
        '''establish a connection to the db.
           No effect if it already exists'''
        self.conn = psycopg2.connect(host='localhost',
                        database='work',
                        user='pete',
                        password='slartybartfast')

    def execute(self, sql):
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()

        except psycopg2.DatabaseError, e:

            if self.conn:
                self.conn.rollback()

            raise e

        finally:
            if self.conn:
                self.conn.close()

    def create(self):
        '''create the stacktraces table'''
        self.connect()
        self.execute(self.CREATE)

    def delete(self):
        '''delete the stacktraces table'''
        self.execute(self.DELETE)

    def insert(self, stacktrace, signature):
        '''insert a stacktrace and signature into the db'''
        sql = self.INSERT.format(stacktrace, signature)
        self.execute(sql)

    def find_matches(self, signature):
        sql = self.FIND.format(signature)
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

if __name__ == '__main__':
    st = ST_Gateway()
    st.delete()
    st.create()
    st.insert("foo", "bar")
    cur = st.find_matches("bar")
    for row in cur:
        print row