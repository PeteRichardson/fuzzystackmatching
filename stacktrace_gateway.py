'''stacktrace_gateway.py - python class to handle stacktraces db'''

import psycopg2


class STGateway:
    
    '''python class to handle stacktraces db'''

    CREATE = '''CREATE TABLE stacktraces (
                    st_id SERIAL PRIMARY KEY,
                    st_sig VARCHAR(128),
                    st_stacktrace TEXT,
                    st_issue VARCHAR(20)
                )'''

    DELETE = "DROP TABLE IF EXISTS stacktraces;"

    INSERT = "INSERT INTO stacktraces (st_issue, st_stacktrace, st_sig) " +\
             "VALUES ('{0}', '{1}', '{2}')"

    FIND2 = "SELECT * FROM stacktraces WHERE st_sig='{0}'"
    FIND = "SELECT st_issue, LEVENSHTEIN('{0}', st_sig) FROM stacktraces " +\
            "WHERE LEVENSHTEIN('{0}', st_sig) < 4;"

    def __init__(self):
        self.conn = None

    def connect(self):
        '''establish a connection to the db.
           No effect if it already exists'''
        if self.conn == None:
            self.conn = psycopg2.connect(host='localhost',
                            database='work',
                            user='pete',
                            password='slartybartfast')

    def execute(self, sql):
        '''execute a single statement against the db.
           For now it always opens and closes the connection.
           Not very efficient.'''
        try:
            self.connect()
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()

        except psycopg2.DatabaseError, exception:

            if self.conn:
                self.conn.rollback()

            raise exception

        finally:
            if self.conn:
                self.conn.close()
                self.conn = None

    def create(self):
        '''create the stacktraces table'''
        self.execute(self.CREATE)

    def delete(self):
        '''delete the stacktraces table'''
        self.execute(self.DELETE)

    def insert(self, issue, stacktrace, signature):
        '''insert a stacktrace and signature into the db'''
        sql = self.INSERT.format(issue, stacktrace, signature)
        self.execute(sql)

    def find_matches(self, signature):
        '''use levenshtein distance < 4 against fuzzy hash
           to find matching stacktraces in db'''
        sql = self.FIND.format(signature)
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

if __name__ == '__main__':
    STG = STGateway()
    STG.delete()
    STG.create()
    STG.insert('jira-678', "foo", "bar")
    CURS = STG.find_matches("bar")
    for row in CURS:
        print row
