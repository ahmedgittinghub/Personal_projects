from python_packages5 import *
import pymysql
import os
from dotenv import load_dotenv
from sql_packages import * 

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


connection, cursor = setup_db_connection()





table_printer('products',cursor)
            
                
         

# a = ['1','2','3']
# a = ','.join(a)

# b = ['4','5','6']
# b = ','.join(b)
# c = a + ',' + b
# print(c)

# list1 = ''
# order_id = 1
# list1 = itemise_items(order_id,list1)

# print(list1)


query = f"SELECT * FROM products"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)
    print('\n')


cursor1 = connection.cursor()






