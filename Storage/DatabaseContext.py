import pyodbc

# TODO Create DB_CONTEXT as a Class

def db_connection(os):
    SQL_DRIVER = os.getenv('SQL_DRIVER')
    SQL_SERVER = os.getenv('SQL_SERVER')
    SQL_DATABASE = os.getenv('SQL_DATABASE')
    SQL_TRUSTED_CONNECTION = os.getenv('SQL_TRUSTED_CONNECTION')

    return pyodbc.connect('Driver='+SQL_DRIVER+';Server='+SQL_SERVER+';Database='+SQL_DATABASE+';'+'Trusted_Connection='+SQL_TRUSTED_CONNECTION+';')

def insert_server_config(os, id, prefix):
    db_context = db_connection(os)
    cursor = db_context.cursor()

    cursor.execute('INSERT INTO SERVER_CONFIGURATION (ID, PREFIX)VALUES ('+str(id)+', \''+prefix+'\');')
    cursor.close()
    
    db_context.commit()
    db_context.close()
    