
import psycopg2

class DBConnection(object):
    def __init__(self, db_name = None, user = None, password = None, host = 'localhost'):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
    
    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname = self.db_name,
            host = self.host,
            user = self.user,
            password = self.password
        )
        return self.connection.cursor()
    
    def __exit__(self, exception_type, exception_instance, traceback):
        self.connection.close()

# Sample querying
with DBConnection(user = 'foo', db_name = 'bar') as db:
    db.execute('SELECT 1 + 1')
    db.fetchall()
