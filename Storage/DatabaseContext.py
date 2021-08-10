from asyncio.windows_events import NULL
import pyodbc

class DatabaseContext():
    def __init__(self, os):
        SQL_DRIVER = os.getenv('SQL_DRIVER')
        SQL_SERVER = os.getenv('SQL_SERVER')
        SQL_DATABASE = os.getenv('SQL_DATABASE')
        SQL_TRUSTED_CONNECTION = os.getenv('SQL_TRUSTED_CONNECTION')
        
        self.COMMAND_PREFIX = os.getenv('DISCORD_COMMAND_PREFIX')

        self.db_context = pyodbc.connect('Driver='+SQL_DRIVER+';Server='+SQL_SERVER+';Database='+SQL_DATABASE+';'+'Trusted_Connection='+SQL_TRUSTED_CONNECTION+';')
        self.cursor = self.db_context.cursor()
        return

    def close_context(self):
        self.cursor.close()
        self.db_context.commit()
        self.db_context.close()
        return

    def insert_or_update_server_config(self, id, prefix):
        self.cursor.execute('SELECT * FROM SERVER_CONFIGURATION WHERE ID = '+str(id)+';')
        if len(self.cursor.fetchall()) == 0:
            query = 'INSERT INTO SERVER_CONFIGURATION (ID, PREFIX)VALUES ('+str(id)+', \''+prefix+'\');'
        else:
            query = 'UPDATE SERVER_CONFIGURATION SET PREFIX = \''+prefix+'\' WHERE ID ='+str(id)+';'
        self.cursor.execute(query)

        self.close_context()
        return

    def insert_or_update_warns(self, server_id, user_id):
        query = 'SELECT * FROM USER_WARNS WHERE SERVER_ID = \''+str(server_id)+'\' and USER_ID = \''+str(user_id)+'\';'
        self.cursor.execute(query)
        if len(self.cursor.fetchall()) == 0:
            query = 'INSERT INTO USER_WARNS (SERVER_ID, USER_ID, WARNS) VALUES ('+str(server_id)+', \''+str(user_id)+'\', 1);'
            warns = 1
        else:
            self.cursor.execute('SELECT WARNS FROM USER_WARNS WHERE SERVER_ID = \''+str(server_id)+'\' and USER_ID = \''+str(user_id)+'\';')
            warns = self.cursor.fetchall()[0][0]
            warns += 1
            query = 'UPDATE USER_WARNS SET WARNS = '+ str(warns) + ' WHERE SERVER_ID = \''+str(server_id)+'\' AND USER_ID = \''+str(user_id)+'\';'

        self.cursor.execute(query)
        self.close_context()
        return warns

    def get_prefix_by_id(self, id):
        self.cursor.execute('SELECT * FROM SERVER_CONFIGURATION WHERE ID = '+str(id)+';')
        query_result = self.cursor.fetchall()

        self.close_context()

        if not query_result:
            return [(0,self.COMMAND_PREFIX)]

        return query_result
        