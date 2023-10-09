from connect_to_db import *

def create_db_tables(connection, cursor):
    print('create_db_tables: started')
    try:

        print('create_db_tables: creating customers')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sample_table (
                customer_id INT IDENTITY(1, 1) PRIMARY KEY,
                customer_name VARCHAR(250) NOT NULL
            );
          """)

        connection.commit()
        print('create_db_tables: committed')

        print('create_db_tables: done')
    except Exception as ex:
        print(f'create_db_tables: failed to run sql: {ex}')
        raise ex
